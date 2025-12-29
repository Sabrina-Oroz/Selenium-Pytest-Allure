# Infraestructura de testing que vive con los tests

""" Contiene: - fixture con driver compartido, un sólo driver por test (usa core/ driver_factory)
              - hook pytest_runtest_makereport con lógica de screenshots + Allure.
              - import steps. """


import pytest
from core.driver_factory import create_driver
import os                                                        # módulo de python para interactuar con el os
from datetime import datetime                                    # módulo de python para obtener marcas de tiempo
import allure                                                    # reportes + evidencias (sólo en fallos) + labels
from allure_commons.types import AttachmentType

## == Import de step definitions BDD ==
from bdd.steps.combobox_steps import *
from bdd.steps.login_steps import *
from bdd.steps.textbox_steps import *


@pytest.fixture
def driver():
    driver = create_driver()
    assert driver is not None, "ERROR: create_driver() devolvió None"

    yield driver             # acá se ejecuta el test, permitiendo ejecutar código después del mismo.
                             # Por ende, yield devuelve el driver al test, pausa el fixture y cuando el test termina,
                             # continúa guardando los resultados en formato Allure (hook de pytest más abajo).

    driver.quit()            # cierre automático y finalización del driver.
                             # se ejecuta SIEMPRE, incluso si el test falla.


""" Evidencias + reportes:
Este hook permite que pytest guarde las ejecuciones en allure y genere los screenshots en caso de fallo. """

SCREENSHOTS_DIR = os.path.join(
    os.getcwd(), "reports", "screenshots")

os.makedirs(SCREENSHOTS_DIR, exist_ok=True)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # === yield permite que pytest ejecute el test y luego que vuelva con el resultado ===
    outcome = yield
    report = outcome.get_result()

    # === Filtro sólo cuando falla el test === report objeto con info de ejecución del test (fase call) ===
    if report.when == "call" and report.failed:

        ## === Búsqueda del driver === item.funcargs.get diccionario con los fixtures usados por el test.
        #      Si no encuentra el driver, devuelve none (fallos por desactualización) ===
        driver = item.funcargs.get("driver", None)
        if not driver:
            return

        # === Data del test === test_name: def test_textbox_page(): + timestamp: fecha y hora ===
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")                 # evita sobrescritura
        test_name = item.nodeid.replace("::", "_").replace("/", "_")             # nombre en el archivo (orden y traza)

        # === Mapeo de data en el screen ===
        screenshot_name = f"{test_name}__FAILED__{timestamp}.png"
        screenshot_path = os.path.join(SCREENSHOTS_DIR, screenshot_name)

        # === Selenium guarda screenshot en disco (quedando disponible fuera de allure) ===
        driver.save_screenshot(screenshot_path)

        # === Pytest adjunta screenshot a Allure (attach) ===
        allure.attach(
            driver.get_screenshot_as_png(),
            name=f"{test_name} - failure",
            attachment_type=AttachmentType.PNG
        )

"""
Cuando Pytest termina un test, si el test falló, busca el driver del fixture y luego saca screenshot 
(esto último a través de selenium).
Acción siguiente: Pytest lo guarda en el disco: directorios reports/screenshots/ y posterior adjunta al reporte Allure. 
Este hook, a nivel framework, se ejecuta y controla el final del ciclo de vida de las pruebas.
"""