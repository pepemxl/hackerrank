#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 20:02:55 2019

@author: pepe
"""

import sys
import math

criba = []


def primes_sieve2(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False
                
def calcula_criba(n):
    global criba
    N = n//2
    criba = [1]*(N+1)
    criba[0] = 0
    criba[1] = 0
    for (i, is_prime) in enumerate(criba):
        if is_prime == 1:
            yield i
            for j in range(i*i, N, i):
                criba[j] = 0
#    current = 2
#    contador = 0
#    while current < N and contador < 100000:
#        for i in range(current,N//current+1):
#            criba[i*current] = 0
#        while current < N and criba[current+1] == 0:
#            current += 1
#        contador += 1
        
def calcula(n):
    global criba
    maximo = 2
    numero = n//2
    flag_n = False
    while (2 <= numero and flag_n == False):
        if criba[numero] == 1:
            # print('{0} {1}'.format(n,numero))
            if n%numero == 0:
                maximo = numero
                flag_n = True
        numero -= 1
    if flag_n == False:
        # print('{0} {1}'.format(n,numero))
        maximo = n
    return maximo
            
lista = []
#t = int(input().strip())
t = 2
#for a0 in range(t):
#    n = int(input().strip())
#    lista.append(n)
lista.append(10)
lista.append(170)
N = max(lista)
calcula_criba(N)
print(criba)
# print(criba)
#for a0 in range(t):
#    n = lista[a0]
#    print(calcula(n))