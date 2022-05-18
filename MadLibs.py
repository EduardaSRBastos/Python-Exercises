# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 11:21:15 2022

@author: Eduarda
"""

print("Bem-vindo ao jogo MadLibs.\nEste jogo consiste em formar frases com os nomes/verbos/adjetivos inseridos por si.")

verb=input("Insira um verbo: ")
local=input("Insira um local: ")
num=input("Insira um número > 1: ")
animal=input("Insira um animal (plural e masculino): ")
nomeF=input("Insira um nome (feminino): ")
adj=input("Insira um adjetivo (masculino): ")
cor=input("Insira uma cor: ")

madlibs= f"Hoje fui {verb} no sítio do costume: {local}. Ao chegar a casa vi {num} {animal} no jardim da casa da frente.\n\
A Sra. {nomeF} andava a tentar apanhá-los, mas eles conseguiam fugir. Fui lá ajudá-la e um dos {animal} ficou parado a olhar \
para mim, a ver o que ia fazer. Era mesmo {adj} e tinha o corpo {cor}. Passado {num} horas, lá conseguimos apanhá-los.\n\
Foi um dia muito atarefado. "

print(madlibs)