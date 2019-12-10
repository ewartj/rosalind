#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:55:30 2019

@author: jsheldon
"""


def line_skip(data):
    lines = []
    with open(data, 'r') as f:
        for count, line in enumerate(f, start=1):
            if count % 2 == 0:
                line = line.strip()
                lines.append(line)
        return lines
            

#data = 'rosalind_rna.txt'
#strng = line_skip(data)  
#strng = '\n'.join(map(str, strng)) 
#print(strng) 