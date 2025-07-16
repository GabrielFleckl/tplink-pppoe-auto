import os
import time
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import (
    StaleElementReferenceException,
    TimeoutException,
    WebDriverException
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def validar_argumento(value):
    value = str(value).strip()
    if not value:
        raise argparse.ArgumentTypeError("Este campo não pode estar vazio.")
    return value


def configurar_driver():
    print("LOG: Iniciando automação...")
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--log-level=3")
    options.add_argument("--silent")
    options.add_argument("--user-data-dir=/tmp/chrome-profile")  

    return webdriver.Chrome(options=options)


def realizar_login(nav, wait, url, senha):
    if not url.startswith("http"):
        print("LOG: ❌ A URL deve começar com 'http://' ou 'https://'.")
        exit(1)

    try:
        nav.get(url)
    except WebDriverException:
        print("LOG: ❌ Erro ao acessar a URL do roteador.")
        nav.quit()
        exit(1)

    try:
        print("LOG: Entrou na tela de login: " + url)
        login_input = wait.until(EC.visibility_of_element_located((By.ID, "pc-login-password")))
        nav.execute_script("arguments[0].scrollIntoView(true);", login_input)
        print("LOG: Preencheu a senha do roteador")
        login_input.send_keys(senha)

        login_button = wait.until(EC.element_to_be_clickable((By.ID, "pc-login-btn")))
        nav.execute_script("arguments[0].scrollIntoView(true);", login_button)
        login_button.click()
        print("LOG: Clicou no botão de login")

        try:
            confirm_btn = WebDriverWait(nav, 5).until(EC.presence_of_element_located((By.ID, "confirm-yes")))
            nav.execute_script("arguments[0].click();", confirm_btn)
            print("LOG: Clicou no botão para confirmar o login")
        except:
            pass  

        advanced_button = wait.until(EC.element_to_be_clickable((By.ID, "advanced")))
        nav.execute_script("arguments[0].click();", advanced_button)
        print("LOG: Clicou no advanced")

    except TimeoutException:
        print("LOG: ❌ Erro de login. Verifique a senha ou a interface do roteador.")
        nav.quit()
        exit(1)


def navegar_para_pppoe(nav, wait):
    for attempt in range(3):
        try:
            time.sleep(1.5)
            network_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[2]/a')))
            nav.execute_script("arguments[0].click();", network_button)
            print("LOG: Clicou no network")
            break
        except StaleElementReferenceException:
            print("LOG: Elemento obsoleto. Tentando novamente...")
        except TimeoutException:
            print("LOG: Elemento 'Network' não apareceu a tempo.")
            return False

    gpon_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[2]/ul/li[1]/a/span')))
    nav.execute_script("arguments[0].click();", gpon_button)
    print("LOG: Clicou no GPON WAN dentro da barra lateral")

    pppoe_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="wanBody"]/tr[3]/td[7]/span[1]')))
    nav.execute_script("arguments[0].click();", pppoe_button)
    print("LOG: Clicou na interface PPPoE para modificar")

    return True


def alterar_pppoe_login(nav, wait, pppoe_login):
    login_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="username"]')))
    nav.execute_script("arguments[0].scrollIntoView(true);", login_input)
    login_input.clear()
    login_input.send_keys(pppoe_login)
    print("LOG: Preencheu o login PPPoE com: " + pppoe_login)

    save_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="saveConnBtn"]')))
    nav.execute_script("arguments[0].scrollIntoView(true);", save_button)
    nav.execute_script("arguments[0].click();", save_button)
    print("LOG: Clicou no botão para salvar")


# -------------------------
# Execução principal
# -------------------------

parser = argparse.ArgumentParser()
parser.add_argument("--url", required=True, type=validar_argumento, help="URL do roteador")
parser.add_argument("--senha", required=True, type=validar_argumento, help="Senha do roteador")
parser.add_argument("--pppoe", required=True, type=validar_argumento, help="Login PPPoE")
args = parser.parse_args()

URL_ROTEADOR = args.url
SENHA_ROTEADOR = args.senha
LOGIN_PPPOE = args.pppoe

nav = configurar_driver()
wait = WebDriverWait(nav, 15)

realizar_login(nav, wait, URL_ROTEADOR, SENHA_ROTEADOR)

if navegar_para_pppoe(nav, wait):
    alterar_pppoe_login(nav, wait, LOGIN_PPPOE)
    print("LOG: ✅ PPPoE trocado com sucesso!")
else:
    print("LOG: ❌ Falha ao acessar a área de configuração PPPoE.")

nav.quit()
