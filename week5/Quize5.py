# Q5-1

import pandas as pd
import matplotlib.pyplot as plt

def get_total_ridership(file_path):
    df = pd.read_excel(file_path)

    # 쉼표 제거 및 정수형 변환
    df['승차승객수'] = df['승차승객수'].astype(str).str.replace(',', '').astype(int)

    if '승차승객수' in df.columns:
        total_ridership = df['승차승객수'].sum()
        return total_ridership  # 이미 int형
    else:
        print(f"Error: '승차승객수' column not found in {file_path}")


# Specify the paths to your three Excel files
file_path_2018 = './transportation_card/2018-03.xls'
file_path_2020 = './transportation_card/2020-03.xls'
file_path_2025 = './transportation_card/2025-03.xls'

# Get the total ridership for each month
ridership_2018 = get_total_ridership(file_path_2018)
ridership_2020 = get_total_ridership(file_path_2020)
ridership_2025 = get_total_ridership(file_path_2025)

# Prepare data for plotting
years = ['2018-03', '2020-03', '2025-03']
ridership = [ridership_2018, ridership_2020, ridership_2025]

# Filter out months with missing data
years_filtered = [year for i, year in enumerate(years) if ridership[i] is not None]
ridership_filtered = [r for r in ridership if r is not None]

# Create the line graph
if years_filtered:
    plt.figure(figsize=(10, 6))
    plt.plot(years_filtered, ridership_filtered, marker='o', linestyle='-', color='skyblue')
    plt.xlabel('Year-Month')
    plt.ylabel('Subway Ridership')
    plt.title('Seoul Subway Ridership Comparison (Pre-COVID and Present)')
    plt.xticks(years_filtered)
    plt.grid(axis='y', linestyle='--')
    plt.tight_layout()
    plt.show()
else:
    print("Error: Could not retrieve ridership data from the files.")
    
    
    
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

    
    
    