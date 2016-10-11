class Edad():

    def edad(self,num1):
        try:
            num1=int(num1)
            if num1< 0:
                return "No existe"
            elif num1<13:
                return "Eres un nino"
            elif num1<18:
                return "Eres un adolecente"
            elif num1<64:
                return "Eres adulto"
            elif num1<119:
                return "adulto mayor"
            else:
                return "Eres mumra"
        except:
            return "No es edad"