// Background service worker for Meeting Timer extension

chrome.action.onClicked.addListener(async (tab) => {
  // Check if we can inject scripts into this tab
  if (tab.url.startsWith('chrome://') || tab.url.startsWith('chrome-extension://')) {
    console.log('Cannot inject into chrome:// or extension pages');
    return;
  }

  try {
    // Inject CSS first
    await chrome.scripting.insertCSS({
      target: { tabId: tab.id },
      files: ['timer.css']
    });

    // Then inject the content script
    await chrome.scripting.executeScript({
      target: { tabId: tab.id },
      files: ['content.js']
    });
  } catch (err) {
    console.error('Failed to inject script:', err);
  }
});
