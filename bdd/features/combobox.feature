# BDD (features y steps) convive con /smoke y /regression

# Smoke --> solo caso feliz con bdd

# Regression --> combinatoria de negativos críticos de negocio con bdd

# Usamos tags, que luego se integran con CI y Allure



Feature: Formulario de registro ComboBox 1

  Como usuario del sistema
  Quiero poder registrarme a través del formulario ComboBox 1
  Para acceder a las funcionalidades protegidas del sistema

@smoke @bdd
Scenario: ComboBox - Enviar formulario ComboBox (happy path)
  Given el usuario abre el formulario ComboBox
  When selecciona combo principal "Valor 2"
  And selecciona combos secundarios "Valor 1,Valor 3,Valor 4"
  And selecciona sistema "Windows" y versión "Windows 11"
  And hace click en el botón enviar
  Then el formulario se envía correctamente

@regression @bdd
Scenario Outline: ComboBox - Enviar formulario con combinaciones válidas
  Given el usuario abre el formulario ComboBox
  When selecciona combo principal "<combo1>"
  And selecciona combos secundarios "<combo2>"
  And selecciona sistema "<os>" y versión "<version>"
  And hace click en el botón enviar
  Then el formulario se envía correctamente

Examples:
| combo1  | combo2                    | os      | version        |
| Valor 2 | Valor 1,Valor 3,Valor 4   | Windows | Windows 11     |
| Valor 1 | Valor 2                   | Linux   | Ubuntu         |
| Valor 3 | Valor 1                   | Mac     | macOS Big Sur  |