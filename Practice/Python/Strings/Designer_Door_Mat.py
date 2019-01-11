#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 17:42:23 2019
Size: 7 x 21 
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------
@author: pepe
"""


def print_row(r, N):
    n_minus = 0
    if r < N//2:
        n_minus = 3*N - (2*r+1)*3
    elif r > N//2:
        n_minus = 3*N - (2*(N-r-1)+1)*3
    else:
        n_minus = 3*N -7
    mitad = n_minus//2
    for i in range(mitad):
        print('-', sep='', end='')
    if r < N//2:
        for i in range(2*r+1):
            print('.|.', sep='', end='')
    elif r > N//2:
        for i in range(2*(N-r-1)+1):
            print('.|.', sep='', end='')
    else:
        print('WELCOME', sep='', end='')
    for i in range(mitad):
        print('-', sep='', end='')


def create_door(N):
    for r in range(N):
        print_row(r, N)
        print('')


if __name__ == '__main__':
    create_door(1)