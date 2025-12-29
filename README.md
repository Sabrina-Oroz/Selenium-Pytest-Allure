[![UI Tests - Smoke](https://github.com/Sabrina-Oroz/Selenium-Pytest-Allure/actions/workflows/ui-tests.yml/badge.svg)](
https://github.com/Sabrina-Oroz/Selenium-Pytest-Allure/actions/workflows/ui-tests.yml
)

## Selenium + Pytest + Allure
Proyecto de automatización con tecnologías:
- Python 3.11+
- Selenium
- Pytest
- Allure CLI
- Page Object Model
- BDD
- CI con GitHub Actions


## Estrategia de testing y framework

- Smoke tests: Validaciones funcionales críticas post-deploy.
[Formato: Pytest + Parametrización en BDD (Happy Path y 1-2 CNCN) + Allure con labels y steps técnicos]

CNCN: Casos Negativos Críticos de Negocio 
(ej: contraseña inválida, usuario bloqueado, pago rechazado)

- Regression tests: Cobertura en validaciones de calidad a nivel técnico. Es decir, combinaciones de estados intermedios, 
escenarios negativos no críticos, valores límites y validaciones de inputs masivas (todo lo que puede romperse cuando se
modifica código y afecte la calidad).
[Formato: Pytest + Parametrización de escenarios + Allure con labels y steps técnicos]

- BDD ---> funcionalidades o flujos de negocio críticos con Gherkin + Allure = Smoke tests

- Pytest clásico ---> validaciones técnicas y parametrizadas + Allure = Regression tests

- POM ---> acciones de negocio encapsulando selenium

- BasePage ---> infra reutilizable

- Allure ---> refleja feature, scenarios, tags (@smoke, @regression, @bdd), labels y parametrización pytest

- Escalabilidad: - Agregado de features BDD sin duplicar lógica 
                 - Los Page Objects se reutilizan con steps finitos.

- Ejecución selectiva local y CI ---> solo smoke, solo regression, solo bdd, todo


## Reglas de diseño
- No se duplican escenarios entre BDD y pytest parametrizado
- BDD se reserva para flujos críticos de negocio
- La regresión masiva se cubre con pytest parametrizado


# Estrategia de validaciones (asserts)
- Smoke / BDD: validaciones de estado final observable
- Regression: asserts estrictos y data-driven
- Page Objects no contienen asserts
- Las validaciones viven en tests o steps según el tipo de prueba.


## Ejecución local
# Smoke tests 
pytest -m smoke --alluredir=reports/allure-results 
allure serve reports/allure-results

# Regression tests 
pytest -m regression --alluredir=reports/allure-results
allure serve reports/allure-results


## CI en GitHub
- Smoke automático en push (local)
- Regression sólo en ejecución manual
- Reportes Allure publicados en GitHub Pages (/smoke: siempre actualizado, /regression: sólo cuando corre).