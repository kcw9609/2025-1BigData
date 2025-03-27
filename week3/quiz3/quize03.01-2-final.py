#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 16:55:07 2025

@author: kangchaewon
"""

import numpy as np
import pandas as pd

'''
loc[]를 사용하면 원본 데이터를 직접 수정
그 외의 함수 사용시에는 emp = 을 사용하여 저장해야함
-> drop, rename, sort_values, 
inplace=True옵션을 주면 직접 수정됨
'''
## 질의 4.0
emp = pd.read_csv('emp.csv')


[질의 4-0] emp.csv를 읽어서 DataFrame emp 만들기
emp = pd.read_csv('emp.csv')

[질의 4-1] emp에 age 열을 만들어 다음을 입력하여라(14명)
emp = emp.loc[:, 'AGE'] = [30,40,50,30,40,50,30,40,50,30,40,50,30,40]
print(emp)

[질의 4-2] INSERT INTO Emp(empno, ename, job) Values (9999, ‘ALLEN’, ‘SALESMAN’)
emp.loc[len(emp), ['EMPNO', 'ENAME', 'JOB']] = [9999, 'ALLEN', 'SALESMAN']

[질의 4-3] emp의 ename=‘ALLEN’ 행을 삭제하여라
(DELETE FROM emp WHERE ename LIKE ‘ALLEN’;)
emp = emp.loc[emp['ENAME'] != 'ALLEN', :]

[질의 4-4] emp의 hiredate 열을 삭제하여라
(ALTER TABLE emp DROP COLUMN hiredate;)
emp = emp.drop('HIREDATE', axis=1) # emp = 으로 저장해야
emp.drop('HIREDATE', axis=1 , inplace=True) # inplace=True로 저장도 같이


[질의 4-5] emp의 ename=‘SCOTT’의 sal을 3000으로 변경하여라
(UPDATE emp SET sal=3000 WHERE ename LIKE ‘SCOTT’;
emp.loc[emp['ENAME'] == 'SCOTT' , 'SAL'] = 3000

[질의 5-1] emp의 sal 컬럼을 oldsal 이름으로 변경하여라.
(ALTER TABLE emp RENAME sal TO oldsal;)
emp = emp.rename(columns = {'SAL' : 'OLDSAL'})
emp.rename(columns = {'SAL' : 'OLDSAL'}, inplace = True)

[질의 5-2] emp에 newsal 컬럼을 추가하여라, 값은 oldsal 컬럼값
(ALTER TABLE emp ADD newsal …;)
emp['NEWSAL'] = emp['OLDSAL']

[질의 5-3] emp의 oldsal 컬럼을 삭제하여라
(ALTER TABLE emp DROP COLUMN oldsal;)
emp = emp.drop('OLDSAL', axis = 1)
emp.drop('OLDSAL', axis = 1, inplace = True)
