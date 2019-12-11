#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 15:00:52 2019

@author: jsheldon
"""



sample_1='catcgtaatgacggcct'
sample_2='catcgtaatgacgiaaa'


#for a,b in [sample_1,sample_2]:
def difference(a,b):
    count = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        else:
            count += 1
    return count
"""
with open('rosalind_hamm.txt', 'r') as myfile:
    dta=myfile.read().rsplit('\n')
    print(dta)

print(difference(dta[0],dta[1])) 
"""