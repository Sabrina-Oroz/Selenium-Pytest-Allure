# Infraestructura reutilizable

""" Fixture que define los recursos reutilizables para los tests: abre el navegador y lo entrega al test """


from selenium import webdriver                                   # permite controlar el navegador
from selenium.webdriver.chrome.service import Service            # especifica dónde está ubicado el driver
from selenium.webdriver.chrome.options import Options            # configura chrome antes de iniciarlo
from webdriver_manager.chrome import ChromeDriverManager         # descarga el driver del navegador automáticamente
import os                                                        # módulo de python para interactuar con el os
from datetime import datetime                                    # módulo de python para obtener marcas de tiempo


def create_driver():
    chrome_options = Options()

    # Opciones generales antes de abrir chrome
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--blink-settings=imagesEnabled=false")

    # Control por variable de entorno
    headless = os.getenv("HEADLESS", "false").lower() == "true"

    if headless:
        # === FLAGS OBLIGATORIOS EN CI ===
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
    else:
        chrome_options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    return driver