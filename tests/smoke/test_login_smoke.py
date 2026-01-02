# Ese archivo solo registra escenarios (BDD PURO) y labels de allure, los datos se encuentran en los features

from pathlib import Path                # Reemplazo de ruta por paths relativos. Fumciona en todos los OS
import allure
from pytest_bdd import scenario

FEATURES_DIR = Path(__file__).resolve().parents[2] / "bdd" / "features"

## Léase feature como épica/módulo - title como escenario
@allure.feature("Autenticación")
@allure.story("US xxx - Login de usuario")
@allure.title("Login exitoso con credenciales válidas")
@allure.description(
    "Verifica que un usuario con credenciales válidas pueda acceder correctamente "
    "al área segura del sistema. Este escenario valida el flujo crítico de autenticación."
)
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("critical_assert")
@scenario(FEATURES_DIR / "login.feature",
          "Login exitoso con credenciales válidas")
def test_login_smoke_1():
    pass


@allure.feature("Autenticación")
@allure.story("US xxx - Login de usuario")
@allure.title("Login fallido con usuario inválido")
@allure.description(
    "Valida que el sistema rechace el acceso cuando el nombre de usuario no existe "
    "y muestre un mensaje de error apropiado."
)
@allure.severity(allure.severity_level.CRITICAL)
@scenario(FEATURES_DIR / "login.feature",
          "Login fallido con usuario inválido")
def test_login_smoke_2():
    pass


@allure.feature("Autenticación")
@allure.story("US xxx - Login de usuario")
@allure.title("Login fallido con password inválida")
@allure.description(
    "Verifica que el sistema impida el inicio de sesión cuando la contraseña es incorrecta, "
    "asegurando el control de acceso."
)
@allure.severity(allure.severity_level.CRITICAL)
@scenario(FEATURES_DIR / "login.feature",
          "Login fallido con password inválida")
def test_login_smoke_3():
    pass


@allure.feature("Autenticación")
@allure.story("US xxx - Login de usuario")
@allure.title("Login fallido sin password")
@allure.description(
    "Valida que el sistema no permita iniciar sesión sin una contraseña ingresada "
    "y notifique correctamente el error al usuario."
)
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("critical_assert")
@scenario(FEATURES_DIR / "login.feature",
          "Login fallido sin password")
def test_login_smoke_4():
    pass

