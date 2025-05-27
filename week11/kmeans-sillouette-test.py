# -*- coding: utf-8 -*-
"""
실루엣 계수 구하기 https://zephyrus1111.tistory.com/193
"""

# 필요한 라이브러리 임포트
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# 테스트 데이터셋 1: 중간 정도로 분리된 군집 (실루엣 계수 0.882)
X = np.array([[2, 3], [1, 3], [2, 2.5], [8, 3], [10, 3], [9, 4]]) # silhouette_coef => 0.8822250218687797
# 테스트 데이터셋 2: 가장 잘 분리된 군집 (실루엣 계수 0.913)
X = np.array([[2, 3], [1, 3], [2, 2.5], [12, 3], [11, 3], [12, 4]]) # silhouette_coef => 0.913370116740671
# 테스트 데이터셋 3: 덜 분리된 군집 (실루엣 계수 0.541)
X = np.array([[2, 3], [1, 3], [2, 2.5], [3, 3], [5, 3], [4, 4]]) # silhouette_coef => 0.5412807938829989
#X = np.array([[2, 3], [9, 3], [6, 3]])

# 데이터프레임 생성 및 시각화
data=pd.DataFrame(X, columns=['x', 'y'])
data.info()
data.plot(kind="scatter", x="x",y="y",figsize=(5,5),color="red")

# K-means 군집화 수행 (2개 군집)
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
labels = kmeans.labels_
centers=kmeans.cluster_centers_
print(centers)

# cluster center 시각화
plt.scatter(X[:,0],X[:,1], marker='o')    # 데이터 포인트
plt.scatter(centers[:,0], centers[:,1], marker='^')    # 군집 중심점
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# 군집별 색상 구분 시각화
fig = plt.figure(figsize=(7,7))
fig.set_facecolor('white')
for i, label in enumerate(labels):
    if label == 0:
        color = 'blue'    # 첫 번째 군집
    elif label ==1:
        color = 'red'     # 두 번째 군집
    else:
        color = 'green'
    plt.scatter(X[i,0],X[i,1], color=color)    
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()

# 실루엣 계수 계산 함수 
def get_silhouette_results(X, labels):
    def get_sum_distance(target_x, target_cluster):
        # 한 점과 클러스터 내 모든 점들 간의 거리 합 계산
        res = np.sum([np.linalg.norm(target_x-x) for x in target_cluster])
        return res
    
    '''
    각 데이터 포인트를 돌면서 a(i), b(i)를 계산
    그리고 s(i)를 계산한다.
    
    마지막으로 Silhouette(실루엣) Coefficient를 계산한다.
    '''
    uniq_labels = np.unique(labels)
    silhouette_val_list = []
    for i in range(len(labels)):
        target_data = X[i]

        ## calculate a(i): 같은 군집 내 평균 거리
        target_label = labels[i]
        target_cluster_data_idx = np.where(labels==target_label)[0]
        if len(target_cluster_data_idx) == 1:
            silhouette_val_list.append(0)
            continue
        else:
            target_cluster_data = X[target_cluster_data_idx]
            temp1 = get_sum_distance(target_data, target_cluster_data)
            a_i = temp1/(target_cluster_data.shape[0]-1)

        ## calculate b(i): 가장 가까운 다른 군집과의 평균 거리
        b_i_list = []
        label_list = uniq_labels[np.unique(labels) != target_label]
        for ll in label_list:
            other_cluster_data_idx = np.where(labels==ll)[0]
            other_cluster_data = X[other_cluster_data_idx]
            temp2 = get_sum_distance(target_data, other_cluster_data)
            temp_b_i = temp2/other_cluster_data.shape[0]
            b_i_list.append(temp_b_i)

        b_i = min(b_i_list)
        s_i = (b_i-a_i)/max(a_i, b_i)    # 실루엣 계수 계산
        silhouette_val_list.append(s_i)

    # 각 군집별 평균 실루엣 계수 계산
    silhouette_coef_list = []
    for ul in uniq_labels:
        temp3 = np.mean([s for s, l in zip(silhouette_val_list, labels) if l == ul])
        silhouette_coef_list.append(temp3)
    
    silhouette_coef = max(silhouette_coef_list) # silhouette_coef = max(silhouette_coef_list)
    return (silhouette_coef, np.array(silhouette_val_list))

# 실루엣 함수 테스트
silhouette_coef, silhouette_val_list = get_silhouette_results(X, labels)
print(silhouette_coef)

# 실루엣 함수 시각화
import seaborn as sns 
## 각 클러스터별로 Silhouette(실루엣) 값을 정렬한다.
uniq_labels = np.unique(labels)
sorted_cluster_svl = []
rearr_labels = []
for ul in uniq_labels:
    labels_idx = np.where(labels==ul)[0]
    target_svl = silhouette_val_list[labels_idx]
    sorted_cluster_svl += sorted(target_svl)
    rearr_labels += [ul]*len(target_svl)

colors = sns.color_palette('hls', len(uniq_labels))
color_labels = [colors[i] for i in rearr_labels]

fig = plt.figure(figsize=(6, 10))
fig.set_facecolor('white')
plt.barh(range(len(sorted_cluster_svl)), sorted_cluster_svl, color=color_labels)
plt.ylabel('Data Index')
plt.xlabel('Silhouette Value')
plt.show()

# sklearn의 실루엣 스코어와 비교
from sklearn.metrics import silhouette_score 
s=silhouette_score(X, labels, metric='euclidean')
print('silhouette_score=>', s)

# 직접구현한 함수의 평균값
#np.mean(silhouette_val_list)