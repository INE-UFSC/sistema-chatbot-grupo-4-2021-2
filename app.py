#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotCansado import BotCansado

###construa a lista de bots disponíveis aqui
lista_bots = [BotCansado("Yoda")]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
