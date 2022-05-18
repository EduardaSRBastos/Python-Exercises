# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 17:59:10 2022

@author: Eduarda
"""

from pprint import pprint

def encontrarVazio(puzzle):
    for l in range(9):
        for c in range(9):
            if puzzle[l][c] == -1:
                return l,c
    
    return None, None

def valido(puzzle, num, linha, col):
    linhaNums = puzzle[linha]
    if num in linhaNums:
        return False
    colNums = [puzzle[i][col] for i in range(9)]
    if num in colNums:
        return False
    
    linhaInicio = (linha // 3) * 3
    colInicio = (col // 3) * 3
    
    for l in range(linhaInicio, linhaInicio +3):
        for c in range(colInicio, colInicio +3):
            if puzzle[l][c] == num:
                return False
    
    return True

def resolver(puzzle):
    linha, col = encontrarVazio(puzzle)
    
    if linha is None:
        return True
    
    for num in range(1, 10):
        if valido(puzzle, num, linha, col):
            puzzle[linha][col] = num
            if resolver(puzzle):
                return True
        
        puzzle[linha][col] = -1
    
    return False

if __name__ == "__main__":
    exemplo=[
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    
    
    print(resolver(exemplo))
    print("Solução do sudoku: ")
    pprint(exemplo)
            
