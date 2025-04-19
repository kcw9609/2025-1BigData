#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 14:21:57 2025

@author: kangchaewon
"""
import regex

def test(lst, str1):
    result = False
    # st1 = st1.replace('/', '.');
    # str2 = str1.split('.');
    # str2 = str2.split('/'); 
    str2 = regex.split('[./]', str1)
    print(str2)
    for x in lst:
        if x in str2:
            result=True
    return result

str1 = "https://www.jjj.com/python-eee/list/"
lst = ['com', 'edu', 'tv']
print(test(lst, str1))

str1 = "https://www.jjj./python-eee/list/net"
lst = ['com', 'edu', 'tv']
print(test(lst, str1))