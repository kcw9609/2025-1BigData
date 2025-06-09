#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
X_train = pd.read_csv("XX_train.csv")
Y_train = pd.read_csv("YY_train.csv")
X_test = pd.read_csv("X_test.csv")
X_train.info()

# encoding
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
X_train['Warehouse_block'] = le.fit_transform(X_train['Warehouse_block'])
X_test['Warehouse_block'] = le.fit_transform(X_test['Warehouse_block'])

X_train['Mode_of_Shipment'] = le.fit_transform(X_train['Mode_of_Shipment'])
X_test['Mode_of_Shipment'] = le.fit_transform(X_test['Mode_of_Shipment'])

X_train['Product_importance'] = le.fit_transform(X_train['Product_importance'])
X_test['Product_importance'] = le.fit_transform(X_test['Product_importance'])

X_train['Gender'] = le.fit_transform(X_train['Gender'])
X_test['Gender'] = le.fit_transform(X_test['Gender'])


# train-test 검증 데이터 분리 20%
from sklearn.model_selection import train_test_split
X_train, X_val, Y_train, Y_val = train_test_split(X_train, Y_train, test_size=0.2, random_state=42)
# 분석에 필요하지 않은 컬럼 제거

# 라벨 인코딩 - 명목형 변수

# minmaxscaling

# 모델 생성1(RandomForest)
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train['Target']) # y는 시리즈 줘야함

# # 모델 성능 평가
from sklearn.metrics import roc_auc_score
pred1=model.predict(X_val)
roc_auc=roc_auc_score(Y_val['Target'], pred1) # 정확도
print(roc_auc)
# 제출 dp -> csv
pred=model.predict(X_test)
submit=pd.DataFrame({'ID': X_test['ID'], 'Predicted':pred})
submit.to_csv('submission2.csv', index=False)
