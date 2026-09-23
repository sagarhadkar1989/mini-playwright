from playwright.sync_api import sync_playwright

def test_google_search():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto("https://qaplayground.com/practice/input-fields")
        page.fill("input[id='movieNameInput']", "Playwright Python")
        assert page.get_attribute("input#movieNameInput", "value") == "Playwright Python"
        browser.close()
