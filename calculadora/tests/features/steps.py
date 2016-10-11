# -*- coding: utf-8 -*-
from lettuce import step, world
from calculadora import Calculadora

@step(u'Dado que tengo los números "([^"]*)" y "([^"]*)"')
def dado_que_tengo_el_numero_group1_y_group1(step,num1,num2):
    cal= Calculadora()
    world.resultado=cal.suma(int(num1),int(num2))

@step(u'cuando realizo la suma')
def cuando_realizo_la_suma(step):
    pass
    
@step(u'entonces el resultado que obtengo de la suma es "([^"]*)"')
def entonces_el_resultado_que_obtengo_es_suma(step, esperado):
    assert int(esperado)==world.resultado, "El Resultado no coincide"

#

@step(u'Dado que tengo el número "([^"]*)" y "([^"]*)"')
def dado_que_tengo_el_numero_group2_y_group2(step,num1,num2):
    cal= Calculadora()
    world.resultado=cal.resta(int(num1),int(num2))

@step(u'cuando realizo la resta')
def cuando_realizo_la_resta(step):
    pass

@step(u'entonces el resultado que obtengo de la resta es "([^"]*)"')
def entonces_el_resultado_que_obtengo_es_resta(step, esperado):
    assert int(esperado)==world.resultado, "El Resultado no coincide"
#
@step(u'Si tengo  "([^"]*)" y "([^"]*)"')
def dado_que_tengo_el_numero_group3_y_group3(step,num1,num2):
    cal= Calculadora()
    world.resultado=cal.multiplicacion(int(num1),int(num2))

@step(u'cuando realizo la multiplicacion')
def cuando_realizo_la_multi(step):
    pass

@step(u'entonces el resultado que obtengo de la multi es "([^"]*)"')
def entonces_el_resultado_que_obtengo_es_multi(step, esperado):
    assert int(esperado)==world.resultado, "El Resultado no coincide"

#

@step(u'Si "([^"]*)" y "([^"]*)"')
def dado_que_tengo_el_numero_group4_y_group4(step,num1,num2):
    cal= Calculadora()
    world.resultado=cal.division(int(num1),int(num2))

@step(u'cuando realizo la division')
def cuando_realizo_la_div(step):
    pass

@step(u'entonces el resultado que obtengo de la div es "([^"]*)"')
def entonces_el_resultado_que_obtengo_es_div(step, esperado):

    assert int(esperado)==world.resultado, "El Resultado no coincide"