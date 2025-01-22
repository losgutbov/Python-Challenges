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

# SOLUÇÃO MELHORADA DO MEU CÓDIGO PELO CHAT GPT

# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()

#     # Navega até o site da BBC
#     page.goto("https://www.bbc.com/news")

#     # Realiza a pesquisa
#     page.get_by_label("Search BBC").click()
#     page.get_by_placeholder("Search news, topics and more").fill("technology")
#     page.get_by_test_id("search-input-search-button").click()

#     # Aguarda os resultados carregarem
#     page.wait_for_selector('[data-testid="card-headline"]')

#     # Extrai e exibe os títulos
#     try:
#         headlines = page.get_by_test_id("card-headline").all()
#         for titulo in headlines[:5]:
#             print(titulo.text_content())
#     except Exception as e:
#         print(f"Erro ao extrair os títulos: {e}")

#     # Fecha o navegador
#     context.close()
#     browser.close()
