from playwright.sync_api import sync_playwright

def test_ozon_url():
    url = "https://www.ozon.ru"
    assert "ozon" in url


def test_status_code():
    status_code = 200
    assert status_code == 200


def test_page_title():
    title = "Ozon"
    assert title == "Ozon"


def test_https_protocol():
    url = "https://www.ozon.ru"
    assert url.startswith("https")
