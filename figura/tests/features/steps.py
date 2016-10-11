# -*- coding: utf-8 -*-
from lettuce import step, world
from figuras import Figuras

@step(u'Si "([^"]*)"')
def dado_que_tengo_el_numero_group1(step,num1):
    ed=Figuras()
    world.resultado=ed.cuadrado(int(num1))

@step(u'cuando realizo la operacion')
def cuando_realizo_la_op(step):
    pass

@step(u'resultado "([^"]*)"')
def entonces_el_resultado_que_obtengo_es_suma(step, esperado):
    assert int(esperado)==world.resultado, "El Resultado no coincide"
