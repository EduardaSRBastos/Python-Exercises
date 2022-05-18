# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 12:33:52 2022

@author: Eduarda
"""

import random

print("\nJogo - Descobre o número que o computador pensou.")

Max=int(input("Número limite: "))

def guess(num):
    randNum = random.randint(1,num)
    guess = 0
    while guess != randNum:
        guess = int(input(f"Escolha um número entre 1 e {num}: "))
        if guess < randNum:
            print("Escolha de novo. Pista: Número mais alto.")
        if guess > randNum:
            print("Escolha de novo. Pista: Número mais baixo.")
        
    print(f"\nParabéns! O número era {randNum}.")

guess(Max)

print("\n\nJogo - O computador descobre o número que pensou.")

def PCGuess(num):
    baixo = 1
    alto = num
    feedback = ""
    
    while feedback != "c":
        if baixo != alto:
            guess = random.randint(baixo,alto)
        else:
            guess = baixo
            
        feedback=input(f"O {guess} está acima(a), abaixo(b) ou correto(c)? ").lower()
        
        if feedback == "a":
            alto = guess - 1
            
        elif feedback == "b":
            baixo = guess + 1
    
    print(f"\nO computador acertou no número {guess} corretamente.")

PCGuess(Max)      
        
        