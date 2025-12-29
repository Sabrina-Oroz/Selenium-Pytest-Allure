# Este archivo centraliza todo el comportamiento de combobox_page

""" En los steps declaramos los escenarios del feature en bdd, lógica encapsulada, asserts y steps en allure, llamando a la clase Page y métodos de selenium.
 Los steps se reutilizan entre diversos escenarios. Los test_ contienen sólo la ruta de los escenarios en bdd y pytest parametrizado en regressiones"""


from pytest_bdd import given, when, then, parsers
from pages.combobox_page import ComboBoxPage
import allure



@given("el usuario abre el formulario ComboBox")
@allure.step("Abrir formulario ComboBox")
def step_open_form(driver):
    ComboBoxPage(driver).open()


@when(parsers.parse('selecciona combo principal "{option}"'))
@allure.step("Seleccionar ComboBox principal")
def step_select_combo1(driver, option):
    ComboBoxPage(driver).select_combobox_1(option)


@when(parsers.parse('selecciona combos secundarios "{values}"'))
@allure.step("Seleccionar ComboBox secundario")
def step_select_combo2(driver, values):
    values_list = [v.strip() for v in values.split(",")]
    ComboBoxPage(driver).select_combobox_2_values(values_list)


@when(parsers.parse('selecciona sistema "{os_name}" y versión "{version}"'))
@allure.step("Seleccionar sistema y versión")
def step_select_os_version(driver, os_name, version):
    page = ComboBoxPage(driver)
    page.select_os(os_name)
    page.select_version(version)


@then("el formulario se envía correctamente")
@allure.step("Validar envío del formulario")
def step_validate_result(driver):
    message = ComboBoxPage(driver).get_result_message()

    assert message is not None
    assert "formulario" in message.lower()
