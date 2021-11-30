from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa=nomeEmpresa
        ##verificar se a lista de bots contém apenas bots
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
        self.__bot.mostra_comandos()

    def le_envia_comando(self):
        escolha = input('Escolha alguma opção: ')
        self.__bot.executa_comando(escolha)
        ##faz a entrada de dados do usuário e executa o comando no bot ativo

    def inicio(self):
        self.boas_vindas()
        self.mostra_menu()
        self.escolhe_bot()
        self.__bot.boas_vindas()
        while self.le_envia_comando() != '-1':
            self.mostra_comandos_bot()
            self.le_envia_comando()
        print(self.__bot.despedida())
        ##mostra mensagem de boas-vindas do sistema
        ##mostra o menu ao usuário
        ##escolha do bot      
        ##mostra mensagens de boas-vindas do bot escolhido
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ##ao sair mostrar a mensagem de despedida do bot
