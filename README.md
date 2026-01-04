![UI Smoke Tests](https://github.com/Sabrina-Oroz/Selenium-Pytest-Allure/actions/workflows/ui-smoke.yml/badge.svg)

![UI Regression Tests](https://github.com/Sabrina-Oroz/Selenium-Pytest-Allure/actions/workflows/ui-regression.yml/badge.svg)


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

- Smoke tests: Validaciones funcionales críticas pre/post-deploy.
[Formato: Pytest + Parametrización en BDD (Happy Path y CNCN) + Allure con labels y steps]

CNCN: Casos Negativos Críticos de Negocio 
(ej: contraseña inválida, usuario bloqueado, pago rechazado)

- Regression tests: Cobertura en validaciones funcionales a nivel técnico. Es decir, combinaciones de datos y/o estados 
intermedios, escenarios negativos NO críticos, valores límites y validaciones de inputs masivas
(todo lo que puede romperse cuando se modifica código y afecte la calidad).
[Formato: Pytest + Parametrización de escenarios + Allure con labels y steps técnicos]

| Suite          | Contiene                                           | Severity posible          |
| -------------- |----------------------------------------------------| ------------------------- |
| **Smoke**      | Escenarios críticos de negocio (happy + negativos) | CRITICAL                  |
| **Regression** | Cobertura funcional profunda                       | CRITICAL / NORMAL / MINOR |


- **BDD** ---> funcionalidades o flujos de negocio críticos con Gherkin + Allure = Smoke tests

- **Pytest clásico** ---> validaciones técnicas y parametrizadas + Allure = Regression tests  

- **POM** ---> acciones de negocio encapsulando Selenium  

- **BasePage** ---> infra reutilizable  

- **Allure** ---> refleja feature, scenarios, tags (@smoke, @regression, @bdd), labels y parametrización pytest  

- **Escalabilidad** ---> agregado de features BDD sin duplicar lógica; Page Objects reutilizables con steps finitos  

- **Ejecución selectiva local y CI** ---> solo smoke, solo regression, solo BDD, todo



## Reglas de diseño
- No se duplican escenarios entre BDD y pytest parametrizado
- BDD se reserva para flujos críticos de negocio
- La regresión masiva se cubre con pytest parametrizado


## Estrategia de validaciones (asserts)
- Smoke / BDD: validaciones de estado final observable
- Regression: asserts estrictos y data-driven
- Page Objects no contienen asserts
- Las validaciones viven en tests o steps según el tipo de prueba.


## Asserts reutilizables y evidencias
- Existe un helper de assertions reutilizables (core/assertions.py) diseñado exclusivamente para:
  - Casos críticos
  - Fallos inesperados
  - Escenarios ambiguos donde el screenshot inmediato aporta un valor real para el diagnóstico
- Estos asserts pueden adjuntar screenshots en el punto exacto del fallo.
- Independientemente de esto, el framework siempre genera evidencias visuales al finalizar un test fallido 
  mediante un hook global de pytest (tests/conftest.py).


## Ejecución local
# Smoke tests 
pytest -m smoke --alluredir=reports/allure-results 
allure serve reports/allure-results

# Regression tests 
pytest -m regression --alluredir=reports/allure-results
allure serve reports/allure-results


## CI / CD en GitHub Actions
# El pipeline ejecuta:
- Instalación de dependencias 
- Smoke automático en push (local)
- Regression sólo en ejecución manual
- Generación dinámica de metadata en Allure (ambiente, executor, categorías por defecto)
- Histórico de ejecuciones
- Reportes Allure publicados en GitHub Pages (/smoke: siempre actualizado, /regression: sólo cuando corre).


## Reportes en Allure
# Cada ejecución genera:
- Reportes independientes por tipo de test
- Información del executor (GitHub)
- Variables de entorno que describen el contexto de ejecución
- Historial de ejecuciones para analizar tendencias y flaky tests (inestabilidad por timing, UI, red, waits)

