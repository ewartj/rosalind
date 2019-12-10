# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def count_dna(DNA):
    dna_lst = []
    A = DNA.count('A') or DNA.count('a')
    C = DNA.count('C') or DNA.count('c')
    G = DNA.count('G') or DNA.count('g')
    T = DNA.count('T') or DNA.count('t')
    dna_lst = {'A':A,'C':C,'G':G,'T':T}
    return dna_lst


