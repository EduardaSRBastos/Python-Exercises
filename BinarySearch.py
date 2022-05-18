# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 10:51:54 2022

@author: Eduarda
"""

import random
import time

def naiveSearch(lista, num):
    for i in range(len(lista)):
        if lista[i] == num:
            return i
    return -1

def binarySearch(lista, num, baixo=None, alto=None):
    if baixo is None:
        baixo = 0
    if alto is None:
        alto = len(lista) - 1
    if alto < baixo:
        return -1
    
    meio = (baixo + alto) // 2
    
    if lista[meio] == num:
        return meio
    elif num < lista[meio]:
        return binarySearch(lista, num, baixo, meio - 1)
    else:
        return binarySearch(lista, num, meio + 1, alto)
    
if __name__ == "__main__":
    tam = 10000
    listaOrd = set()
    while len(listaOrd) < tam:
        listaOrd.add(random.randint(-3*tam, 3*tam))
    listaOrd = sorted(list(listaOrd))
    
    inicio = time.time()
    for num in listaOrd:
        naiveSearch(listaOrd, num)
    fim = time.time()
    print("Tempo Naive Search: ", round((fim-inicio), 3), "segundos.")
    
    inicio = time.time()
    for num in listaOrd:
        binarySearch(listaOrd, num)
    fim = time.time()
    print("Tempo Binary Search: ", round((fim-inicio), 3), "segundos.")