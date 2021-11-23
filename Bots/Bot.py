##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r

class Bot(ABC):

    def __init__(self, nome):
        self.__nome = nome
        self.__comandos = {}

    @property
    def nome(self):
        return nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    def mostra_comandos(self):
        print('1 - Bom Dia')
        print('2 - Qual o seu nome?')
        print('3 - Quero um conselho')
        print('4 - Adeus')
    @abstractmethod
    def executa_comando(self,cmd):
        pass

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass