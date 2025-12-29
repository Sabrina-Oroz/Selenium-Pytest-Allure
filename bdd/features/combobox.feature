# BDD (features y steps) convive con /smoke y /regression

# Smoke --> solo caso feliz con bdd

# Regression --> combinatoria de negativos críticos de negocio con bdd

# Usamos tags, que luego se integran con CI y Allure



Feature: Formulario de registro ComboBox 1

@smoke @bdd
Scenario: Enviar formulario ComboBox (happy path)
  Given el usuario abre el formulario ComboBox
  When selecciona combo principal "Valor 2"
  And selecciona combos secundarios "Valor 1,Valor 3,Valor 4"
  And selecciona sistema "Windows" y versión "Windows 11"
  Then el formulario se envía correctamente

@regression @bdd
Scenario Outline: Enviar formulario con combinaciones válidas
  Given el usuario abre el formulario ComboBox
  When selecciona combo principal "<combo1>"
  And selecciona combos secundarios "<combo2>"
  And selecciona sistema "<os>" y versión "<version>"
  Then el formulario se envía correctamente

Examples:
| combo1  | combo2                    | os      | version        |
| Valor 2 | Valor 1,Valor 3,Valor 4   | Windows | Windows 11     |
| Valor 1 | Valor 2                   | Linux   | Ubuntu         |
| Valor 3 | Valor 1                   | Mac     | macOS Big Sur  |