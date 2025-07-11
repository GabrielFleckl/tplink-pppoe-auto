from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import time

from selenium.webdriver.support.ui import WebDriverWait

# Descomentar caso queira que rode em segundo plano (sem o navegador aparecer)
# from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--url")
parser.add_argument("--senha")
parser.add_argument("--pppoe")

args = parser.parse_args()

arg_url = args.url
arg_senha = args.senha
arg_pppoe = args.pppoe

# Se não for passado nenhum arg ira usar o valor padrão da direita
URL_ROTEADOR = arg_url or "http://192.168.2.254"
SENHA_ROTEADOR = arg_senha or "gigaweb@cliente"
LOGIN_PPPOE = arg_pppoe or "teste4"


# Descomentar caso queira que rode em segundo plano (sem o navegador aparecer)
# options = Options()
# options.add_argument("--headless=new")
# options.add_argument("--window-size=1920,1080")

# Abri o navegador
nav = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Descomentar e excluir a linha de cima caso queira que rode em segundo plano
# nav = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

wait = WebDriverWait(nav, 10)

nav.get(URL_ROTEADOR)

nav.maximize_window()

login_input = wait.until(EC.presence_of_element_located((By.ID, "pc-login-password")))
login_input.send_keys(SENHA_ROTEADOR)

login_button = wait.until(EC.presence_of_element_located((By.ID, "pc-login-btn")))
login_button.click()


# Verifica e aperta para logar mesmo assim se alguém estiver já logado no roteador
try:
    login_confirm_button = WebDriverWait(nav, 5).until(
        EC.presence_of_element_located((By.ID, "confirm-yes"))
    )
    login_confirm_button.click()
except:
    pass

advanced_button = wait.until(EC.presence_of_element_located((By.ID, "advanced")))
advanced_button.click()

for attempt in range(3):
    try:
        network_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[2]/a'))
        )
        network_button.click()
        break  # Se clicou com sucesso, sai do loop
    except StaleElementReferenceException:
        print("Elemento ficou obsoleto. Tentando novamente...")
        time.sleep(1)
    except TimeoutException:
        print("Elemento não apareceu a tempo.")
        break

gpon_button = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@id="menuTree"]/li[2]/ul/li[1]/a/span')
    )
)
gpon_button.click()

pppoe_modify_button = wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="wanBody"]/tr[3]/td[7]/span[1]'))
)
pppoe_modify_button.click()

login_pppoe_input = wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))
)
login_pppoe_input.clear()
login_pppoe_input.send_keys(LOGIN_PPPOE)

save_pppoe_button = wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="saveConnBtn"]'))
)

ActionChains(nav).move_to_element(save_pppoe_button).perform()

save_pppoe_button.click()

nav.quit()
