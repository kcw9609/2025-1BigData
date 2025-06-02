#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 14:14:03 2025

@author: kangchaewon
"""

import pandas as pd
data=pd.read_csv("mtcars.csv")
print (data)
dir (pd)
pd.read_csv._doc_
print (pd.read_csv._doc_)
print(pd.DataFrame.head._
.doc_)
dir(pd.DataFrame) ###
print(data.head( ))
print(data. shape)
print(type(data))
print(data.columns); print(type(data.columns) )
print (data. describe()) # data. info()
print (data[ 'hp']. describe())
print(data[' gear']. unique ( ))
print(data[' cyl']. unique ( ))
print(data.info())
print(data.corr())
X=data.drop(columns= 'mpg')
Y=data[ 'mpg']