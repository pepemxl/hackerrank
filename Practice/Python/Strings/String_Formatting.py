#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 18:12:30 2019

@author: pepe
"""


def print_binary(i, n):
    print('{0:{1}b}'.format(i, len('{0:b}'.format(n))+1), end='')


def print_octal(i, n):
    print('{0:{1}o}'.format(i, len('{0:o}'.format(n))+1), end='')


def print_hexadecimal(i, n):
    print('{0:{1}X}'.format(i, len('{0:X}'.format(n))+1), end='')


if __name__ == '__main__':
    n = 20
#    for i in range(n):
#        print('{0:{1}}'.format(i,len('{0:b}'.format(n))+1), end='')
#        print('{0:{1}o}'.format(i, len('{0:b}'.format(n))+1), end='')
#        print('{0:{1}X}'.format(i, len('{0:b}'.format(n))+1), end='')
#        print('{0:{1}b}'.format(i, len('{0:b}'.format(n))+1), end='')
#        print('')
        
    width = len("{0:b}".format(n))
    for i in range(1,n+1):
        print("{0:{1}d} {0:{1}o} {0:{1}X} {0:{1}b}".format(i, width))