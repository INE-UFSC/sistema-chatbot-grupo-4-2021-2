from Bots.Bot import Bot

class BotCansado(Bot):
    def __init__(self,nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    def apresentacao_Cansado(self):
        mensagem = "Olá, pronto para o próximo comando."
        print(mensagem)
 
    def mostra_comandos(self):
        pass
    
    def executa_comando(self,cmd):
        pass

    def boas_vindas_Cansado(self):
        mensagem = "Seja bem-vindo(a)."
        print(mensagem)

    def despedida(self):
        mensagem = "Foi um prazer. Volte sempre."
        print(mensagem)

