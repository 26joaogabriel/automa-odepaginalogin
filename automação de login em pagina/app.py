from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto('https://portalhashtag.com/login')
    pagina.locator('xpath=//*[@id="email-login"]').click()
    pagina.fill('xpath=//*[@id="email-login"]',"joaosilva2023@gmail.com")
    time.sleep(10)
