#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 14:50:52 2019

@author: jsheldon
"""


def fibonachi_rab(time, litter):
    n1, n2 = 1, 1
    fn = 1
    for i in range(2, time):
        fn = n1 + n2 * litter
        n2, n1 = n1, fn
    return fn 

"""
This was needed for origional challenge but not for subsequent use 

with open('rosalind_fib.txt', 'r') as myfile:
    dta=myfile.read().replace("\n", "").split(' ')
    print(dta)
       
    
print(fibonachi_rab(int(dta[0]),int(dta[1])))
"""
