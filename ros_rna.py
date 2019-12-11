# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
os.chdir('/home/jsheldon/Downloads')
location = os.getcwd()
print(location)

with open('rosalind_revc.txt', 'r') as myfile:
    dta=myfile.read()

def RNA(DNA, standard):
    DNA_upper = DNA.upper()
    string = list(DNA_upper)
    transcript = {'A':'A', 'T':'U','C':'C','G':'G'}
    complimnet = {'A':'T', 'T':'A','C':'G','G':'C'}
# input('RNA or reverse compliment? ')
    if standard == 'R':
        for index, item in enumerate(string):
            for key, value in transcript.items():
                if item==key:
                    string[index]=value
        return ''.join(string)
    if standard == 'C':
        for index, item in enumerate(string):
            for key, value in complimnet.items():
                if item==key:
                    string[index]=value
        return ''.join(string[::-1])
    else:
        print('please specify standard')

#print(RNA(dta, 'R'))
print(RNA(dta, 'C'))