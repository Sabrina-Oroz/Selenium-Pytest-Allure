"""Con BasePage generamos herencia (clase padre para el resto de las page), es el corazón del POM.
Centralizamos lógica selenium: acceso al driver, waits, clicks, send_keys, scroll."""


from selenium.webdriver.support.ui import WebDriverWait                # manejo de esperas explícitas
from selenium.webdriver.support import expected_conditions as EC       # condiciones que selenium evalúa

class BasePage:
    def __init__(self, driver, timeout=10):                           # el constructor guarda el driver, centraliza los
        self.driver = driver                                          # waits y deja lista la página para selenium
        self.wait = WebDriverWait(driver, timeout)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    ## === Para inputs === limpia antes
    def type(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    ## === Validaciones para tests ==== obtiene texto visible
    def get_text(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text

    ## === Desplazamiento a la vista ===
    def scroll_into_view(self, locator):
        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", element
        )