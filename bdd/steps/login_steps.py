# Este archivo centraliza TODO el comportamiento de login_page

""" En los steps declaramos los escenarios del feature en bdd, lógica encapsulada, asserts y steps en allure, llamando a la clase Page y métodos de selenium.
 Los steps se reutilizan entre diversos escenarios. Los test_ contienen sólo la ruta de los escenarios en bdd y pytest parametrizado en regressiones"""


from pytest_bdd import given, when, then, parsers
from pages.login_page import LoginPage
import allure

## === ESCENARIO POSITIVO ===
# Scenario: Login exitoso con credenciales válidas

# DADO QUE
@given("el usuario navega a la página de login")
@allure.step("Abrir página de login")
def step_open_login(driver):
    LoginPage(driver).open()


# CUANDO
@when(parsers.parse('ingresa usuario "{username}" y password "{password}"'))
@allure.step("Ingresar credenciales")
def step_login(driver, username, password):
    LoginPage(driver).complete_credentials(username, password)


# Y
@when("hace click en el botón login")
@allure.step("Click en botón Login")
def step_click_login(driver):
    LoginPage(driver).login()


# ENTONCES
@then("debería acceder al área segura del sistema")
@allure.step("Inicio de sesión correctamente")
def step_verify_success(driver):                    # paso para verificar acceso
    message = LoginPage(driver).get_flash_message()
    assert "You logged into a secure area!" in message



## === ESCENARIO NEGATIVO CRÍTICO DE NEGOCIO ===
#  Scenario: Login fallido con password inválida

# ENTONCES
@then("debería ver un mensaje de error")
@allure.step("Inicio de sesion incorrecto")

def step_verify_error(driver):
    message = LoginPage(driver).get_flash_message()
    assert "Your password is invalid!" in message