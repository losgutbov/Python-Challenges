from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.bbc.com/news")
    page.get_by_label("Search BBC").click()
    page.get_by_placeholder("Search news, topics and more").fill("technology")
    page.get_by_test_id("search-input-search-button").click()
    for titulo in page.get_by_test_id("card-headline").all()[0:5]:
        print(titulo.text_content())
    browser.close()