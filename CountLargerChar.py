# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 22:05:37 2020

@author: andya
"""

from string import ascii_lowercase
def solve(n, string):
    
    alphabet_dict = dict()
    answer = []
    
    
    largest_char = max(string)
    for char in string:
        if char not in alphabet_dict:
            alphabet_dict[char] = sum([1 for x in string if x > char])
        
        answer.append(str(alphabet_dict[char]))
    
    result = ' '.join(answer)
    # Write your code here
    return print(result)

n = 8
string = 'aaabbbcd'
solve(n, string)
