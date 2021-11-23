from Bots.Bot import Bot

class BotLegal(Bot):
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(nome):
        self.__nome= nome

    def apresentacao(self):
        return "Olá! Eu sou o Bot Legal, podemos ser amigos?"
 
    def mostra_comandos(self):
        pass
    
    def executa_comando(self,cmd):
        pass

    def boas_vindas(self):
        return "Oii, que bom que voçê me escolheu, acho que já somos amigos então"

    def despedida(self):
        return "Aff, você já está indo? Até uma próxima então"