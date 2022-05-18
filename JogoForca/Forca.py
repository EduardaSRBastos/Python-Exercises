# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 00:13:09 2022

@author: Eduarda
"""

import random
from palavras import animais, paises, alimentos
from desenhoForca import homem
import string

print("\nJogo da Forca")
palavraEsc = "r"
def get_palavras(palavras):
    escolha = "t"
    while(escolha != "A" and escolha != "a" and escolha != "P" and escolha != "p" and escolha != "C" and escolha != "c"):
        escolha = input("Escolha o tema: Animais (A), Países (P) ou Comida (C): ")
        
        if(escolha == "A" or escolha == "a"):
            tema = random.choice(animais)
        elif(escolha == "P" or escolha == "p"):
            tema = random.choice(paises)
        elif(escolha == "C" or escolha == "c"):
            tema = random.choice(alimentos)
        else:
            print("Escolheu a letra errada.")
            
    return tema.upper()

def forca():
    palavra = get_palavras(palavraEsc)
    letrasPalavra = set(palavra)
    alfabeto = set(string.ascii_uppercase)
    letrasUsadas = set()
    vidas = 7
    
    while (len(letrasPalavra) > 0 and vidas > 0):
        print(f"\nTem {vidas} tentativas. Usou as letras: ", "".join(letrasUsadas))
        listaLetras = [letra if letra in letrasUsadas else '-' for letra in palavra]
        print(homem[vidas])
        print("Palavra: ", "".join(listaLetras))
        
        letrasUser = input("Escolha uma letra: ").upper()
        if letrasUser in alfabeto - letrasUsadas:
            letrasUsadas.add(letrasUser)
            
            if letrasUser in letrasPalavra:
                letrasPalavra.remove(letrasUser)
                print("")
            else:
                vidas -= 1
                print(f"\nA letra {letrasUser} não pertence à palavra.")
                
        elif letrasUser in letrasUsadas:
            print(f"\nJá escolheu a letra {letrasUser}.")
            
        else:
            print("\nNão é uma letra válida.")
            
    if vidas == 0:
        print(homem[vidas])
        print(f"Perdeu... A palavra era: {palavra}.")
        
    else:
        print(f"Parabéns! Adivinhou a palavra '{palavra}'.")
        
if __name__ == "__main__":
    forca()
            
        
        
    