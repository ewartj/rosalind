# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
os.chdir('/home/jsheldon/Downloads')
location = os.getcwd()
print(location)

with open('rosalind_dna.txt', 'r') as myfile:
    data=myfile.read()

def count_dna(DNA):
    dna_lst = []
    A = DNA.count('A') or DNA.count('a')
    C = DNA.count('C') or DNA.count('c')
    G = DNA.count('G') or DNA.count('g')
    T = DNA.count('T') or DNA.count('t')
    dna_lst = (A,C,G,T)
    return ' '.join(map(str, dna_lst))


#data = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

count_dna(data)
