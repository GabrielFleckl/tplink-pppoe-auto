import os
import time
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Verifica se o argumento é vazio
def non_empty_string(value):
    value = str(value).strip()
    if not value:
        raise argparse.ArgumentTypeError("Este campo não pode estar vazio.")
    return value


parser = argparse.ArgumentParser()
parser.add_argument(
    "--url", required=True, type=non_empty_string, help="URL do roteador"
)
parser.add_argument(
    "--senha", required=True, type=non_empty_string, help="Senha do Roteador"
)
parser.add_argument("--pppoe", required=True, type=non_empty_string, help="Login PPPoE")

args = parser.parse_args()

# Constantes
URL_ROTEADOR = args.url
SENHA_ROTEADOR = args.senha
LOGIN_PPPOE = args.pppoe

options = Options()
# Comentar option abaixo para deixar o Chrome aparecendo
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--log-level=3")
options.add_argument("--silent")

service = Service(ChromeDriverManager().install(), log_path=os.devnull)

# Abre o navegador
nav = webdriver.Chrome(
    service=service,
    options=options,
)

wait = WebDriverWait(nav, 10)

nav.get(URL_ROTEADOR)

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
    EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[2]/ul/li[1]/a/span'))
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

print("PPPoE Trocado com sucesso!")
