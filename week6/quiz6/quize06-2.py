#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 17:01:07 2025

@author: kangchaewon
"""

import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# JSON 데이터를 DataFrame으로 변환
with open('/Users/kangchaewon/Documents/2025덕성여대_수업/빅데이터/week06-v2/output/china_visitors_2019_202412.json') as f:
    js = json.load(f)  # json.loads(f.read()) 도 되지만 json.load(f)로 간단히 가능

df = pd.DataFrame(js)  # 중복 선언 제거 (기존에 있던 "data"는 없어도 됨)

# yyyymm을 datetime 형식으로 바꿔서 정렬 (시각화 시 순서 문제 방지)
df['yyyymm'] = pd.to_datetime(df['yyyymm'], format='%Y%m')
df = df.sort_values('yyyymm')

# 그래프 그리기
plt.figure(figsize=(18, 6))  # 그래프 크기 조절
plt.bar(df['yyyymm'].dt.strftime('%Y-%m'), df['visit_cnt'], color='skyblue')

plt.title('중국인의 월별 한국 방문자 수 (2019~2024)', fontsize=16)
plt.xlabel('연도-월', fontsize=12)
plt.ylabel('방문자 수', fontsize=12)
plt.xticks(rotation=45, ha='right')  # x축 날짜 회전
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()
