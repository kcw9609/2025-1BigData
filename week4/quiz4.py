#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 09:57:11 2025

@author: kangchaewon
"""

'''
(2) 데이터 처리
csv 파일에서 17개 지역별 인구수를 읽어서 인구변동수를 계산한 후 배열에 저장한다.
인구수를 처리할 때 콤마(,)를 빼고 숫자로 계산한다. (replace 함수 사용)
(3) bar 차트를 그린다.(참고: https://python-graph-gallery.com/1-basic-barplot/ )
import matplotlib.pyplot as plt
plt.bar( )
plt.savefig( )
'''

import csv
import os
import matplotlib.pyplot as plt


print("현재 작업 디렉토리:", os.getcwd())  # 디버깅용

regions = []
diff_population = []

file2015 = open('201502population.csv', encoding='cp949')  # 혹은 경로 지정
file2025 = open('202502population.csv', encoding='cp949')  # 혹은 경로 지정
data_2015 = csv.reader(file2015)
data_2025 = csv.reader(file2025)
next(data_2015)  # 헤더 건너뛰기
next(data_2025)

home = []  # 입력 받은 지역의 데이터를 저장할 리스트


# 두 파일에서 각 줄을 동시에 읽어옴
for row_2015, row_2025 in zip(data_2015, data_2025):
    region_2015 = row_2015[0]
    region_2025 = row_2025[0]

    # 지역명이 같은지 확인
    if region_2015 != region_2025:
        print(f"지역 불일치: {region_2015} != {region_2025}")
        continue

    pop_2015 = int(row_2015[1].replace(',', ''))
    pop_2025 = int(row_2025[1].replace(',', ''))

    diff = pop_2025 - pop_2015  # 인구변동수 계산

    regions.append(region_2015)
    diff_population.append(diff)

file2015.close()
file2025.close()


# 바 차트 그리기
plt.figure(figsize=(12, 6))  # 그래프 크기 설정
plt.rc('font', family ='AppleGothic')
plt.bar(regions, diff_population, color='skyblue')
plt.xticks(rotation=90)  # 지역명이 겹치지 않도록 회전
plt.xlabel('지역')
plt.ylabel('인구 변화 (명)')
plt.title('2015년 대비 2025년 지역별 인구 변화')
plt.tight_layout()  # 레이아웃 자동 조절

# 그래프 이미지로 저장
plt.savefig('population_change_barplot.png')

# 화면에 보여주기 (선택사항)
plt.show()

# ---------


import pandas as pd
import matplotlib.pyplot as plt
import os

print("현재 작업 디렉토리:", os.getcwd())  # 디버깅용

# CSV 파일 불러오기
df_2015 = pd.read_csv('201502population.csv', encoding='cp949')
df_2025 = pd.read_csv('202502population.csv', encoding='cp949')

# 컬럼명 통일: '행정구역' 컬럼의 괄호 및 공백 제거
df_2015['행정구역'] = df_2015['행정구역'].str.extract(r'([\uAC00-\uD7A3]+)')  # 한글만 추출
df_2025['행정구역'] = df_2025['행정구역'].str.extract(r'([\uAC00-\uD7A3]+)')

# 인구수 숫자 변환 (콤마 제거 후 정수로 변환)
df_2015['총인구수'] = df_2015['2015년02월_총인구수'].str.replace(',', '').astype(int)
df_2025['총인구수'] = df_2025['2025년02월_총인구수'].str.replace(',', '').astype(int)

# 필요한 컬럼만 추출
df_2015 = df_2015[['행정구역', '총인구수']]
df_2025 = df_2025[['행정구역', '총인구수']]

# 데이터 병합
df = pd.merge(df_2015, df_2025, on='행정구역', suffixes=('_2015', '_2025'))

# 인구 변화량 계산
df['인구변화'] = df['총인구수_2025'] - df['총인구수_2015']

# 바 차트 그리기
plt.figure(figsize=(12, 6))
plt.rc('font', family='AppleGothic')  # Mac 기준, Windows는 'Malgun Gothic'
plt.bar(df['행정구역'], df['인구변화'], color='skyblue')
plt.xticks(rotation=90)
plt.xlabel('지역')
plt.ylabel('인구 변화 (명)')
plt.title('2015년 대비 2025년 지역별 인구 변화')
plt.tight_layout()

# 이미지 저장
plt.savefig('population_change_barplot.png')
plt.show()






