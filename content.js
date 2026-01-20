(function () {
  'use strict';

  // Prevent multiple injections
  if (window.meetingTimerInjected) return;
  window.meetingTimerInjected = true;

  // Timer state
  let state = {
    currentTime: 5 * 60, // 5 minutes in seconds
    maxTime: 5 * 60,
    totalMeetingTime: 0,
    isPaused: false,
    isRunning: false,
    shouldClearLapsOnStart: false,
    laps: []
  };

  let countdownInterval = null;
  let totalTimeInterval = null;
  let isDragging = false;
  let dragOffset = { x: 0, y: 0 };
  let isResizing = false;
  let resizeStartX = 0;
  let resizeStartY = 0;
  let resizeStartWidth = 0;
  let resizeStartHeight = 0;

  // Load saved settings
  function loadSettings() {
    chrome.storage.sync.get(['maxTime'], (result) => {
      if (result.maxTime) {
        state.maxTime = result.maxTime;
        state.currentTime = result.maxTime;
      }
      updateDisplay();
    });
  }

  // Save settings
  function saveSettings() {
    chrome.storage.sync.set({
      maxTime: state.maxTime
    });
  }

  // Create timer UI
  const timerContainer = document.createElement('div');
  timerContainer.id = 'meeting-timer-extension';
  timerContainer.innerHTML = `
    <div class="timer-header" id="timer-drag-handle">
      <span class="timer-title">⏱️ Meeting Timer</span>
      <div class="header-buttons">
        <button class="timer-minimize" id="timer-minimize">−</button>
        <button class="timer-close" id="timer-close" title="Close timer">×</button>
      </div>
    </div>
    <div class="timer-body">
      <div class="timer-display">
        <div class="countdown-section">
          <div class="timer-label">Max per Speaker</div>
          <div class="countdown-time" id="countdown-display">05:00</div>
          <div class="time-inputs" id="time-inputs">
            <input type="number" class="time-input" id="time-input-minutes" min="0" max="99" placeholder="5" title="Minutes">
            <span class="time-separator">:</span>
            <input type="number" class="time-input" id="time-input-seconds" min="0" max="59" placeholder="00" title="Seconds">
          </div>
        </div>
        <div class="total-section">
          <div class="timer-label">Total Time</div>
          <div class="total-time" id="total-display">00:00</div>
        </div>
      </div>
      <div class="timer-controls">
        <button class="timer-btn start-pause" id="timer-start-pause">Start</button>
        <button class="timer-btn lap" id="timer-lap" disabled>Lap</button>
        <button class="timer-btn stop" id="timer-stop" disabled>Stop</button>
      </div>
      <div class="laps-container" id="laps-container"></div>
    </div>
    <div class="resize-handle" id="resize-handle"></div>
  `;

  document.body.appendChild(timerContainer);

  // Get elements
  const dragHandle = document.getElementById('timer-drag-handle');
  const closeBtn = document.getElementById('timer-close');
  const minimizeBtn = document.getElementById('timer-minimize');
  const resizeHandle = document.getElementById('resize-handle');
  const timerBody = timerContainer.querySelector('.timer-body');
  const countdownDisplay = document.getElementById('countdown-display');
  const totalDisplay = document.getElementById('total-display');
  const timeInputMinutes = document.getElementById('time-input-minutes');
  const timeInputSeconds = document.getElementById('time-input-seconds');
  const timeInputsContainer = document.getElementById('time-inputs');
  const startPauseBtn = document.getElementById('timer-start-pause');
  const lapBtn = document.getElementById('timer-lap');
  const stopBtn = document.getElementById('timer-stop');
  const lapsContainer = document.getElementById('laps-container');

  // Utility: Format time as MM:SS
  function formatTime(seconds) {
    const mins = Math.floor(Math.abs(seconds) / 60);
    const secs = Math.abs(seconds) % 60;
    const sign = seconds < 0 ? '-' : '';
    return `${sign}${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
  }

  // Update displays
  function updateDisplay() {
    countdownDisplay.textContent = formatTime(state.currentTime);
    totalDisplay.textContent = formatTime(state.totalMeetingTime);

    const minutes = Math.floor(state.maxTime / 60);
    const seconds = state.maxTime % 60;
    timeInputMinutes.value = minutes;
    timeInputSeconds.value = seconds.toString().padStart(2, '0');

    // Add warning class if time is up
    if (state.currentTime <= 0) {
      countdownDisplay.classList.add('time-warning');
    } else {
      countdownDisplay.classList.remove('time-warning');
    }

    // Show/hide time input based on state
    if (state.isRunning || state.isPaused) {
      timeInputsContainer.style.display = 'none';
      countdownDisplay.style.display = 'block';
    } else {
      timeInputsContainer.style.display = 'flex';
      countdownDisplay.style.display = 'none';
    }
  }

  // Start timer
  function startTimer() {
    if (state.isRunning) return;

    // Clear laps if reset was pressed
    if (state.shouldClearLapsOnStart) {
      state.laps = [];
      state.shouldClearLapsOnStart = false;
      renderLaps();
    }

    state.isRunning = true;
    state.isPaused = false;
    state.totalMeetingTime = 0;

    updateDisplay();

    // Start countdown
    countdownInterval = setInterval(() => {
      state.currentTime--;
      updateDisplay();

      // Optional: Alert when time is up
      if (state.currentTime === 0) {
        // Play a subtle alert or visual notification
        countdownDisplay.classList.add('time-warning');
      }
    }, 1000);


    // Start total time
    totalTimeInterval = setInterval(() => {
      state.totalMeetingTime++;
      updateDisplay();
    }, 1000);

    updateButtons();
  }

  // Pause timer
  function pauseTimer() {
    state.isPaused = true;
    state.isRunning = false;

    clearInterval(countdownInterval);
    clearInterval(totalTimeInterval);

    updateButtons();
  }

  // Stop timer (don't clear total time or laps immediately)
  function stopTimer() {
    state.isRunning = false;
    state.isPaused = false;
    state.currentTime = state.maxTime;
    state.shouldClearLapsOnStart = true; // Flag to clear laps on next start

    clearInterval(countdownInterval);
    clearInterval(totalTimeInterval);

    updateDisplay();
    updateButtons();
  }

  // Lap functionality
  function addLap() {
    const lapTime = state.maxTime - state.currentTime;
    const lap = {
      id: Date.now(),
      duration: lapTime,
      timestamp: new Date().toLocaleTimeString()
    };

    // Add to beginning (newest first)
    state.laps.unshift(lap);

    // Reset countdown for next speaker
    state.currentTime = state.maxTime;
    updateDisplay();
    renderLaps();
  }

  // Remove lap
  function removeLap(lapId) {
    state.laps = state.laps.filter(lap => lap.id !== lapId);
    renderLaps();
  }

  // Close/remove timer from page
  function closeTimer() {
    timerContainer.remove();
    window.meetingTimerInjected = false;
  }

  // Render laps list
  function renderLaps() {
    if (state.laps.length === 0) {
      lapsContainer.innerHTML = '';
      return;
    }

    lapsContainer.innerHTML = `
      <div class="laps-header">Speaker Times</div>
      ${state.laps.map((lap, index) => `
        <div class="lap-item" data-lap-id="${lap.id}">
          <span class="lap-number">Speaker ${index + 1}</span>
          <span class="lap-time">${formatTime(lap.duration)}</span>
          <button class="lap-remove" data-lap-id="${lap.id}">×</button>
        </div>
      `).join('')}
    `;

    // Add remove handlers
    lapsContainer.querySelectorAll('.lap-remove').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const lapId = parseInt(btn.dataset.lapId);
        removeLap(lapId);
      });
    });
  }

  // Update button states
  function updateButtons() {
    if (state.isRunning) {
      // Running state - show Pause button
      startPauseBtn.textContent = 'Pause';
      startPauseBtn.className = 'timer-btn pause';
      startPauseBtn.disabled = false;
      lapBtn.disabled = false;
      stopBtn.disabled = false;
    } else if (state.isPaused) {
      // Paused state - show Resume button
      startPauseBtn.textContent = 'Resume';
      startPauseBtn.className = 'timer-btn resume';
      startPauseBtn.disabled = false;
      lapBtn.disabled = true;
      stopBtn.disabled = false;
    } else {
      // Idle state - show Start button
      startPauseBtn.textContent = 'Start';
      startPauseBtn.className = 'timer-btn start-pause';
      startPauseBtn.disabled = false;
      lapBtn.disabled = true;
      stopBtn.disabled = true;
    }
  }

  // Button event listeners
  startPauseBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    if (state.isRunning) {
      pauseTimer();
    } else {
      startTimer();
    }
  });

  stopBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    stopTimer();
  });

  lapBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    addLap();
  });

  // Time input handlers
  function updateMaxTime() {
    const minutes = parseInt(timeInputMinutes.value) || 0;
    const seconds = parseInt(timeInputSeconds.value) || 0;
    state.maxTime = minutes * 60 + seconds;
    if (state.maxTime === 0) {
      state.maxTime = 5 * 60; // Default to 5 minutes if both are 0
    }
    state.currentTime = state.maxTime;
    updateDisplay();
    saveSettings();
  }

  timeInputMinutes.addEventListener('change', (e) => {
    e.stopPropagation();
    updateMaxTime();
  });

  timeInputSeconds.addEventListener('change', (e) => {
    e.stopPropagation();
    updateMaxTime();
  });

  timeInputMinutes.addEventListener('click', (e) => {
    e.stopPropagation();
  });

  timeInputSeconds.addEventListener('click', (e) => {
    e.stopPropagation();
  });

  // Close button handler
  closeBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    closeTimer();
  });

  // Minimize/Maximize functionality
  minimizeBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    timerContainer.classList.toggle('minimized');
    timerBody.classList.toggle('minimized');
    minimizeBtn.textContent = timerBody.classList.contains('minimized') ? '+' : '−';
  });

  // Drag functionality
  dragHandle.addEventListener('mousedown', (e) => {
    isDragging = true;
    dragHandle.style.cursor = 'grabbing';

    const rect = timerContainer.getBoundingClientRect();
    dragOffset.x = e.clientX - rect.left;
    dragOffset.y = e.clientY - rect.top;

    e.preventDefault();
  });

  document.addEventListener('mousemove', (e) => {
    if (!isDragging) return;

    const x = e.clientX - dragOffset.x;
    const y = e.clientY - dragOffset.y;

    // Keep within viewport bounds
    const maxX = window.innerWidth - timerContainer.offsetWidth;
    const maxY = window.innerHeight - timerContainer.offsetHeight;

    const boundedX = Math.max(0, Math.min(x, maxX));
    const boundedY = Math.max(0, Math.min(y, maxY));

    timerContainer.style.left = `${boundedX}px`;
    timerContainer.style.top = `${boundedY}px`;
    timerContainer.style.right = 'auto';
    timerContainer.style.bottom = 'auto';
  });

  document.addEventListener('mouseup', () => {
    if (isDragging) {
      isDragging = false;
      dragHandle.style.cursor = 'grab';
    }
    if (isResizing) {
      isResizing = false;
    }
  });

  // Resize functionality
  resizeHandle.addEventListener('mousedown', (e) => {
    isResizing = true;
    resizeStartX = e.clientX;
    resizeStartY = e.clientY;
    resizeStartWidth = timerContainer.offsetWidth;
    resizeStartHeight = timerContainer.offsetHeight;
    e.preventDefault();
    e.stopPropagation();
  });

  document.addEventListener('mousemove', (e) => {
    if (!isResizing) return;

    const deltaX = e.clientX - resizeStartX;
    const deltaY = e.clientY - resizeStartY;

    const newWidth = Math.max(280, resizeStartWidth + deltaX);
    const newHeight = Math.max(200, resizeStartHeight + deltaY);

    timerContainer.style.width = `${newWidth}px`;
    timerContainer.style.height = `${newHeight}px`;
  });

  // Prevent timer from interfering with page
  timerContainer.addEventListener('click', (e) => {
    e.stopPropagation();
  });

  resizeHandle.addEventListener('click', (e) => {
    e.stopPropagation();
  });

  // Initialize
  loadSettings();
  updateDisplay();
  updateButtons();

})();
