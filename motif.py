#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 15:06:23 2019

@author: jsheldon
"""
import regex as re

def start_seq(q,motif):
    start_loc = []
    for i in re.finditer(motif,q, overlapped=True):
        start_loc.append(i.start()+1)
    return start_loc

with open('rosalind_subs.txt', 'r') as myfile:
    dta=myfile.read().rsplit('\n')
    
print(' '.join(map(str, start_seq(dta[0],dta[1]))))