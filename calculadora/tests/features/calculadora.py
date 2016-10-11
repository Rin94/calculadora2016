class Calculadora ():

    def suma(self,num1,num2):
        return num1+num2

    def resta(self,num1,num2):
        return num1-num2

    def multiplicacion(self,num1,num2):
        return num1*num2

    def division(self,num1,num2):
        if num1 is 0:
            return "No se puede ese"
        else:
            return num1/num2
