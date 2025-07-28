import time
import logging
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver import configurar_driver


def executar_tp_link_xx530(url, senha, pppoe_login):
    nav = configurar_driver()
    wait = WebDriverWait(nav, 15)

    formatted_url = f"http://{url}/"

    def realizar_login():
        if url.startswith("http"):
            logging.error("❌ A URL deve conter apenas o IP do roteador.")
            nav.quit()
            return False
        try:
            # http://192.168.2.254/
            nav.get(formatted_url)
        except WebDriverException:
            logging.error("❌ Erro ao acessar a URL do roteador.")
            nav.quit()
            return False
        try:
            logging.info("Entrou na tela de login: " + formatted_url)
            login_input = wait.until(EC.visibility_of_element_located((By.ID, "pc-login-password")))
            nav.execute_script("arguments[0].scrollIntoView(true);", login_input)
            login_input.send_keys(senha)
            login_button = wait.until(EC.element_to_be_clickable((By.ID, "pc-login-btn")))
            nav.execute_script("arguments[0].scrollIntoView(true);", login_button)
            login_button.click()
            try:
                confirm_btn = WebDriverWait(nav, 5).until(EC.presence_of_element_located((By.ID, "confirm-yes")))
                nav.execute_script("arguments[0].click();", confirm_btn)
            except:
                pass
            advanced_button = wait.until(EC.element_to_be_clickable((By.ID, "advanced")))
            nav.execute_script("arguments[0].click();", advanced_button)
            return True
        except TimeoutException:
            logging.error("❌ Erro ao fazer login.")
            nav.quit()
            return False

    def navegar_para_pppoe():
        for _ in range(3):
            try:
                time.sleep(1.5)
                network_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[2]/a')))
                nav.execute_script("arguments[0].click();", network_button)
                break
            except (StaleElementReferenceException, TimeoutException):
                continue
        gpon_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[2]/ul/li[1]/a/span')))
        nav.execute_script("arguments[0].click();", gpon_button)
        wait.until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, "#wanBody > tr:not(#editContainer)")))
        linhas = nav.find_elements(By.CSS_SELECTOR, "#wanBody > tr:not(#editContainer)")
        for linha in linhas:
            colunas = linha.find_elements(By.TAG_NAME, "td")
            if len(colunas) >= 2 and colunas[1].text.strip().lower() == "internet":
                try:
                    botao_editar = colunas[6].find_element(By.CLASS_NAME, "edit-modify-icon")
                    nav.execute_script("arguments[0].click();", botao_editar)
                    return True
                except Exception as e:
                    logging.error(f"❌ Erro ao clicar em editar: {e}")
                    return False
        return False

    def alterar_pppoe():
        login_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="username"]')))
        nav.execute_script("arguments[0].scrollIntoView(true);", login_input)
        login_input.clear()
        login_input.send_keys(pppoe_login)
        save_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="saveConnBtn"]')))
        nav.execute_script("arguments[0].scrollIntoView(true);", save_button)
        nav.execute_script("arguments[0].click();", save_button)

        try:
            WebDriverWait(nav, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="divPage"]/div[15]/div[2]/div/form/div/span[@class="load"]')
                )
            )
            logging.info("Botão para salver PPPoE pressionado")
        except TimeoutException:
            logging.warning("⚠️ O spinner não apareceu a tempo.")

    try:
        if realizar_login() and navegar_para_pppoe():
            alterar_pppoe()
            logging.info("✅ PPPoE alterado com sucesso!")
        else:
            logging.error("❌ Falha no processo de alteração de PPPoE.")
    finally:
        nav.quit()
