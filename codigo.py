"""
Passo 1 - Entrar no sistema da empresa
    Link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
Passo 2 - Fazer Login
Passo 3 - Pegar/Importar a base de dados
Passo 4 - Cadastrar um produto
Passo 5 - Repetir o passo 4 até cadastrar todos os produtos

"""

import pyautogui
import time

# pyautogui.click - clicar com o mouse
# pyautogui.write - escrever um texto
# pyautogui.press - apertar 1 tecla
# pyautogui.hotkey - combinação de teclas (Ctrl C)
# pyautogui.scroll - rolar a tela  para cima ou para baico

pyautogui.PAUSE = 0.9

# Passo 1 - Entrar no sistema da empresa
# Abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)

pyautogui.hotkey("win", "up")  # Atalho para maximizar a janela no Windows
# entrar no Link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.click(x=664, y=83)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")



#Passo 2 - Fazer Login
pyautogui.click(x=713, y=466)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("teste@email.com")

pyautogui.press("tab")
pyautogui.write("senhaqualquer")

pyautogui.click(x=947, y=669)

time.sleep(3)

# Passo 3 - Pegar/Importar a base de dados

import pandas

table_products = pandas.read_csv("produtos.csv")

print(table_products)

# Passo 4 - Cadastrar um produto
for linha in table_products.index:   #index é o número da linha
    
    #código
    pyautogui.click(x=730, y=323)
    codigo = str(table_products.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    
    #marca
    marca = str(table_products.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    
    #tipo
    tipo = str(table_products.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    
    #categoria
    categoria = str(table_products.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    
    #preco
    preco = str(table_products.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    
    #custo
    custo = str(table_products.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    
    #obs
    obs = str(table_products.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
        
        
    #clickar botao enviar
    pyautogui.press("tab")  
    pyautogui.press("enter")

    pyautogui.scroll(3000)

# Passo 5 - Repetir o passo 4 até cadastrar todos os produtos

