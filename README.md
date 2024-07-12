# Automação de Entrada de Dados com PyAutoGUI

Este projeto automatiza a entrada de dados em um sistema usando a biblioteca `pyautogui`.

## Passos da Automação

1. **Entrar no sistema da empresa**
    - Link: https://dlp.hashtagtreinamentos.com/python/intensivao/login

2. **Fazer Login**
    - Insira as credenciais de login.

3. **Pegar/Importar a base de dados**
    - Importar a base de dados dos produtos a partir de um arquivo CSV.

4. **Cadastrar um produto**
    - Inserir os dados do produto no sistema.

5. **Repetir o cadastro**
    - Repetir o passo 4 até cadastrar todos os produtos.

## Como Usar

1. **Configurar o ambiente**
    - Certifique-se de ter o Python instalado.
    - Instale as dependências necessárias: `pandas` e `pyautogui`.

    ```bash
    pip install pandas pyautogui
    ```

2. **Executar o Script**
    - Abra o script Python (`automacao.py`).
    - Certifique-se de que o arquivo `produtos.csv` está no mesmo diretório que o script.
    - Execute o script.

    ```bash
    python automacao.py
    ```

## Exemplo de Código

```python
import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.9

# Passo 1 - Entrar no sistema da empresa
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)
pyautogui.hotkey("win", "up")
pyautogui.click(x=664, y=83)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Passo 2 - Fazer Login
pyautogui.click(x=713, y=466)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("teste@email.com")
pyautogui.press("tab")
pyautogui.write("senhaqualquer")
pyautogui.click(x=947, y=669)
time.sleep(3)

# Passo 3 - Pegar/Importar a base de dados
table_products = pandas.read_csv("produtos.csv")

# Passo 4 - Cadastrar um produto
for linha in table_products.index:
    pyautogui.click(x=730, y=323)
    codigo = str(table_products.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = str(table_products.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = str(table_products.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(table_products.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco = str(table_products.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    custo = str(table_products.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(table_products.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(3000)