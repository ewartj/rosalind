# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
os.chdir('/home/jsheldon/Downloads')
location = os.getcwd()
print(location)

with open('rosalind_ini6.txt', 'r') as myfile:
    data=myfile.readlines()

word_dict = {}

def word_count(data):
    string = ' '.join(map(str, data))
    word_string = string.split()
    for item in word_string:
        if item in word_dict:
            word_dict[item] += 1
        else:
            word_dict[item] = 1
    with open('dictionary.txt', 'w') as f:
        for key, value in word_dict.items():
            f.write('%s %s\n' % (key, value))



word_count(data)
