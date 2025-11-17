def test_browser_name(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    print("Using browser: Chromium")
    browser.close()
