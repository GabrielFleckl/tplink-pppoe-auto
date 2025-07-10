from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait

# Descomentar caso queira que rode em segundo plano (sem o navegador aparecer)
# from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

URL_ROTEADOR = "http://192.168.2.254"
SENHA_ROTEADOR = "gigaweb@cliente"
LOGIN_PPPOE = "12113gabriel"

# var = input("URL do roteador:")

# 12113gabriel

# Rodar em segundo plano
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
login_confirm_button = wait.until(
    EC.presence_of_element_located((By.ID, "confirm-yes"))
)
if login_confirm_button:
    login_confirm_button.click()

advanced_button = wait.until(EC.presence_of_element_located((By.ID, "advanced")))
advanced_button.click()

network_button = wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="menuTree"]/li[2]/a'))
)
network_button.click()

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


