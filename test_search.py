from playwright.sync_api import sync_playwright

def test_open_site():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://www.ozon.ru")

        assert "ozon" in page.url.lower()

        browser.close()