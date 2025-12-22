[![UI Tests - Smoke](https://github.com/Sabrina-Oroz/Selenium-Pytest-Allure/actions/workflows/ui-tests.yml/badge.svg)](
https://github.com/Sabrina-Oroz/Selenium-Pytest-Allure/actions/workflows/ui-tests.yml
)

## Selenium + Pytest + Allure

Proyecto de automatización con tecnologías:
- Selenium
- Pytest
- Allure
- Page Object Model
- CI con GitHub Actions


## Ejecución local

# Smoke tests
pytest tests/smoke --alluredir=reports/allure-results
allure serve reports/allure-results

# Regression tests
pytest tests/regression --alluredir=reports/allure-results
allure serve reports/allure-results