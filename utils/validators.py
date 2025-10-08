import time
import logging
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver import configurar_driver
import argparse

def validar_argumento(value):
    value = str(value).strip()
    if not value:
        raise argparse.ArgumentTypeError("Este campo não pode estar vazio.")
    return value


def valida_modelo(url):
    nav = configurar_driver()
    wait = WebDriverWait(nav, 15)
    nav.get(url)
    model = wait.until(EC.visibility_of_element_located((By.ID, "pc-bot-productName")))
    logging.info(f"Modelo identificado: {model.text}")
