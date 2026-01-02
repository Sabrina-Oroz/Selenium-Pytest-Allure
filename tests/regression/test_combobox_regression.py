# Ese archivo solo registra escenarios (BDD PURO), los datos se encuentran en los steps

from pathlib import Path                # Reemplazo de ruta por paths relativos. Fumciona en todos los OS
import allure
from pytest_bdd import scenario

FEATURES_DIR = Path(__file__).resolve().parents[2] / "bdd" / "features"

@allure.feature("Formulario de registro ComboBox 1")
@allure.story("US xxx - Formulario de registro ComboBox 1")
@allure.title("El usuario puede resgistrarse con combinaciones válidas correctamente")
@allure.severity(allure.severity_level.NORMAL)
@scenario(FEATURES_DIR / "combobox.feature",
          "ComboBox - Enviar formulario con combinaciones válidas")
def test_combobox_regression():
    pass
