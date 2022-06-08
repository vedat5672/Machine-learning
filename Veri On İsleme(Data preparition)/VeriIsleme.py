# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 09:30:02 2022

@author: Monster
"""
#import
#ders-6 kütüphanelerin yüklenmesi
#kütüphaneler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Kod Bölümü
# =============================================================================
# veri = pd.read_csv('veriler.csv')
# print(veri)
# boy=veri[['boy']]
# print(boy)
# boyUlke=veri[['boy','ulke']]
# print(boyUlke)
# x=10
# =============================================================================

#eksik veriler
# eksik verilerin yerine ortalama deger atanmıs
veri1=pd.read_csv('eksikveriler.csv')

from sklearn.impute  import SimpleImputer
imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
# missing_values:int=0, float, str, np.nan, None or pandas.NA, default=np.nan
# STRATEGY
# =============================================================================
# strategystr, default=’mean’
# The imputation strategy.
# 
# mean= eksik veriyi ortalama deger ile değiştir
# 
# median=eksik veriyi medyam deger ile değiştir
# 
# most_frequent = eksik veriyi en çok kullanılan veriyle değiştir
# constant=  sabit deger ata eksik veri yerine
# =============================================================================
print(veri1)
yas=veri1.iloc[:,1:4 ].values # tablodan deger alma
print(yas)
imputer=imputer.fit(yas[:,1:4]) # Makine ögrenmesi ögremdiği
yas[:,1:4]=imputer.transform(yas[:,1:4]) # Makine ögrenmesi uygulanması
print(yas)





































