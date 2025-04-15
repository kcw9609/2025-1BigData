# Q5-1

 
    
    
####
# xls to csv
'''
import pandas as pd
# 엑셀 파일에서 'times' 시트만 바로 읽기
df = pd.read_excel("./transportation_card/2018-03.xls", sheet_name='지하철 시간대별 이용현황')
print(df)
print(df['승차'].dtype)  # int64나 float64라면 숫자형임
print(df['승차'].head())  # 천 단위 콤마 없이 그냥 숫자로 나올 것

df['승차'] = df['승차'].str.replace(',', '', regex=False).astype(int)

# CSV로 저장
df.to_csv('./transportation_card/201803.csv', index=False)
print(df)


xls = pd.read_excel("./transportation_card/2020-03.xls")
xls.to_csv("./transportation_card/202003.csv")

xls = pd.read_excel("./transportation_card/2025-03.xls")
xls.to_csv("./transportation_card/202503.csv")



df = pd.read_excel(excel_file, sheet_name=sheet_name)

print(xls)

# 콤마 제거

xls['
'] = df['금액'].str.replace(',', '', regex=False).astype(int)

###
'''

import csv
import matplotlib.pyplot as plt

def read_subway_data(filename):
    f = open(filename)
    data = csv.reader(f)
    next(data)  # 헤더 스킵
    next(data)
    s_in = [0] * 24
    s_out = [0] * 24
    for row in data:
        row[4:] = map(int, row[4:])
        for i in range(24):
            s_in[i] += row[4 + i * 2]     # 승차 인원
            s_out[i] += row[5 + i * 2]    # 하차 인원
    f.close()
    return s_in, s_out

# 각각의 CSV 파일에서 데이터 읽기
s_in_2018, s_out_2018 = read_subway_data('./transportation_card/201803.csv')
s_in_2020, s_out_2020 = read_subway_data('./transportation_card/202003.csv')
s_in_2025, s_out_2025 = read_subway_data('./transportation_card/202503.csv')

# 그래프 그리기
plt.figure(dpi=300)
plt.rc('font', family='AppleGothic')
plt.title('지하철 시간대별 승하차 인원 추이(단위 1000만명)')

plt.plot(s_in_2018, label='201803승차', linestyle='-', color='blue')
plt.plot(s_out_2018, label='201803하차', linestyle=':', color='orange')

plt.plot(s_in_2020, label='202003승차', linestyle='-', color='green')
plt.plot(s_out_2020, label='202003하차', linestyle=':', color='red')

plt.plot(s_in_2025, label='202503승차', linestyle='-', color='purple')
plt.plot(s_out_2025, label='202503하차', linestyle=':', color='brown')

plt.legend()
plt.xticks(range(24), range(4, 28))  # 4시 ~ 27시로 표시
plt.show()


###
    
# Q 5-2

# In[ ]: 6개

import numpy as np
import csv
#1. 데이터를 읽어온다.
f = open('age.csv', encoding='cp949')
data = csv.reader(f)
next(data)
data = list(data)
#2. 궁금한 지역의 이름을 입력받는다.
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
mn = 1 # 최솟값을 저장할 변수 생성 및 초기화
result_name = '' # 최솟값을 갖는 지역의 이름을 저장할 변수 생성 및 초기화
result = 0 # 최솟값을 갖는 지역의 연령대별 인구 비율을 저장할 배열 생성 및 초기화
home = []  #입력 받은 지역의 데이터를 저장할 리스트 생성
#3. 궁금한 지역의 인구 구조를 저장한다.
for row in data :
    if name in row[0]: #입력 받은 지역의 이름이 포함된 행 찾기
        areaname=row[0]
        for i in row[3:]: #3번 인덱스 값부터 슬라이싱 0세~
            home.append(int(i)) #입력 받은 지역의 데이터를 home에 저장
        hometotal=int(row[2])
for k in range(len(home)):
    home[k]=(home[k]/hometotal) # ➊
#4. 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역을 찾는다.
result_list=[]
for row in data : 
    away=[]
    for i in row[3:]: #3번 인덱스 값부터 슬라이싱 0세~
        away.append(int(i)) #입력 받은 지역의 데이터를 away에 저장
    awaytotal=int(row[2])
    for k in range(len(away)):
        away[k]=(away[k]/awaytotal)
    s=0
    for j in range(len(away)):
        s=s+(home[j]-away[j])**2
    result_list.append([row[0], away, s])
result_list.sort(key=lambda s: s[2]) # sum 값으로 정렬...

#5. 궁금한 지역의 인구 구조와 가장 비슷한 곳의 인구 구조를 시각화한다.
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.figure(figsize = (10,5), dpi=300)            
plt.rc('font', family ='AppleGothic')
plt.title(name +' 지역과 가장 비슷한 인구 구조를 가진 지역')
plt.plot(home, label = name)
for i in range(5):
    plt.plot(result_list[i+1][1], label = result_list[i+1][0])

plt.legend()
plt.show()


# Q 5-3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. 데이터 불러오기
df = pd.read_csv('age.csv', encoding='cp949')

# 2. 사용자로부터 지역 이름 입력받기
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')

# 3. 입력한 지역 데이터 추출 및 정규화
target_row = df[df.iloc[:, 0].str.contains(name)]

if target_row.empty:
    print(f"'{name}' 이름을 포함하는 지역이 없습니다.")
else:
    area_name = target_row.iloc[0, 0]
    population_total = int(target_row.iloc[0, 2])
    home = target_row.iloc[0, 3:].astype(int) / population_total

    # 4. 다른 지역과의 거리 계산
    results = []
    for idx, row in df.iterrows():
        comp_area_name = row[0]
        comp_total = int(row[2])
        comp_data = row[3:].astype(int) / comp_total

        ssd = np.sum((home - comp_data) ** 2)  # sum of squared differences
        results.append((comp_area_name, comp_data, ssd))

    # SSD 오름차순 정렬 (가장 비슷한 지역들 찾기)
    results.sort(key=lambda x: x[2])

    # 5. 시각화
    plt.style.use('ggplot')
    plt.figure(figsize=(10, 5), dpi=300)
    plt.rc('font', family='AppleGothic')
    plt.title(f"{area_name} 지역과 가장 비슷한 인구 구조를 가진 지역")

    plt.plot(home.values, label=area_name)  # 입력한 지역

    for i in range(5):  # 가장 비슷한 5개 지역
        comp_name, comp_data, _ = results[i + 1]  # 0번은 자기 자신
        plt.plot(comp_data.values, label=comp_name)

    plt.legend()
    plt.show()

    
    
    