# BDD (features y steps) convive con /smoke y /regression

# Smoke --> solo caso feliz con bdd

# Regression --> negativos críticos de negocio con bdd

# Usamos tags, que luego se integran con CI y Allure


Feature: Registro de usuario

  @smoke @bdd
  Scenario: Registro exitoso
    Given el usuario navega a la página de registro
    When ingresa nombre "Sabrina Oroz", email "ejemplo@gmail.com", dirección actual "Dirección 1", dirección permanente "Dirección 2"
    And envía el formulario
    Then debería ver sus datos reflejados en el resultado