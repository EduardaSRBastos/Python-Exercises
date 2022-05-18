# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 14:27:20 2022

@author: Eduarda
"""

print("\nJogo - Pedra, Papel, Tesoura")

import random

def play():
    
    user = "R"
    
    while (user != "P" and user != "A" and user != "T"):
       print("\n\nInsira a letra 'P', 'A' ou 'T'.")
       user = input("Pedra (P), Papel (A), Tesoura (T)? ")
       
    pc = random.choice(["P", "A", "T"])
    
    if user == pc:
        return ("\nEmpate!")
    
    if userWin(user, pc):
        return ("\nGanhou!")
    
    return ("\nPerdeu!")

def userWin(jog, comp):
    if (jog == "P" and comp == "T") or (jog == "T" and comp == "A") or (jog == "A" and comp == "P"):
        return True
    
print(play())     