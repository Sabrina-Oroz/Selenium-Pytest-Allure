# Este archivo centraliza TODO el comportamiento de textbox_page

""" En los steps declaramos los escenarios del feature en bdd, lógica encapsulada, asserts y steps en allure, llamando a la clase Page y métodos de selenium.
 Los steps se reutilizan entre diversos escenarios. Los test_ contienen sólo la ruta de los escenarios en bdd y pytest parametrizado en regressiones"""


from pytest_bdd import given, when, then, parsers
from pages.textbox_page import TextBoxPage
import allure


# DADO QUE
@given("el usuario navega a la página de registro")
@allure.step("Abrir página de registro")
def step_open_registro(driver):
    TextBoxPage(driver).open()

# CUANDO
@when(parsers.parse(
        'ingresa nombre "{name}", email "{email}", '
        'dirección actual "{current}", dirección permanente "{permanent}"'))
@allure.step("Completar formulario de registro")
def step_completar_registro(driver, name, email, current, permanent):
    TextBoxPage(driver).fill_form(name, email, current, permanent)

# Y
@when("envía el formulario")
@allure.step("Enviar formulario")
def step_enviar_formulario(driver):
    TextBoxPage(driver).submit_form()

# ENTONCES
@then("debería ver sus datos reflejados en el resultado")
@allure.step("Validar resultado de envío del formulario")

def step_verificar_resultado(driver):
    page = TextBoxPage(driver)
    output = page.get_flash_message()

    assert "Sabrina Oroz" in output
    assert output is not None, "No se mostró ningún resultado"
