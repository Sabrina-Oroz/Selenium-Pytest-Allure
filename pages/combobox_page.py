"""El Page Object herada comportamientos de la clase BasePage. Realiza ACCIONES de negocio usando Selenium,
el test sólo envía los datos"""

from pages.base_page import BasePage                               # herencia BasePage
from selenium.webdriver.common.by import By                        # localiza los elementos
from selenium.webdriver.support.ui import Select                   # realiza selecciones
from selenium.webdriver.support import expected_conditions as EC   # condiciones que selenium evalúa
from selenium.common.exceptions import TimeoutException            # manejo controlado fallos esperables


## === Page Object del formulario ComboBox === definimos locators
class ComboBoxPage(BasePage):
    COMBOBOX_1 = (By.ID, "comboBox1")
    COMBOBOX_2 = (By.ID, "comboBox2")
    OS_SELECT = (By.ID, "os")
    VERSION_SELECT = (By.ID, "version")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-primary")
    RESULT_MESSAGE = (By.ID, "flashMessage")


## === Navegación === sincro inicial, abre la página
    def open(self):
        self.driver.get(
            "https://validaciones.rodrigovillanueva.com.mx/ComboBox_ok.html"
        )


## === ComboBox 1  === selección de un valor
    def select_combobox_1(self, option):
        select = Select(self.wait.until(EC.element_to_be_clickable(self.COMBOBOX_1)))
        select.select_by_visible_text(option)


## === ComboBox 2 (multi select) === selección más de un valor
    def select_combobox_2_values(self, values):
        # Esperamos que el <select> sea visible y lo envolvemos con Select
        select = Select(self.wait.until(EC.visibility_of_element_located(self.COMBOBOX_2)))

        # Validamos que realmente sea un multiselect
        if not select.is_multiple:
            raise AssertionError("El ComboBox 2 no es multiselect")

        # Validamos que values sea una lista o tupla
        if not isinstance(values, (list, tuple)):
            raise AssertionError("Los valores del ComboBox 2 deben ser una lista")

        # Limpiamos cualquier selección previa
        select.deselect_all()

        # Obtenemos los textos disponibles (para validación previa)
        available_options = [option.text for option in select.options]

        # Iteramos y seleccionamos
        for value in values:
            select.select_by_visible_text(value)


## === Sistema Operativo + Versión ===
    def select_os(self, os_name):
        select = Select(self.wait.until(EC.element_to_be_clickable(self.OS_SELECT)))
        select.select_by_visible_text(os_name)

    def select_version(self, version):
        select = Select(self.wait.until(EC.element_to_be_clickable(self.VERSION_SELECT)))

        # Obtenemos los textos disponibles e iteramos (validación previa por método dependiente)
        available_versions = [option.text for option in select.options]

        assert version in available_versions, (
            f"Versión '{version}' no disponible. "
            f"Disponibles: {available_versions}"
        )

        select.select_by_visible_text(version)


## === Enviar formulario ===
    def submit(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()


## === Obtener mensaje de confirmación (para assertions en el test) ===
    def get_result_message(self):
        try:
            return self.wait.until(
            EC.visibility_of_element_located(self.RESULT_MESSAGE)
        ).text
        except TimeoutException:
            return None