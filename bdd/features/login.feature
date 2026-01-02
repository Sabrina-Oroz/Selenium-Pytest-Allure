# BDD (features y steps) convive con /smoke y /regression

# Smoke --> solo caso feliz con bdd

# Regression --> combinatoria de negativos críticos de negocio con bdd

# Usamos tags, que luego se integran con CI y Allure



Feature: Login de usuario

  Como usuario del sistema
  Quiero poder iniciar sesión
  Para acceder a las funcionalidades protegidas del sistema

  @smoke @bdd
  Scenario: Login exitoso con credenciales válidas
    Given el usuario navega a la página de login
    When ingresa usuario "tomsmith" y password "SuperSecretPassword!"
    And hace click en el botón login
    Then debería acceder al área segura del sistema

  @smoke @bdd
  Scenario: Login fallido con usuario inválido
    Given el usuario navega a la página de login
    When ingresa usuario "usuario_invalido" y password "SuperSecretPassword!"
    And hace click en el botón login
    Then debería ver un mensaje de error por usuario inválido

  @smoke @bdd
  Scenario: Login fallido con password inválida
    Given el usuario navega a la página de login
    When ingresa usuario "tomsmith" y password "incorrecta"
    And hace click en el botón login
    Then debería ver un mensaje de error por credenciales inválidas

  @smoke @bdd
  Scenario: Login fallido sin password
    Given el usuario navega a la página de login
    When ingresa usuario "tomsmith" y password " "
    And hace click en el botón login
    Then debería ver un mensaje de error por password requerida




 # Usuario bloqueado → Smoke + CRITICAL

 # Error en recuperación de contraseña → Regression + CRITICAL

 # Validación de largo de password → Regression + MINOR

 # Combinaciones de datos → Regression + NORMAL

 ## == Smoke es un subconjunto de Regression, no lo opuesto.
 ##    Eso protege al negocio, no al código.