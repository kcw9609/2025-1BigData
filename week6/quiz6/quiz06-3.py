#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 17:14:01 2025

@author: kangchaewon
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# 기상청 관측 자료 페이지 URL
url = 'https://www.weather.go.kr/w/obs-climate/land/city-obs.do'

# 웹 페이지 요청
response = requests.get(url)
response.encoding = 'utf-8'  # 인코딩 설정

# HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 테이블 선택
table = soup.find('table', {'class': 'table-col'})

# 테이블에서 행 추출
rows = table.find_all('tr')[1:]  # 헤더를 제외한 데이터 행

# 데이터 저장을 위한 리스트
data = []

# 각 행에서 데이터 추출
for row in rows:
    cols = row.find_all('td')
    if len(cols) >= 7:
        region = row.find('th').get_text(strip=True)  # 지역 이름 추출
        temp = cols[5].get_text(strip=True)
        humidity = cols[6].get_text(strip=True)
        data.append([region, temp, humidity])

# 데이터프레임 생성
df = pd.DataFrame(data, columns=['sido-gu', '온도', '습도'])

# 데이터프레임 출력
print(df)
