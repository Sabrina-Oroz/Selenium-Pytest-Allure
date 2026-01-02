"""
Assert reutilizable que adjunta screenshot en caso de fallo en escenarios CRÍTICOS, INESPERADOS o AMBIGUOS.
El screenshot se captura en el momento exacto del fallo para aportar diagnóstico visual.
Los screenshots generales al finalizar el test se gestionan mediante el hook global de pytest (conftest.py)
"""


import allure
from allure_commons.types import AttachmentType


def assert_with_screenshot(
    condition: bool,
    driver,
    message: str,
    step_name: str = "Assertion failure"
):
    try:
        assert condition, message                         # si la condición es verdadera, el step continúa
    except AssertionError:
        allure.attach(                                    # se ejecuta solo si el assert fallo, screen exacto del fallo en el step
            driver.get_screenshot_as_png(),
            name=step_name,
            attachment_type=AttachmentType.PNG
        )
        raise                                             # pytest corta el escenario, allure lo marca como fallo y se ejecuta el hook