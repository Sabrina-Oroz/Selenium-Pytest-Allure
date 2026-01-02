# Ese archivo solo registra escenarios (BDD PURO), los datos se encuentran en los features

from pathlib import Path                # Reemplazo de ruta por paths relativos. Fumciona en todos los OS
import allure
from pytest_bdd import scenario

FEATURES_DIR = Path(__file__).resolve().parents[2] / "bdd" / "features"

@allure.feature("Formulario TextBox - Registro de usuario")
@allure.story("US xxx - Formulario TextBox - Registro de usuario")
@allure.title("El usuario puede registrarse correctamente")
@allure.severity(allure.severity_level.CRITICAL)
@scenario(FEATURES_DIR / "textbox.feature",
          "Registro exitoso")
def test_textbox_smoke_1():
    pass