import allure                                 # reportes + evidencias (sólo en fallos) + labels
import pytest                                 # framework de ejecución automation
from pages.textbox_page import TextBoxPage    # importamos en el test textbox_page junto con su clase


## === Configuración de labels en allure ===
@allure.feature("Formulario TexBox")                                # módulo funcional o feature del sistema
@allure.story("Enviar formulario TextBox")                          # caso de uso, flujo o HDU dentro de una feature
@allure.severity(allure.severity_level.CRITICAL)                    # impacto del fallo
@allure.tag("smoke", "ui")                                    # análisis - libres para clasificar tests
@allure.title("CP - Enviar formulario con selecciones válidas")     # legibilidad - nombre del test en el reporte

# descripción funcional - validación del test
@allure.description("""                                              
El usuario completa:
- Nombre completo
- Email
- Dirección concurrente
_ Dirección permantente
Y envía el formulario correctamente.
""")


## === Declaramos la función test_ con los métodos y atributos de la clase TextBoxPage, junto con los inputs ===
@pytest.mark.smoke
def test_textbox_page(driver):
    page = TextBoxPage(driver)

    with allure.step("Abrir Formulario de registro"):
        page.open()

    with allure.step(f"Completar formulario"):
        page.fill_form(
            "Sabrina Oroz",
            "ejemplo@gmail.com",
            "Dirección 1",
            "Dirección 2"
    )
    with allure.step("Enviar formulario"):
        page.submit_form()

    with allure.step("Verificar devolución del texto"):
        getoutput = page.get_output()
        assert "Sabrina Oroz" in getoutput

        assert getoutput is not None, "No se pudo enviar el texto"

