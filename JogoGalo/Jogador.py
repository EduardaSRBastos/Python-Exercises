# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 11:07:03 2022

@author: Eduarda
"""

import math
import random

class Jogador():
    def __init__(self, letra):
        self.letra = letra
        
    def mov(self, jogo):
        pass
    
class User(Jogador):
    def __init__(self, letra):
        super().__init__(letra)
        
    def mov(self, jogo):
        quad_valido = False
        val = None
        while not quad_valido:
            quadrado = input(self.letra + "\" turno. Escolha movimento (0-8): ")
            try:
                val = int(quadrado)
                if val not in jogo.movValido():
                    raise ValueError
                quad_valido = True
            except ValueError:
                print("Quadrado inválido. Tente de novo.")
        return val
    
class ComputadorSmart(Jogador):
    def __init__(self, letra):
        super().__init__(letra)
        
    def mov(self, jogo):
        if len(jogo.movValido()) == 9:
            quadrado = random.choice(jogo.movValido())
        else:
            quadrado = self.minimax(jogo, self.letra)["posicao"]
        return quadrado
    
    def minimax(self, estado, jogador):
        maxJog = self.letra
        outroJog = "O" if jogador == "X" else "X"
        
        if estado.vencedorAtual == outroJog:
            return {"posicao": None, "pontuacao": 
                    1*(estado.numQuadVazios() + 1) 
                    if outroJog == maxJog 
                    else -1*(estado.numQuadVazios() + 1)}
        elif not estado.quadVazios():
            return {"posicao": None, "pontuacao": 0}
        
        if jogador == maxJog:
            melhor = {"posicao": None, "pontuacao": -math.inf}
        else:
            melhor = {"posicao": None, "pontuacao": math.inf}
        
        for movPossivel in estado.movValido():
            estado.fazerMov(movPossivel, jogador)
            pontuacao = self.minimax(estado, outroJog)
            
            estado.tabuleiro[movPossivel] = " "
            estado.vencedorAtual = None
            pontuacao["posicao"] = movPossivel
            
            if jogador == maxJog:
                if pontuacao["pontuacao"] > melhor["pontuacao"]:
                    melhor = pontuacao
            else:
                if pontuacao["pontuacao"] < melhor["pontuacao"]:
                    melhor = pontuacao
        
        return melhor
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                
            
            
            
            