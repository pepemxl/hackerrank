#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 18:36:25 2019

@author: pepe

A palindromic number reads the same both ways. The smallest 6 digit palindrome made from the product of two 3-digit numbers is .

Find the largest palindrome made from the product of two 3-digit numbers which is less than 
"""

def is_palindrome(palabra):
    flag = True
    n = len(palabra)
    for i in range(n//2):
        if palabra[i] != palabra[n-i-1]:
            flag = False
            break
    return flag


def is_product_3digits(num):
    flag = False
    for i in range(100,1000):
        for j in range(100,1000):
            if i*j == num:
                flag = True
    return flag

def find_max_poli3(n):
    for i in range(n):
        num = n - i
        if is_palindrome(str(num)):
            if is_product_3digits(num):
                break
    return num


def run(lista):
    N = len(lista)
    for i in range(N):
        a = find_max_poli3(lista[i])
        print(a)

if __name__ == '__main__':
    N = 2
    lista = [101110, 800000]
    run(lista)