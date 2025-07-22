
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging

def configurar_driver():
    logging.info("Iniciando automação...")
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
