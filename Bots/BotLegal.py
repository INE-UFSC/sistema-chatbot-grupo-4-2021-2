from Bots.Bot import Bot

class BotLegal(Bot):
    def __init__(self, nome):
        self.__nome = nome
        self.comandos = {}

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo):
        self.__nome = novo

    def apresentacao(self):
        return "Olá! Eu sou o Bot Legal, podemos ser amigos?"
 
    def mostra_comandos(self):
        self.comandos = {
                "1": "Apresentar",
                "2": "Boas vindas",
                "3": "Mostrar despedida"
                }
        numero_de_comandos = len(self.comandos)
        mensagem = ""
        for numero, texto in self.comandos.items():
            mensagem += f"{numero} - {texto}"
            tem_proxima_linha = numero != numero_de_comandos
            if tem_proxima_linha:
                mensagem += "\n"
        return(mensagem)
    
    def executa_comando(self,cmd):
        cmd = int(cmd)
        if cmd <= len(self.comandos):
            if cmd == 1:
                return self.apresentacao()
            elif cmd == 2:
                return self.boas_vindas()
            elif cmd == 3:
                return self.despedida()
        else:
            return "comando invalido"

    def boas_vindas(self):
        return "Oii, que bom que voçê me escolheu, acho que já somos amigos então"

    def despedida(self):
        return "Aff, você já está indo? Até uma próxima então"