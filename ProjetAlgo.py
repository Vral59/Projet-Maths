# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 14:03:11 2022

@author: Valentin
"""

""" IMPORT """
import random


#QUESTION 1
""" qN = (rN-bN)/(hN-bN) """


#QUESTION 2
""" Voir fonction dans QUESTION 3 """

#QUESTION 3
   
def trianglePascal(n):
    T = [[0] * (n+1) for p in range(n+1)]
    for n in range(n+1):
        if n == 0:
            T[n][0] = 1
        else:
            for k in range(n+1):
                if k == 0:
                    T[n][0] = 1
                else:
                    T[n][k] = T[n-1][k-1] + T[n-1][k]
    return T



def pricer_1(N,rN,hN,bN,s,f):
    qN = (rN-bN)/(hN-bN)
    T = trianglePascal(N)
    somme = 0
    for k in range(0,N+1):
        somme += f(s*((1+hN)**k)*((1+bN)**(N-k)))*T[N][k]*(qN**k)*((1-qN)**(N-k))
    return (1/((1+rN)**N))*somme

#QUESTION 4

def f1(x):
    return max(x - 110,0)

pricer = pricer_1(20,0.02,0.05,-0.05,100,f1)

print("Question 4 :")
print("Prix : ",pricer)

#QUESTION 5


def pricer_2(N,rN,hN,bN,s,f):
    qN = (rN-bN)/(hN-bN)
    # Initialisation des f(x) à la fin de l'arbre
    tree = [[f(s*((1+bN)**k)*((1+hN)**(N-k))) for k in range(0,N+1)]]
    for n in range(N,0,-1):
        aux = []
        for i in range(0,n):
            fup = tree[-1][i]
            fdown = tree[-1][i+1]
            vn = (1/(1+rN))*(qN*fup+(1-qN)*fdown)
            aux.append(vn)
        tree.append(aux)
    return tree

def f2(x):
    return max(x - 100,0)

#QUESTION 6

print("Question 6 :")
arbre = pricer_2(3,0.02,0.05,-0.05,100,f2)
print("Prix : ", arbre[-1][0])
print("Voici l'arbre :",arbre)
#L'arbre est aussi visible en .SVG 

#QUESTION 7

randomN = random.randint(5, 15)
s = 100
rN = 0.01
hN = 0.05
bN = -0.05

tree = pricer_2(randomN,rN,hN,bN,s,f1)

pricerRandom1 = pricer_1(randomN,rN,hN,bN,s,f1) 
pricerRandom2 = tree[-1][0]

print("Question 7 :")
print("On a N = ",randomN)
print("pricer 1 avec N random :", pricerRandom1)
print("pricer 2 avec N random :", pricerRandom2)
