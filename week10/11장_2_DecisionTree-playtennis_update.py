#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 22 15:25:22 2025

@author: kangchaewon
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, classification_report
from sklearn import tree

# 1. 데이터 로드
tennis_data = pd.read_csv('playtennis.csv')

# 2. Label 인코딩 (map 사용)
tennis_data['Outlook'] = tennis_data['Outlook'].map({'Sunny': 0, 'Overcast': 1, 'Rain': 2})
tennis_data['Temperature'] = tennis_data['Temperature'].map({'Hot': 0, 'Mild': 1, 'Cool': 2})
tennis_data['Humidity'] = tennis_data['Humidity'].map({'High': 0, 'Normal': 1})
tennis_data['Wind'] = tennis_data['Wind'].map({'Weak': 0, 'Strong': 1})
tennis_data['PlayTennis'] = tennis_data['PlayTennis'].map({'No': 0, 'Yes': 1})

# 3. Feature/Label 나누기
X = tennis_data[['Outlook', 'Temperature', 'Humidity', 'Wind']].values
y = tennis_data['PlayTennis'].values  # 1차원으로

# 4. Train/Test 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

# 5. 모델 학습
dt_clf = DecisionTreeClassifier(criterion='entropy', random_state=42)
dt_clf.fit(X_train, y_train)

# 6. 예측 및 평가
y_pred = dt_clf.predict(X_test)
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 7. 트리 시각화
plt.figure(figsize=(20, 10))
plot_tree(dt_clf, 
          feature_names=['Outlook', 'Temperature', 'Humidity', 'Wind'],
          class_names=['No', 'Yes'],
          filled=True)
plt.show()

# 8. Graphviz 시각화용 dot data 생성 (pydotplus 사용 가능)
dot_data = tree.export_graphviz(
    dt_clf,
    out_file=None,
    feature_names=['Outlook', 'Temperature', 'Humidity', 'Wind'],
    class_names=['No', 'Yes'],
    filled=True, rounded=True, special_characters=True
)

# 아래 코드 주석 해제하면 pydotplus 이미지 출력 가능
# import pydotplus
# from IPython.display import Image
# graph = pydotplus.graph_from_dot_data(dot_data)
# Image(graph.create_png())
from sklearn.metrics import accuracy_score

# 예측
y_pred = dt_clf.predict(X_test)

# 정확도 계산
accuracy = accuracy_score(y_test, y_pred)

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("Accuracy:", accuracy)
