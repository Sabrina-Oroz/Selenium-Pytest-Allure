import allure                                 # reportes + evidencias (sólo en fallos) + labels
import pytest                                 # framework de ejecución automation
from pages.combobox_page import ComboBoxPage  # importamos en el test combobox_pages junto con su clase


## === Configuración de labels en allure ===
@allure.feature("Formulario ComboBox")                               # módulo funcional o feature del sistema
@allure.story("Enviar formulario ComboBox")                          # caso de uso, flujo o HDU dentro de una feature
@allure.severity(allure.severity_level.CRITICAL)                     # impacto del fallo
@allure.tag("smoke", "ui")                                     # análisis - libres para clasificar tests
@allure.title("CP - Enviar formulario con selecciones válidas")      # legibilidad - nombre del test en el reporte

# descripción funcional - validación del test
@allure.description("""                                              
El usuario completa:
- ComboBox simple
- ComboBox múltiple
- Sistema operativo y versión
Y envía el formulario correctamente.
""")


## === Declaramos los métodos y atributos de la clase ComboBox, junto con los valores y parametrizamos ===
@pytest.mark.smoke
@pytest.mark.parametrize(
"combo1, combo2_values, os_name, version",
    [
        ("Valor 2", ["Valor 1", "Valor 3", "Valor 4"], "Windows", "Windows 11"),
        ("Valor 1", ["Valor 2"], "Linux", "Ubuntu"),
        ("Valor 3", ["Valor 1"], "Mac", "macOS Big Sur"),
    ],
    ids=[
         "Windows - selección múltiple completa",
         "Linux - selección simple",
         "Mac - selección básica",
    ]
)

## === Declaramos la función test_ con los métodos y atributos de la clase ComboBoxPage,
#      junto con los valores parametrizados con diferentes escenarios y descripción del paso a paso en allure ===
def test_combobox_flow(driver, combo1, combo2_values, os_name, version):
    page = ComboBoxPage(driver)

    with allure.step("Abrir formulario"):
        page.open()

    with allure.step(f"Seleccionar ComboBox 1: {combo1}"):
        page.select_combobox_1(combo1)

    with allure.step(f"Seleccionar ComboBox 2: {combo2_values}"):
        page.select_combobox_2_values(combo2_values)

    with allure.step(f"Seleccionar Sistema Operativo: {os_name}"):
        page.select_os(os_name)

    with allure.step(f"Seleccionar versión: {version}"):
        page.select_version(version)

    with allure.step("Enviar formulario"):
        page.submit()

    with allure.step("Validar mensaje de confirmación"):
        message = page.get_result_message()
        assert message is not None, "No se mostró mensaje de confirmación"

