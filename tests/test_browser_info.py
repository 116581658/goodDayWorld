from playwright.sync_api import sync_playwright

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)
page = browser.new_page()
page.goto("https://playwright.dev")

print(page.title())

# Keep browser alive
print("Browser will stay open... Press Ctrl+C to exit.")
while True:
    pass
