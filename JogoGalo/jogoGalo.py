# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 11:50:40 2022

@author: Eduarda
"""

import math
import time
from Jogador import User, ComputadorSmart

class JogoGalo():
    def __init__(self):
        self.tabuleiro = self.fazerTab()
        self.vencedorAtual = None
    
    @staticmethod
    def fazerTab():
        return[" " for _ in range(9)]
    
    def printTab(self):
        for linha in [self.tabuleiro[i*3:(i+1)*3] for i in range(3)]:
            print("|" + "|".join(linha) + "|")
            
    @staticmethod
    def printTabNums():
        numTab = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for linha in numTab:
            print("|" + "|".join(linha) + "|")
            
    def fazerMov(self, quadrado, letra):
        if self.tabuleiro[quadrado] == " ":
            self.tabuleiro[quadrado] = letra
            if self.vencedor(quadrado, letra):
                self.vencedorAtual = letra
            return True
        return False
    
    def vencedor(self, quadrado, letra):
        linhaI = math.floor(quadrado/3)
        linha = self.tabuleiro[linhaI*3:(linhaI+1)*3]
        if all([s == letra for s in linha]):
            return True
        
        colI = quadrado % 3
        coluna = [self.tabuleiro[colI+i*3] for i in range(3)]
        if all([s == letra for s in coluna]):
            return True
        if quadrado % 2 == 0:
            diagonal1 = [self.tabuleiro[i] for i in [0, 4, 8]]
            if all([s == letra for s in diagonal1]):
                return True
            diagonal2 = [self.tabuleiro[i] for i in [2, 4, 6]]
            if all([s == letra for s in diagonal2]):
                return True
        return False
    
    def quadVazios(self):
        return " " in self.tabuleiro
    def numQuadVazios(self):
        return self.tabuleiro.count(" ")
    def movValido(self):
        return [i for i, x in enumerate(self.tabuleiro) if x==" "]
    
def jogada(jogo, xJog, oJog, printJogo=True):
    if printJogo:
        jogo.printTabNums()
    
    letra = "X"
    while jogo.quadVazios():
        if letra == "O":
            quadrado = oJog.mov(jogo)
        else:
            quadrado = xJog.mov(jogo)
        
        if jogo.fazerMov(quadrado, letra):
            if printJogo:
                print(letra + " moveu para quadrado {}".format(quadrado))
                jogo.printTab()
                print("")
            
            if jogo.vencedorAtual:
                if printJogo:
                    print(letra + " ganhou!")
                return letra
            letra = "O" if letra == "X" else "X"
        
        time.sleep(2)
    
    if printJogo:
        print("É empate!")
        
if __name__ == "__main__":
    xJog = ComputadorSmart("X")
    oJog = User("O")
    t = JogoGalo()
    jogada(t, xJog, oJog, printJogo=True)
        
    