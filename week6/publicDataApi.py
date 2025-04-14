#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 13:14:36 2025

@author: kangchaewon
"""

import requests

url = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'
params ={'serviceKey' : 'HtxRjgT1daVOawrGCF07kPNTVKPDRxQx4Kh8BYy4OdV8L+NPBJ/eRNTTIW67UP5mzEVCt5i0I28Ci/c/G0QnvA==', 'YM' : '201201', 'NAT_CD' : '112', 'ED_CD' : 'E' }

response = requests.get(url, params=params)
print(response.content)