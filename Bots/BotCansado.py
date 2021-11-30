from Bots.Bot import Bot
from random import randint

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
        comandos = {
                "1": "Apresentar",
                "2": "Mostrar um conselho",
                "3": "Mostrar despedida"
                }
        numero_de_comandos = len(comandos)
        mensagem = ""
        for numero, texto in comandos.items():
            mensagem += f"{numero} - {texto}"
            tem_proxima_linha = numero != numero_de_comandos
            if tem_proxima_linha:
                mensagem += "\n"
        print(mensagem)
    
    def executa_comando(self,cmd):
        if cmd == "1":
            self.apresentacao_Cansado()
        elif cmd == "2":
            self.mostra_conselho()
        elif cmd == "3":
            self.despedida()

    def boas_vindas_Cansado(self):
        mensagem = "Seja bem-vindo(a)."
        print(mensagem)

    def despedida(self):
        mensagem = "Foi um prazer. Volte sempre."
        print(mensagem)
    
    def mostra_conselho(self):
        conselhos = (
                "Estude ao menos 1 hora por dia.",
                "Programe computador todos os dias",
                "Faça ao menos 30 minutos de atividade física por dia.",
                ("Mantenha uma alimentação saudável com frutas, legumes e"
                    + " vegetais todos os dias."),
                ("Use máscara para impedir a propagação de epidemias"
                    + " respiratórias.")
                )
        indice_aleatorio = randint(0, len(conselhos) - 1)
        conselho_aleatorio = conselhos[indice_aleatorio]
        print(conselho_aleatorio)

