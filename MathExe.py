# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 16:29:43 2022

@author: Duda Bastos
"""

def soma2valores(x,y):
    return x+y

x=float(input("x="))
y=float(input("y="))
print(f"Total={soma2valores(x,y)}")



###
import math as m
def RaizQuadrada(Inf, Sup):
    for i in range(Inf, Sup+1):
        print(m.sqrt(i), end=", ")
    return

RaizQuadrada(1, 20)



###
import numpy as np
a=np.array(range(1,21))
print(a)

b=a**.5 # ** = ^, n**2 = n^2, n**.5=n^(1/2)==raiz(n)
print(b)



###
import numpy as np
ar=np.array([[4,5,6],[3,8,7],[0,1,2],[4,5,6],[5,5,7],[1,4,6]])
print(ar)

for i in range(ar.shape[0]): #shape=nr de elementos da matriz
    print("Exemplo: ", ar[i])
    

    
###
import numpy as np
Est=np.array([["A. Gomes",50],["B. Silva",70],["C. Costa",20],["D. Simões",80], ["E. Cabrito",40],["F. Fonte",48]])
Est20=np.zeros(Est.shape[0])

for i in range(Est.shape[0]):
    Est20[i]=np.array(Est[i][1]) #[1] = 2ªcoluna (números)

Est20=Est20*20/100
print(Est20)

Passa=9.5
Sit=Est20 > Passa
print(Sit)
Sit=[x for x in range(Sit.shape[0]) if Sit[x]==True]
print("Aprovados: ")
for i in Sit:
    print(f"{Est[i][0]:8} {Est[i][1]: >5} {Est20[i]:>5}")









