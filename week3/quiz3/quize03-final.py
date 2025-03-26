#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 13:33:39 2025

@author: kangchaewon
"""

import numpy as np
import pandas as pd

## 질의 3-1
emp = pd.read_csv('emp.csv')

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

# 3-4
emp[['ENAME', 'SAL']]
emp['ENAME', 'SAL'] # 이렇게 하면 안됨. emp[]는 하나의 행을 가져오는 문법이기 때문
emp.loc[:,['ENAME', 'SAL']]
emp.iloc[:,[1,5]]

emp.loc[0:13,['ENAME', 'SAL']]
emp.iloc[0:13,['ENAME', 'SAL']] # xxx이렇게 하면 안됨
emp.iloc[0:14, [1,5]]

# 3-5
emp['JOB']
emp['JOB'].unique()
emp['JOB'].drop_duplicates() # 시리즈
# 3-6
[질의 3-6] SELECT * FROM Emp WHERE sal < 2000;
emp.loc[emp['SAL'] < 2000, :]

[질의 3-7] SELECT * FROM Emp WHERE sal BETWEEN 1000 AND 2000;
emp.loc[(emp['SAL'] >= 1000) & (emp['SAL'] <= 2000), :]

[질의 3-8] SELECT * FROM Emp WHERE sal >= 1500 AND job= ‘SALESMAN’;
emp.loc[(emp['SAL'] >= 1500) & (emp['JOB'] == 'SALESMAN'), :]

[질의 3-9] SELECT * FROM Emp WHERE job IN ('MANAGER', 'CLERK');
emp.loc[(emp['JOB'] == 'MANAGER') | (emp['JOB'] == 'CLERK'), :]\
[질의 3-10] SELECT * FROM Emp WHERE job NOT IN ('MANAGER', 'CLERK');
emp.loc[(emp['JOB'] != 'MANAGER') & (emp['JOB'] != 'CLERK')]

[질의 3-11] SELECT ename, job FROM Emp WHERE ename LIKE 'BLAKE';
emp.loc[(emp['ENAME'] == 'BLAKE'), ['JOB', 'ENAME']]

[질의 3-12] SELECT ename, job FROM Emp WHERE ename LIKE '%AR%';
emp.loc[emp['ENAME'].str.contains('AR'), ['ENAME', 'JOB']]

[질의 3-13] SELECT * FROM Emp WHERE ename LIKE '%AR%' AND sal >= 2000;
emp.loc[ ( emp['ENAME'].str.contains('AR') ) & ( emp['SAL'] >= 2000 ), :]

[질의 3-14] SELECT * FROM Emp ORDER BY ename;
emp.sort_values(by='ENAME')

[질의 3-15] SELECT SUM(sal) FROM Emp;
emp['SAL'].sum()

[질의 3-16] SELECT SUM(sal) FROM Emp WHERE job LIKE 'SALESMAN';
emp.loc[ emp['JOB'] == 'SALESMAN' , 'SAL' ].sum()

[질의 3-17] SELECT SUM(sal), AVG(sal), MIN(sal), MAX(sal) FROM Emp;
'''

emp['SAL'].sum()
emp['SAL'].AVG()
emp['SAL'].MIN()
emp['SAL'].MAX()

'''
# 한번에 출력
emp['SAL'].agg([ 'sum', 'mean', 'min', 'max'] )

[질의 3-18] SELECT COUNT(*) FROM Emp;
emp.count() # xxx : 각 열에서 nan이 아닌 개수 나타냄
len(emp)
emp.shape[0]

[질의 3-19] SELECT COUNT(*), SUM(sal) FROM Emp GROUP BY job;
emp.groupby('JOB').agg( count_sal = ('SAL', 'count'), sum_sal = ('SAL', 'sum'))

[질의 3-20] SELECT * FROM Emp WHERE comm IS NOT NULL;
emp.dropna()  
        
        
        
        
        
        
        
        
        
        
        