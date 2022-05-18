# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 12:49:14 2022

@author: Eduarda
"""

import time

print("\nTemporizador")

def temporizador(t):
    while(t):
        mins, segs = divmod(t,60)
        contador = "\n{:02d}:{:02d}".format(mins, segs)
        print(contador, end="\r")
        time.sleep(1)
        t -= 1
        
    print("\nTemporizador chegou ao fim.")
        
t = input("Insira o tempo em segundos: ")

temporizador(int(t))
    

