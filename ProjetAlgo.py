# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 14:03:11 2022

@author: Valentin
"""

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


def f(x):
    return max(x - 110,0)

pricer = pricer_1(20,0.02,0.05,-0.05,100,f)

#QUESTION 5

def trouverAnte(N,rN,hN,bN,x,qN,f):
    return (1/(1+rN))*(qN*f(x*(1+hN))+(1-qN)*f(x*(1+bN)))

def pricer_2(N,rN,hN,bN,s,f):
    init = [f(s*((1+rN)**k)*((1+hN)**(N-k)) for k in range(0,N+1)]
    for i in range(N-1,0,-1):
        #TODO
        
    

