# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 11:08:26 2022

@author: Eduarda
"""

import random
import re

class Campo:
    def __init__(self, tamanho, numBombas):
        self.tamanho = tamanho
        self.numBombas = numBombas
        
        self.campo = self.novoCampo()
        self.valoresCampo()
        
        self.buraco = set()
        
    def novoCampo(self):
        campo = [[None for _ in range(self.tamanho)] for _ in range(self.tamanho)]
        
        bombasCampo = 0
        while bombasCampo < self.numBombas:
            loc = random.randint(0, self.tamanho**2 - 1)
            linha = loc//self.tamanho
            col = loc% self.tamanho
            
            if campo[linha][col] == "*":
                continue
            
            campo[linha][col] = "*"
            bombasCampo +=1
        
        return campo
    
    def valoresCampo(self):
        for l in range(self.tamanho):
            for c in range(self.tamanho):
                if self.campo[l][c] == "*":
                    continue
                self.campo[l][c] = self.numBombViz(l,c)
    
    def numBombViz(self, linha, col):
        numBomb = 0
        for l in range(max(0, linha - 1), min(self.tamanho - 1, linha + 1)+1):
            for c in range(max(0, col - 1), min(self.tamanho - 1, col + 1)+1):
                if l == linha and c == col:
                    continue
                if self.campo[l][c] == "*":
                    numBomb +=1
        return numBomb
    
    def buracos(self, linha, col):
        self.buraco.add((linha, col))
        
        if self.campo[linha][col] == "*":
            return False
        elif self.campo[linha][col] > 0:
            return True
        
        for l in range(max(0, linha-1), min (self.tamanho-1, linha+1)+1):
            for c in range(max(0, col-1), min (self.tamanho-1, col+1)+1):
                if(l, c) in self.buraco:
                    continue
                self.buracos(l, c)
        
        return True
    
    def __str__(self):
        campoVisivel = [[None for _ in range(self.tamanho)] for _ in range(self.tamanho)]
        for linha in range(self.tamanho):
            for col in range(self.tamanho):
                if(linha, col) in self.buraco:
                    campoVisivel[linha][col] = str(self.campo[linha][col])
                else:
                    campoVisivel[linha][col] = " "
            
        stringRep = ""
        largura = []
        for idx in range(self.tamanho):
            colunas = map(lambda x: x[idx], campoVisivel)
            largura.append(len(max(colunas, key = len)))
        
        indices = [i for i in range(self.tamanho)]
        indicesLinha="   "
        cels = []
        for idx, col in enumerate(indices):
            format = "%-" + str(largura[idx]) + "s"
            cels.append(format % (col))
        indicesLinha += "  ".join(cels)
        indicesLinha += "  \n"
        
        for i in range(len(campoVisivel)):
            linha = campoVisivel[i]
            stringRep += f"{i} |"
            cels = []
            for idx, col in enumerate(linha):
                format = "%-" + str(largura[idx]) + "s"
                cels.append(format % (col))
            stringRep += " |".join(cels)
            stringRep += " |\n"
            
        strTam = int(len(stringRep)/(self.tamanho))
        stringRep = indicesLinha + "-"*strTam + "\n" + stringRep + "-"*strTam
        
        return stringRep

def jogo(tamanho=10, numBombas=10):
    campo = Campo(tamanho, numBombas)
    
    salvo = True
    
    while len(campo.buraco) < campo.tamanho**2 - numBombas:
        print(campo)
        userInput = re.split(",(\\s)*", input("Onde quer abrir buraco? Insira Linha, Coluna: "))
        linha, col = int(userInput[0]), int(userInput[-1])
        if linha < 0 or linha >= campo.tamanho or col < 0 or col >= tamanho:
            print("Local inválido. Tente de novo.")
            continue                                      
         
        salvo = campo.buracos(linha, col)
        if not salvo:
            break
        
    if salvo:
        print("Parabéns! Ganhou.")
    else:
        print("Perdeu, caiu numa bomba.")
        campo.buraco = [(l,c) for l in range(campo.tamanho) for c in range(campo.tamanho)]
        print(campo)
        
if __name__ == "__main__":
    jogo()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        