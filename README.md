automação ultilizando a biblioteca playwright 
navegador = p.chromium.launch(headless=False) #chamando a função 
    pagina = navegador.new_page() #entrando no navegador
    pagina.goto('https://portalhashtag.com/login') #entrando na pagina
    pagina.locator('xpath=//*[@id="email-login"]').click() #especificando que quero clicar na area de login
    pagina.fill('xpath=//*[@id="email-login"]',"joaosilva2023@gmail.com") #inserindo login 
    time.sleep(10) #tempo em que o site ficara aberto 
    
