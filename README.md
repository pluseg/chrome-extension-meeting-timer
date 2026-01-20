# Meeting Timer - Chrome Extension

A Chrome extension for tracking speaker time during meetings with countdown timer and lap tracking functionality.

## Features

- ⏱️ **Editable Countdown Timer**: Customize time per speaker (default 5 minutes)
- 💾 **Persistent Settings**: Timer duration saved across sessions and pages
- 📊 **Total Meeting Time**: Tracks the overall meeting duration
- 🏃 **Lap Tracking**: Record each speaker's time separately
- 👁️ **Show/Hide**: Timer is hidden by default - only appears when you need it
- 🎯 **Draggable UI**: Move the timer anywhere on the page
- ⏯️ **Smart Controls**: Single Start/Pause/Resume button with Lap and Reset
- 🎨 **Modern Design**: Beautiful gradient UI with smooth animations
- ❌ **Remove Laps**: Hover over any lap to remove it

## Installation

### Load Unpacked Extension (Development Mode)

1. Open Google Chrome
2. Navigate to `chrome://extensions/`
3. Enable **Developer mode** (toggle in the top-right corner)
4. Click **Load unpacked**
5. Select the `chrome-extension-timer` folder
6. The extension icon should appear in your extensions toolbar

## Usage

### Show/Hide Timer

1. **Show Timer**: Click the ⏱️ button in the bottom-right corner to show the timer
2. **Hide Timer**: Click the 👁️ (eye) button in the timer header to hide it
3. The timer remembers if it was visible/hidden across page loads

### Set Timer Duration

1. When the timer is idle (not running), you'll see a number input field
2. Enter the desired minutes per speaker (1-99)
3. The setting is automatically saved and persists across all pages and sessions
4. Default is 5 minutes

### Basic Controls

1. **Drag to reposition** - Click and drag the header to move the timer anywhere on the page
2. **Start/Pause/Resume**: Single button that changes based on state
   - **Start** (green): Begin the countdown and total meeting time
   - **Pause** (yellow): Temporarily stop both timers
   - **Resume** (green): Continue from where you paused
3. **Lap**: Record current speaker's time and reset countdown for next speaker (only active while running)
4. **Reset**: Stop the timer and reset countdown - laps are cleared when you press Start again

### Timer Display

- **Max per Speaker**: Shows countdown from your configured time (editable when idle)
  - Input field appears when timer is idle
  - Turns red and pulses when time is up
  - Continues counting negative time if you go over
- **Total Time**: Displays the overall meeting duration

### Lap Management

- Each lap shows as "Speaker 1", "Speaker 2", etc.
- Displays the time each speaker used
- Hover over a lap to reveal the **×** (remove) button
- Click **×** to remove that lap from the list

### Minimize/Hide

- **Minimize**: Click the **−** button to collapse the timer body (header stays visible)
- **Expand**: Click **+** to expand it again
- **Hide**: Click the **👁️** button to completely hide the timer
- **Show**: Click the **⏱️** button (appears in bottom-right when hidden) to show the timer

## Workflow Example

1. **Daily standup starts**: Click the ⏱️ show button
2. **First speaker starts**: Click Start
3. **First speaker finishes**: Click Lap (their time is recorded)
4. **Next speaker starts**: Timer automatically resets to max time
5. **Meeting ends**: Click Reset, then hide the timer with 👁️
6. **Tomorrow**: Timer stays hidden until you need it again

## Customization

No code changes needed! Simply:
- Click the number input field when the timer is idle
- Enter your desired minutes (e.g., 3 for 3 minutes)
- Setting is automatically saved

## File Structure

```
chrome-extension-timer/
├── manifest.json       # Extension configuration
├── content.js          # Main timer logic and UI
├── timer.css          # Styling
├── icons/             # Extension icons
│   ├── icon16.png
│   ├── icon48.png
│   └── icon128.png
├── generate_icons.py  # Icon generator script
└── README.md          # This file
```

## Technical Details

- **Manifest Version**: 3 (latest Chrome extension standard)
- **Permissions**: `storage`, `activeTab`
- **Injection**: Content script runs on all URLs
- **Compatibility**: Chrome, Edge, and other Chromium-based browsers

## Tips

- The timer starts hidden by default - no distraction on regular browsing
- Timer settings (duration, visibility) persist across all tabs and sessions
- The timer stays on top of page content with a high z-index
- Timer state is isolated and won't interfere with the page's JavaScript
- Laps are preserved when you press Reset - they only clear when you start a new meeting
- Use the minimize feature to keep the timer small during presentations
- The show button (⏱️) always appears in the same position for easy access

## Troubleshooting

**Timer doesn't appear?**
- Refresh the page after installing the extension
- Check if the extension is enabled in `chrome://extensions/`

**Can't click buttons on the page?**
- Move the timer by dragging it to a different location

**Timer resets when navigating?**
- This is expected behavior - timer state (running/paused) resets on page load
- However, your settings (max time, visibility) are preserved

**Want to change the time limit mid-meeting?**
- You need to click Reset first to stop the timer
- Then you can edit the time input field
- Click Start to begin with the new duration

## Development

To modify the extension:

1. Make changes to the source files
2. Go to `chrome://extensions/`
3. Click the **Reload** button on the extension card
4. Refresh any tabs where you want to see the changes

## License

Free to use and modify for personal or commercial purposes.
