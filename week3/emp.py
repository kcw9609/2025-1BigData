#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 13:33:39 2025

@author: kangchaewon
"""

import numpy as np
import pandas as pd

## 질의 3-1
pd.read_csv('emp.csv')

# 질의 3-2
print(emp)
emp
emp[:]
emp[:][:]

emp.loc[:]
emp.loc[:,:]

emp.iloc[:]
emp.iloc[:,:]


# 3-3

emp.ENAME # csv파일에 ENAME로 정의되어있음
emp['ENAME']
emp.loc[:, 'ENAME']
emp.loc[:]['ENAME']
