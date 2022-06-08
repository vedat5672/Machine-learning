# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 17:49:44 2022

@author: Monster
"""

import pandas as pd

titanic=pd.read_csv("titanic.csv")
ortalama=titanic["Age"].mean() #ortalama
print("ortalama yas {}".format(ortalama))
median=titanic[["Age", "Fare"]].median()
print(format(median))
acıklama=titanic[["Age", "Fare"]].describe()
print(acıklama)
# =============================================================================
# Önceden tanımlanmış istatistikler yerine, belirli sütunlar için toplama istatistiklerinin1
# belirli kombinasyonları veri çerçevesi kullanılarak tanımlanabilir.agg() yöntemi:
# =============================================================================
agg=titanic.agg(
    {
        "Age": ["min", "max", "median", "skew"],
        "Fare": ["min", "max", "median", "mean"],
    }
)
print(agg)
# =============================================================================
# Kategoriye göre gruplandırılmış istatistikleri toplama
# Erkek ve kadın Titanik yolcuların yaş ortalaması nedir?
# =============================================================================
categorySex=titanic[["Sex", "Age"]].groupby("Sex").mean()
print(categorySex)
# =============================================================================
# Bir sütundaki her kategori için belirli bir istatistiğin (örneğin ortalama yaş) hesaplanması (örneğin Cinsiyet sütunundaki erkek / kadın) 
#
#ortak bir modeldir. Groupby yöntemi bu tür işlemleri desteklemek için kullanılır. Daha genel olarak, bu daha genel split-apply-combine desenine uyar:
# 
# Verileri gruplara ayırma split
# 
# Her gruba bağımsız olarak bir işlev uygulama apply
# 
# Sonuçları bir veri yapısında birleştirin combine
# 
# Uygula ve birleştir adımları genellikle pandalarda birlikte yapılır.
# 
# Önceki örnekte, önce 2 sütunu açıkça seçtik. Değilse, sayısal sütunlar içeren her sütuna ortalama yöntemi uygulanır:
# =============================================================================

bycinsiyet=titanic.groupby("Sex").mean()
print(bycinsiyet)

# =============================================================================
# Pclass'ın ortalama değerini elde etmek pek mantıklı değil. yalnızca her cinsiyet için ortalama yaşla
#  ilgileniyorsak, gruplandırılmış veriler üzerinde sütun seçimi (her zamanki gibi dikdörtgen köşeli ayraçlar [])
#  de desteklenir
# =============================================================================



agesex=titanic.groupby("Sex")["Age"].mean()
print(agesex)



# =============================================================================
#  Pclass sütunu sayısal veriler içerir, ancak aslında sırasıyla ‘1’, ‘2’ ve ‘3'
#  etiketli 3 kategoriyi (veya faktörü) temsil eder. Bunlara ilişkin istatistiklerin
#  hesaplanması pek mantıklı değil. Bu nedenle, pandalar bu tür verileri 
#  işlemek için Kategorik bir veri türü sağlar. Daha fazla bilgi kullanım 
#  kılavuzu Kategorik veriler bölümünde verilmiştir.
# 
# =============================================================================



# =============================================================================
# Cinsiyet ve kabin sınıfı kombinasyonlarının her biri için ortalama bilet ücreti fiyatı nedir?
ort=titanic.groupby(["Sex", "Pclass"])["Fare"].mean()
print(ort)
# =============================================================================



# =============================================================================
# titanic["Pclass"].value_counts()
# Out[12]: 
# 3    491
# 1    216
# 2    184
# Name: Pclass, dtype: int64
# =============================================================================

# =============================================================================
# titanic["Pclass"].value_counts()
# Out[12]: 
# 3    491
# 1    216
# 2    184
# Name: Pclass, dtype: int64
# =============================================================================


# =============================================================================
# Hem boyut hem de sayım groupby ile birlikte kullanılabilir.
# Boyut, NaN değerlerini içerirken ve yalnızca satır 
# (tablonun boyutu) sağlarken, count eksik değerleri hariç t
# utar. Value_counts().dropna yönteminde, NaN değerlerini dahil 
# veya hariç tutmak için dropna bağımsız değişkenini kullanın.
# =============================================================================









 