#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:55:30 2019

@author: jsheldon
"""


def line_skip(fle):
    lines = []
    with open(fle, 'r') as f:
        for count, line in enumerate(f, start=1):
            if count % 2 == 0:
                lines.append(line)
        return lines
            

fle = 'rosalind_ini5.txt'
strng = line_skip(fle)  
strng = '\n'.join(map(str, strng)) 
print(strng) 