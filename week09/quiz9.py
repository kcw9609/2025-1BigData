# Q9-1
# -*- coding: utf-8 -*-
"""
Created on Sun May 18 13:09:01 2025

@author: kangchaewon
"""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 데이터 입력
X = np.array([59, 49, 75, 54, 78, 56, 60, 82, 69, 83, 88, 94, 47, 65, 89, 70]).reshape(-1, 1)
Y = np.array([209, 180, 195, 192, 215, 197, 208, 189, 213, 201, 214, 212, 205, 186, 200, 204])

# 회귀모델 생성 및 훈련
model = LinearRegression()
model.fit(X, Y)

# 회귀계수 및 절편 출력
alpha = model.intercept_
beta = model.coef_[0]
print(f"(1) 회귀분석식: Y = {alpha:.2f} + {beta:.3f} * X")

# R^2 계산
r_squared = model.score(X, Y)
print(f"(2) 결정계수 R^2: {r_squared:.3f}")

# X=58일 때 Y 예측
X_new = np.array([[58]])
Y_pred = model.predict(X_new)
print(f"(3) X=58일 때 예측된 Y값: {Y_pred[0]:.2f}")


# Q9-2

from sklearn import linear_model, datasets
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import pandas as pd

# 데이터 불러오기
'''
속성 수 (features): 10개
예: age, sex, BMI, blood pressure, S1 ~ S6 (혈청 측정값 등)

데이터 개수 (샘플 수): 442개

타겟값 (target): 당뇨병 진행도 지표 (연속값)

'''
diabetes_data = datasets.load_diabetes()
print(diabetes_data.DESCR)
X = pd.DataFrame(diabetes_data.data)
y = diabetes_data.target

# train/test 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 회귀 모델 훈련
linear_regression = linear_model.LinearRegression()
linear_regression.fit(X_train, y_train)

# 예측
prediction = linear_regression.predict(X_test)

# 회귀 계수 및 절편 출력
print('a value (intercept_) =', linear_regression.intercept_)
print('b value (coefficients) =', linear_regression.coef_)

# 평가 지표 계산
r_squared = r2_score(y_test, prediction)
print('R_squared (test data) =', r_squared)
print('score (model.score) =', linear_regression.score(X_test, y_test))
print('Mean Squared Error =', mean_squared_error(y_test, prediction))
print('RMSE =', mean_squared_error(y_test, prediction)**0.5)
