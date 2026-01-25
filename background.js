// Background service worker for Meeting Timer extension

chrome.action.onClicked.addListener(async (tab) => {
  // tab.url might be undefined if we don't have permission for the page
  const url = tab.url || '';

  // Check if we can inject scripts into this tab
  // Restricted: chrome://, chrome-extension://, edge://, about:, and Chrome Web Store
  const isRestricted =
    url.startsWith('chrome://') ||
    url.startsWith('chrome-extension://') ||
    url.startsWith('edge://') ||
    url.startsWith('about:') ||
    url.includes('chrome.google.com/webstore');

  if (isRestricted || !url) {
    console.warn('Cannot inject into restricted page:', url || 'Unknown URL');
    return;
  }

  try {
    console.log('Injecting timer into tab:', tab.id);

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

    console.log('Injection successful');
  } catch (err) {
    console.error('Failed to inject script into tab ' + tab.id + ':', err.message || err);
  }
});
