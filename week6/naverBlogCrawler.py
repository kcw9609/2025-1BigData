#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 12:31:42 2025

@author: kangchaewon
"""

import os
import sys
import urllib.request
client_id = "Tng_FRjJ2uL56t5q1Xkw"
client_secret = "GSPZ5QOdaW"
encText = urllib.parse.quote("마크 컴백")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    myresult = response_body.decode('utf-8')
    print(myresult)
else:
    print("Error Code:" + rescode)
