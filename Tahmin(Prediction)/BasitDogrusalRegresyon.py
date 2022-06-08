# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 11:46:29 2022

@author: Monster

"""
# ctrl+i bilgilendirme

import matplotlib.pyplot as plt
import numpy as np

import pandas as pd

veriler=pd.read_csv('satislar.csv')

print(veriler)
aylar=veriler[['Aylar']]
satis=veriler[['Satislar']]

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test =train_test_split(aylar,satis,test_size=0.33,random_state=0)
# =============================================================================
# 
# from sklearn.preprocessing import StandardScaler
# =============================================================================

# =============================================================================
# sc=StandardScaler() # verilerin ölçeklenmesi
# X_train=sc.fit_transform(x_train)
# X_test=sc.fit_transform(x_test)
# Y_train=sc.fit_transform(y_train)
# Y_test=sc.fit_transform(y_test)
# =============================================================================

# model inşası
from sklearn.linear_model import LinearRegression
# =============================================================================
# lr=LinearRegression() #y=ax+b
# lr.fit(X_train,Y_train)
# tahmin=lr.predict(X_test)  # Y_test tahmin
# =============================================================================


lr=LinearRegression()
lr.fit(x_train ,y_train)
tahmin=lr.predict(x_test)

x_train=x_train.sort_index()
y_train=y_train.sort_index()



plt.scatter(x_train, y_train)
plt.plot(x_train.values[:,0], y_train.values[:,0]) #DİZİ SEKLİNDE VERİ YÜKLE
plt.plot(x_test.values[:,0],lr.predict(x_test))
plt.title("aylara göre satıs")
plt.xlabel("aylar")
plt.ylabel("satislar")
plt.show()