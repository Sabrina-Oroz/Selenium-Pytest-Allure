""" El Page Object herada comportamientos de la clase BasePage. Realiza acciones de negocio encapsulando Selenium,
Los tests y steps solo orquestan datos y validaciones. """

from core.base_page import BasePage                                # herencia BasePage
from selenium.webdriver.common.by import By                        # localiza los elementos
from selenium.webdriver.support.ui import WebDriverWait, Select    # manejo de espera explícita
from selenium.webdriver.support import expected_conditions as EC   # condiciones que Selenium evalúa
from selenium.common.exceptions import TimeoutException            # manejo controlado fallos esperables


## === Page Object del formulario TextBox ===
class TextBoxPage(BasePage):

    URL = "https://demoqa.com/text-box"

    # == LOCATORS ==
    TITLE = (By.CSS_SELECTOR, "h1")
    USER_NAME = (By.ID, "userName")
    USER_EMAIL = (By.ID, "userEmail")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    PERMANENT_ADDRESS = (By.ID, "permanentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")
    OUTPUT = (By.ID, "output")


    ## == NAVEGACIÓN == abre la página y espera visibilidad del título
    def open(self):
        self.driver.get(self.URL)
        self.wait.until(EC.visibility_of_element_located(self.TITLE))

    ## == ACCIONES DE NEGOCIO == completar formulario
    def fill_form(self, name, email, current, permanent):
        self.type(self.USER_NAME, name)
        self.type(self.USER_EMAIL, email)
        self.type(self.CURRENT_ADDRESS, current)
        self.type(self.PERMANENT_ADDRESS, permanent)

    ## == ENVÍO DEL FORMULARIO == scroll + click
    def submit_form(self):
        self.scroll_into_view(self.SUBMIT_BUTTON)
        self.click(self.SUBMIT_BUTTON)

    ## === RETORNO DE INPUTS ===
    def get_flash_message(self):                    # definimos un sólo punto de lectura, el mensaje puede cambiar,
        return self.get_text(self.OUTPUT)           #  pero el elemento no
