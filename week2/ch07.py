#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 14:31:36 2025

@author: kangchaewon
"""

import pandas as pd
data = {
'apples': [3, 2, 0, 1],
'oranges': [0, 3, 7, 2]
}
purchases = pd.DataFrame(data)
purchases
purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])
purchases
col1=pd.Series([3, 2, 0, 1], name='apples')
col2=pd.Series([3, 2, 0, 1], name='oranges', index=['June', 'Robert', 'Lily', 'David'])
col1
col1.name
col1.values
col1.index
purchases2 = pd.DataFrame(col1)
purchases2
purchases3 = pd.DataFrame(col2)
purchases3
col2=pd.Series([3, 2, 0, 1], name='oranges')
purchases4= pd.concat([col1, col2], axis=1)
purchases4
purchases4.index=['June', 'Robert', 'Lily', 'David']
purchases4
#purchases4.name
purchases4.index
purchases4.columns