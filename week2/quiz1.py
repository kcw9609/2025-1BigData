#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 13:56:11 2025

@author: kangchaewon
1. 2개의 리스트를 읽어서 공통된 데이터가 있으면 True, 아니면 None을 반환하는 프로그램
을 작성하여라
"""

def common_data(list1, list2):
    for i in range(len(list2)):
        
        if list1.__contains__(list2[i]):
            return True;
        
    
    
    
print(common_data([1,2,3,4,5], [5,6,7,8,9])) # True
print(common_data([1,2,3,4,5], [6,7,8,9])) # False

def test(lst, str1):
    result = False
    str2 = str1.split('.'); print(str2)
    for x in lst:
        if x in str2:
            resutl=True
    return result

str1 = "https://www.jjj.com/python-eee/list/"
lst = ['.com', '.edu', '.tv']
print(test(lst, str1))

str1 = "https://www.jjj./python-eee/list/net"
lst = ['.com', '.edu', '.tv']
print(test(lst, str1))