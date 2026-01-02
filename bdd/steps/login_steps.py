# Este archivo centraliza TODO el comportamiento de login_page

""" En los steps declaramos los escenarios del feature en bdd, lógica encapsulada, steps en allure y asserts, llamando a la clase Page y métodos de selenium.
 Los steps se reutilizan entre diversos escenarios. Los test_ contienen la severidad y la ruta de los escenarios en bdd y pytest parametrizado en regressiones"""


from pytest_bdd import given, when, then, parsers
from pages.login_page import LoginPage
import allure
from core.assertions import assert_with_screenshot   # assert reutilizable en core que adjunta screenshot en el momento exacto en caso de fallo

## === ESCENARIO POSITIVO ===
# Scenario: Login exitoso con credenciales válidas

# DADO QUE
@given("el usuario navega a la página de login")
@allure.step("Abrir página de login")
def step_open_login(driver):
    LoginPage(driver).open()


# CUANDO
@when(parsers.parse('ingresa usuario "{username}" y password "{password}"'))
@allure.step("Ingresar credenciales de usuario")
def step_login(driver, username, password):
    LoginPage(driver).complete_credentials(username, password)


# Y
@when("hace click en el botón login")
@allure.step("Enviar formulario de login")
def step_click_login(driver):
    LoginPage(driver).login()


# ENTONCES  == Validación positiva
@then("debería acceder al área segura del sistema")
@allure.step("Validar acceso al área segura del sistema")
def step_verify_success(driver):
    message = LoginPage(driver).get_flash_message()

    assert_with_screenshot(                                         # assert crítico reutilizable
        condition="You logged into a secure area!" in message,
        driver=driver,
        message="El usuario no accedió al área segura del sistema",
        step_name="Login exitoso con credenciales válidas – fallo en acceso al área segura"
    )


## === ESCENARIOS NEGATIVOS CRÍTICOS DE NEGOCIO ===

# Scenario: Login fallido con usuario inválido
@then("debería ver un mensaje de error por usuario inválido")
@allure.step("Validar mensaje de error por usuario inválido")
def step_verify_invalid_user(driver):
    message = LoginPage(driver).get_flash_message()
    assert "Your username is invalid!" in message


#  Scenario: Login fallido con password inválida
@then("debería ver un mensaje de error por credenciales inválidas")
@allure.step("Validar mensaje de error por credenciales inválidas")
def step_verify_invalid_credentials(driver):
    message = LoginPage(driver).get_flash_message()
    assert "Your password is invalid!" in message


#Scenario: Login fallido sin password
@then("debería ver un mensaje de error por password requerida")
@allure.step("Validar mensaje de error por password requerida")
def step_verify_empty_password(driver):
    message = LoginPage(driver).get_flash_message()

    assert_with_screenshot(
        condition="Password is required" in message or "invalid$$$$$$$$$" in message, #FALLO INTENCIONAL
        driver=driver,
        message="No se mostró el mensaje esperado para password vacía",
        step_name="Validación por password requerida"
    )