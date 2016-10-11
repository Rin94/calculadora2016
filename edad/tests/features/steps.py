# -*- coding: utf-8 -*-
from lettuce import step, world
from Edad import Edad

@step(u'Si "([^"]*)"')
def dado_que_tengo_el_numero_group1(step,num1):
    ed=Edad()
    world.resultado=ed.edad(num1)

@step(u'cuando realizo la operacion')
def cuando_realizo_la_op(step):
    pass

@step(u'la persona es "([^"]*)"')
def entonces_el_resultado_que_obtengo_es_suma(step, esperado):
    assert esperado==world.resultado, "El Resultado no coincide"
