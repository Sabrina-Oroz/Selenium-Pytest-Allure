# Infraestructura reutilizable

""" Fixture que define los recursos reutilizables para los tests: abre el navegador y lo entrega al test """


from selenium import webdriver                                   # permite controlar el navegador
from selenium.webdriver.chrome.options import Options            # configura chrome antes de iniciarlo
from webdriver_manager.chrome import ChromeDriverManager         # descarga el driver del navegador automáticamente
import os                                                        # módulo de python para interactuar con el os



def create_driver():
    chrome_options = Options()

    # Opciones base previo al abrir el navegador
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--blink-settings=imagesEnabled=false")

    headless = os.getenv("HEADLESS", "false").lower() == "true"

    if headless:
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
    else:
        chrome_options.add_argument("--start-maximized")

    #  Selenium Manager (NO webdriver-manager)
    driver = webdriver.Chrome(options=chrome_options)
    return driver