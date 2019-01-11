#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 19:10:26 2019

@author: pepe
You are given an integer, . Your task is to print an alphabet rangoli of size

. (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----


#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""


def print_row(r, n):
    total = 2*n+2*(n-1)-1
    n_minus = total - 2*(2*r+1)+1
    mitad = n_minus//2
    for i in range(mitad):
        print('-', end='')
    for i in range(r+1):
        if r > 0:
            print('{0}-'.format(chr(ord('a')+n-i-1)), end='')
        else:
            print('{0}'.format(chr(ord('a')+n-i-1)), end='')
    for i in range(r-1):
        print('{0}-'.format(chr(ord('a')+n-r+i)), end='')
    if r > 0:
        print('{0}'.format(chr(ord('a')+n-1)), end='')
    for i in range(mitad):
        print('-', end='')
    print('')


def create_square(n):
    for r in range(n):
        print_row(r,n)
    for r in range(1,n):
        print_row(n-r-1,n)


if __name__ == '__main__':
    create_square(5)
#    for i in range(27):
#        print('{0}'.format(chr(i+ord('a'))))
