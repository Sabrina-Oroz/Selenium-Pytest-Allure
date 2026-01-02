# Ese archivo solo registra escenarios (BDD PURO), los datos se encuentran en los steps

from pathlib import Path                # Reemplazo de ruta por paths relativos. Fumciona en todos los OS
import allure
from pytest_bdd import scenario

FEATURES_DIR = Path(__file__).resolve().parents[2] / "bdd" / "features"

@allure.feature("Formulario de registro ComboBox 1")
@allure.story("US xxx - Formulario de registro ComboBox 1")
@allure.title("El usuario puede registrarse correctamente")
@allure.severity(allure.severity_level.CRITICAL)
@scenario(FEATURES_DIR / "combobox.feature",
          "ComboBox - Enviar formulario ComboBox (happy path)")
def test_combobox_smoke_1():
    pass

