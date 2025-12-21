"""El Page Object herada comportamientos de la clase BasePage. Realiza ACCIONES de negocio usando Selenium,
el test sólo envía los datos"""

from pages.base_page import BasePage                               # herencia BasePage
from selenium.webdriver.common.by import By                        # localiza los elementos
from selenium.webdriver.support.ui import WebDriverWait, Select    # manejo de espera explícita
from selenium.webdriver.support import expected_conditions as EC   # condiciones que Selenium evalúa
from selenium.common.exceptions import TimeoutException            # manejo controlado fallos esperables


## === Page Object del formulario TextBox === definimos locators
class TextBoxPage(BasePage):
    TITLE = (By.CSS_SELECTOR, "h1")
    USER_NAME = (By.ID, "userName")
    USER_EMAIL = (By.ID, "userEmail")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    PERMANENT_ADDRESS = (By.ID, "permanentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")
    OUTPUT = (By.ID, "output")


    ## === Navegación === sincro inicial, abre la página y espera visibilidad del título
    def open(self):
        self.driver.get("https://demoqa.com/text-box")
        self.wait.until(EC.visibility_of_element_located(self.TITLE))

    ## === Acciones de negocio === completar y enviar formulario
    def fill_form(self, name, email, current, permanent):
        self.type(self.USER_NAME, name)
        self.type(self.USER_EMAIL, email)
        self.type(self.CURRENT_ADDRESS, current)
        self.type(self.PERMANENT_ADDRESS, permanent)

    ## === Envío del formulario === scroll + click
    def submit_form(self):
        self.scroll_into_view(self.SUBMIT_BUTTON)
        self.click(self.SUBMIT_BUTTON)

    ## === Retorno de inputs ===
    def get_output(self):
        return self.get_text(self.OUTPUT)
