""" El Page Object herada comportamientos de la clase BasePage. Realiza acciones de negocio encapsulando Selenium,
Los tests y steps solo orquestan datos y validaciones. """

# Este Page Object sirve tanto para BDD como para pytest clásico

from core.base_page import BasePage                     # define cómo interactuar
from selenium.webdriver.common.by import By             # define qué buscar


class LoginPage(BasePage):

    URL = "https://the-internet.herokuapp.com/login"

    # == LOCATORS ==
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.ID, "flash")

    # == NAVEGACIÓN ==
    def open(self):
        self.driver.get(self.URL)

    # == COMPLETAR CREDENCIALES ==
    def complete_credentials(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)

    # == LOGIN ==
    def login(self):
        self.click(self.LOGIN_BUTTON)

    # == VALIDACIÓN ==
    def get_flash_message(self):                    # definimos un sólo punto de lectura, el mensaje puede cambiar,
        return self.get_text(self.FLASH_MESSAGE)    #  pero el elemento no