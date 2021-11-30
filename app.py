#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotCansado import BotCansado
from Bots.BotLegal import BotLegal
from Bots.Botmanezinho import BotManezinho

###construa a lista de bots disponíveis aqui
lista_bots = [BotCansado("Yoda"), BotLegal('Zé'), BotManezinho('Carlos')]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
