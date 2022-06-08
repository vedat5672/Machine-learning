# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 10:35:37 2022

@author: Monster
"""

import pandas as pd
import numpy as np




veriler=pd.read_csv('veriler.csv')
# Encoder kategorik-> Nominal Ordinal ->Numeric
ulke=veriler.iloc[:,0:1 ].values # tüm satırları al 0.sütün
print(ulke)
from sklearn import preprocessing
le=preprocessing.LabelEncoder() # sayıya dönüştür
ulke[:,0]=le.fit_transform(veriler.iloc[:,0])#tr 1 usa 2 fr 3
print(ulke)
ohe=preprocessing.OneHotEncoder() # kolon baslıklarını etikete tasımak verilere  0 1 ata
ulke=ohe.fit_transform(ulke).toarray() # 100 tr 010 fr 001 usa gibi tabloya dönüştürür.
print(ulke)
# numpy dizileri dataframe donusum
sonuc=pd.DataFrame(data=ulke,index=range(22),columns=['fr','tr','us'])
print(sonuc)
veriler2=pd.read_csv('veriler.csv')
yas=veriler.iloc[:,1:4].values

sonuc2=pd.DataFrame(data=yas,index=range(22),columns=['boy','kilo','yas'])
print(sonuc2)
cinsiyet=veriler.iloc[:,-1].values
print(cinsiyet)
sonuc3=pd.DataFrame(data=cinsiyet,index=range(22),columns=['cinsiyet'])
print(sonuc3)
# dataframe birleştir
s=pd.concat([sonuc,sonuc2]) # dikey birlestirmiş
s1=pd.concat([sonuc,sonuc2],axis=1) # esleme
s2=pd.concat([s1,sonuc3],axis=1) # esleme
print(s2)

# =============================================================================
# Veri Kümesinin Eğitim ve Test Olarak Bölünmesi
# =============================================================================

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test =train_test_split(s1,sonuc3,test_size=0.33,random_state=0)
 # concructor
# x bagımsız y bagımlı ulke boy kilo yasa göre cinsiyet tahmini
# 4 tane  veri kümemiz çıkmıs oluyor bagımlı degişken, 1 eğitmek için 2 test için
# bagımsız degıişen train anad test



# =============================================================================
# Öznitelik ve Ölçeklendirme
# =============================================================================

# verilerin standartlasması
from sklearn.preprocessing import StandardScaler

sc=StandardScaler() # verilerin ölçeklenmesi
X_train=sc.fit_transform(x_train)
X_test=sc.fit_transform(x_test)

# =============================================================================
# Veri On Isleme Sablonu
# =============================================================================
























