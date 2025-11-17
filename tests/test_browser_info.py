def test_browser_name(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://playwright.dev")
    print("Using browser: Chromium")
    # browser.close()
    input("Browser is running. Press ENTER to close...")