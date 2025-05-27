# -*- coding: utf-8 -*-
"""
실루엣 계수 구하기 https://zephyrus1111.tistory.com/193
실루엣 계수: 군집화의 품질을 평가하는 지표 (-1 ~ 1)
- 1에 가까울수록: 잘 된 군집화
- 0에 가까울수록: 군집 경계가 모호
- -1에 가까울수록: 잘못된 군집화
"""

# [필수 라이브러리]
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from sklearn.cluster import KMeans
 
# [시험포인트 1] 데이터 생성
np.random.seed(100)    # 재현성을 위한 시드 설정
num_data = 50          # 데이터 포인트 50개 생성
 
# 세 구간으로 나누어진 x값 생성 (군집이 잘 구분되도록)
x11 = np.linspace(0.3,0.7,20)   # 첫 번째 구간: 20개 점
x12 = np.linspace(1.3,1.8,15)   # 두 번째 구간: 15개 점
x13 = np.linspace(2.4,3,15)     # 세 번째 구간: 15개 점
x1 = np.concatenate((x11,x12,x13),axis=None)  # x값들을 하나로 합침

# y값 생성: y = 1.5x + 2 + 오차(노이즈)
error = np.random.normal(1,0.5,num_data)  # 평균 1, 표준편차 0.5인 정규분포 노이즈
x2 = 1.5*x1+2+error   # 선형관계에 노이즈를 추가

# [시험포인트 2] 원본 데이터 시각화
fig = plt.figure(figsize=(7,7))
fig.set_facecolor('white')
plt.scatter(x1, x2, color='k')   # 검은색 점으로 표시
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()

# [시험포인트 3] K-means 군집화 수행
X = np.stack([x1, x2], axis=1)   # 입력 데이터 형태로 변환
init = np.array([[2., 4.], [1., 5.], [2.5, 6.]])  # 초기 중심점 직접 지정
 
kmeans = KMeans(n_clusters=3, init=init)  # 3개 군집, 지정한 초기점으로 시작
kmeans.fit(X)   # 군집화 수행
labels = kmeans.labels_   # 각 점의 군집 레이블

# [시험포인트 4] 군집화 결과 시각화
fig = plt.figure(figsize=(7,7))
fig.set_facecolor('white')
for i, label in enumerate(labels):
    if label == 0:
        color = 'blue'     # 첫 번째 군집: 파란색
    elif label ==1:
        color = 'red'      # 두 번째 군집: 빨간색
    else:
        color = 'green'    # 세 번째 군집: 초록색
    plt.scatter(X[i,0],X[i,1], color=color)    
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()

# [매우 중요!] 실루엣 계수 계산 함수 
def get_silhouette_results(X, labels):
    # 한 점과 클러스터 내 모든 점들 간의 거리 합 계산
    def get_sum_distance(target_x, target_cluster):
        res = np.sum([np.linalg.norm(target_x-x) for x in target_cluster])
        return res
    
    '''
    실루엣 계수 계산 과정:
    1. a(i): 한 점과 같은 군집 내 다른 점들과의 평균 거리
    2. b(i): 한 점과 가장 가까운 다른 군집까지의 평균 거리
    3. s(i): 실루엣 계수 = (b(i) - a(i)) / max(a(i), b(i))
    '''
    uniq_labels = np.unique(labels)  # 고유한 군집 레이블 추출
    silhouette_val_list = []  # 각 점의 실루엣 값을 저장할 리스트
    
    # 각 데이터 포인트에 대해 실루엣 계수 계산
    for i in range(len(labels)):
        target_data = X[i]  # 현재 데이터 포인트
 
        # 1단계: a(i) 계산 - 같은 군집 내 평균 거리
        target_label = labels[i]
        target_cluster_data_idx = np.where(labels==target_label)[0]
        if len(target_cluster_data_idx) == 1:  # 군집에 점이 하나뿐이면
            silhouette_val_list.append(0)
            continue
        else:
            target_cluster_data = X[target_cluster_data_idx]
            temp1 = get_sum_distance(target_data, target_cluster_data)
            a_i = temp1/(target_cluster_data.shape[0]-1)
 
        # 2단계: b(i) 계산 - 가장 가까운 다른 군집과의 평균 거리
        b_i_list = []
        label_list = uniq_labels[np.unique(labels) != target_label]
        for ll in label_list:
            other_cluster_data_idx = np.where(labels==ll)[0]
            other_cluster_data = X[other_cluster_data_idx]
            temp2 = get_sum_distance(target_data, other_cluster_data)
            temp_b_i = temp2/other_cluster_data.shape[0]
            b_i_list.append(temp_b_i)
 
        # 3단계: 실루엣 계수 계산
        b_i = min(b_i_list)  # 가장 가까운 군집과의 거리
        s_i = (b_i-a_i)/max(a_i, b_i)  # 실루엣 계수 공식
        silhouette_val_list.append(s_i)
 
    # 각 군집별 평균 실루엣 계수 계산
    silhouette_coef_list = []
    for ul in uniq_labels:
        temp3 = np.mean([s for s, l in zip(silhouette_val_list, labels) if l == ul])
        silhouette_coef_list.append(temp3)
 
    silhouette_coef = max(silhouette_coef_list)  # 최대 실루엣 계수 반환
    return (silhouette_coef, np.array(silhouette_val_list))

# [시험포인트 5] 실루엣 계수 계산 및 출력
silhouette_coef, silhouette_val_list = get_silhouette_results(X, labels)
print(silhouette_coef)  # 전체 실루엣 계수 출력

# [시험포인트 6] 실루엣 시각화
import seaborn as sns 
# 각 군집별로 실루엣 값을 정렬하여 시각화 준비
uniq_labels = np.unique(labels)
sorted_cluster_svl = []  # 정렬된 실루엣 값 저장
rearr_labels = []       # 재배열된 레이블 저장
for ul in uniq_labels:
    labels_idx = np.where(labels==ul)[0]
    target_svl = silhouette_val_list[labels_idx]
    sorted_cluster_svl += sorted(target_svl)  # 실루엣 값 정렬
    rearr_labels += [ul]*len(target_svl)     # 레이블 재배열
 
# 시각화를 위한 색상 설정
colors = sns.color_palette('hls', len(uniq_labels))
color_labels = [colors[i] for i in rearr_labels]
 
# 실루엣 플롯 생성
fig = plt.figure(figsize=(6, 10))
fig.set_facecolor('white')
plt.barh(range(len(sorted_cluster_svl)), sorted_cluster_svl, color=color_labels)
plt.ylabel('Data Index')
plt.xlabel('Silhouette Value')
plt.show()

# [비교 포인트] sklearn의 실루엣 스코어와 비교
from sklearn.metrics import silhouette_score 
s=silhouette_score(X, labels, metric='euclidean')
print(s)

# 직접 구현한 함수의 평균값과 비교
np.mean(silhouette_val_list)