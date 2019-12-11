#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:53:46 2019

@author: jsheldon
"""


import os
import numpy as np
import pandas as pd
os.chdir('/home/jsheldon/Downloads')
location = os.getcwd()
print(location)

from skip_line import line_skip


dna = line_skip('rosalind_rna.txt')



    
matrix = []
A = []
C = []
G = []
T = []
    
for i in dna:
    matrix.append([j for j in i]) 
M = np.array(matrix).reshape(len(matrix),len(matrix[0]))
print(M[:,1])
for i in range(len(matrix[0]))  :
    A_count = 0
    T_count = 0
    G_count = 0
    C_count = 0
    for j in M[:,i]:
        if j == "A":
            A_count += 1
        elif j == "C":
            C_count += 1
        elif j == "G":
            G_count += 1
        elif j == "T":
            T_count += 1 
    A.append(A_count)
    C.append(C_count)
    G.append(G_count)
    T.append(T_count) 

profile_matrix = {"A": A, "C": C, "G": G, "T": T}
print(profile_matrix)   

consensus = pd.DataFrame.from_dict(profile_matrix)    
print(consensus)    

for k, v in profile_matrix.items:
    print(k + ":"  + "".join(str(x) for x in v))
