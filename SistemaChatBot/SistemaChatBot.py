from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa=nomeEmpresa
        ##verificar se a lista de bots contém apenas bots
        for elemento in lista_bots:
            tem_tipo_bot = isinstance(elemento, Bot)
            if not tem_tipo_bot:
                mensagem_de_erro = ("Elemento de tipo diferente. A lista de"
                        + " bots deve conter somente instâncias de classes"
                        + " derivadas de Bot.")
                raise Exception(mensagem_de_erro)
        self.__lista_bots = lista_bots
        self.__bot = None
    
    def boas_vindas(self):
        print('Bom dia, esse é o sistema de bots da empresa 2Bots')

    def mostra_menu(self):
        for i in range(len(self.__lista_bots)):
            print(f'{i + 1}) Escolher bot {self.__lista_bots[i].nome} mensagem de apresentação: {self.__lista_bots[i].boas_vindas()}')
        ##mostra o menu de escolha de bots
    
    def escolhe_bot(self):
        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot 
        escolha = input('Escolha um dos bots: ')
        while not self.__check_input_in_range(1, len(self.__lista_bots), escolha):
            print('Valor não aceito, tente novamente')
            escolha = input('Escolha um dos bots: ')
        self.__bot = self.__lista_bots[int(escolha) - 1]
    @staticmethod
    def __check_input_in_range(min, max, num):
        if num.isnumeric():
            num = int(num)
            if num >= min and num <= max:
                return True
        return False
    def mostra_comandos_bot(self):
        print('Digite -1 para sair.')
        print(self.__bot.mostra_comandos())

    def le_envia_comando(self):
        escolha = input('Escolha alguma opção: ').strip()
        tem_comando_de_sair = escolha == "-1"
        if not tem_comando_de_sair:
            mensagem = self.__bot.executa_comando(escolha)
            self.imprimir_mensagem_com_nome_do_bot(mensagem)
        return escolha
        ##faz a entrada de dados do usuário e executa o comando no bot ativo

    def adiciona_nome_do_bot_na_mensagem(self, mensagem):
        mensagem_com_nome = self.__bot.nome + " diz: " + mensagem
        return mensagem_com_nome

    def imprimir_mensagem_com_nome_do_bot(self, mensagem):
        mensagem_com_nome = self.adiciona_nome_do_bot_na_mensagem(mensagem)
        print(mensagem_com_nome)

    def inicio(self):
        self.boas_vindas()
        self.mostra_menu()
        self.escolhe_bot()
        self.imprimir_mensagem_com_nome_do_bot(self.__bot.boas_vindas())
        while True:
            self.mostra_comandos_bot()
            escolha = self.le_envia_comando()
            if escolha == "-1":
                break

        self.imprimir_mensagem_com_nome_do_bot(self.__bot.despedida())
        ##mostra mensagem de boas-vindas do sistema
        ##mostra o menu ao usuário
        ##escolha do bot
        ##mostra mensagens de boas-vindas do bot escolhido
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ##ao sair mostrar a mensagem de despedida do bot

