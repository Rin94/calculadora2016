Feature: Verificar edades.
  Yo como usuario de la app Edad
  quiero realizar etiquetar la edad de una persona
  para poder sentirme mejor conmigomismo porque no tengo autoestima.

  Scenario: Comprobar nino.
    Si "12"
    cuando realizo la operacion
    la persona es "Eres un nino"

  Scenario: Comprobar noEs.
    Si "-1"
    cuando realizo la operacion
    la persona es "No existe"

  Scenario: Comprobar adolecente.
    Si "17"
    cuando realizo la operacion
    la persona es "Eres un adolecente"

  Scenario: Comprobar adulto
    Si "33"
    cuando realizo la operacion
    la persona es "Eres adulto"

  Scenario: Comprobar adulto
    Si "70"
    cuando realizo la operacion
    la persona es "adulto mayor"

  Scenario: Comprobar momia
    Si "130"
    cuando realizo la operacion
    la persona es "Eres mumra"

  Scenario: Comprobar noNumero
    Si "h"
    cuando realizo la operacion
    la persona es "No es edad"
