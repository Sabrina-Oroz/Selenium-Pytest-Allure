"""
Smoke → solo caso feliz

Regression → negativo crítico

Usamos tags, que luego se integran con CI y Allure

"""


Feature: Login de usuario

  Como usuario del sistema
  Quiero poder iniciar sesión
  Para acceder a las funcionalidades protegidas

  @smoke @bdd
  Scenario: Login exitoso con credenciales válidas
    Given el usuario navega a la página de login
    When ingresa usuario "tomsmith" y password "SuperSecretPassword!"
    And hace click en el botón login
    Then debería acceder al área segura

  @regression @bdd
  Scenario: Login fallido con password inválida
    Given el usuario navega a la página de login
    When ingresa usuario "tomsmith" y password "incorrecta"
    And hace click en el botón login
    Then debería ver un mensaje de error