# =============================================================================
#              COKLU DOGRUSAL REGRESYON
# =============================================================================

# BASİT DOGRUSAL REGRESYON y=ax+b veya y=a+bxi+ei
# ÇOKLU DOGRUSAL REGRESYON  y=b0+b1x1+b2x2+b3x3+c



# =============================================================================
#  p-value(olasılık değeri)
# ======================================================

# ========================================================
# H0:NULL hypothesis:Farksızlık hipotezi,sıfır hipotezi,boş hipotez
# H1:Alternatif hipotez
# p-değeri: olasılık değeri(genelde 0.05 alınır)
# P-değeri küçüldükçe H0 hatalı olma ihtimali artar
# P-değeri büyüdükçe H1 hatalı olma ihtimali artar 
# ======================================================

# =============================================================================
# Farklı Yaklasımlar

# .Bütün değişkenleri dahil etmek
# .Geriye doğru eleme(backward Elimination)
# .ileri secim(Forward Selection)
# .iki yönlü eleme(bidirectional Elimination)
# .Skor Karsılastırması(Score Comparison)

# =============================================================================

# BUTUN DEĞİŞKENLER
# değişken seçimi yapıldıysa ve değişkenlerden eminsek
# Zorunluluk varsa
# Kesif için


#GERİYE ELEME
#1)Significancce Level(SL) secilir genelde 0,065
#2)Bütün değişkenler kullanılırak model elde edilir
#2)En yüksek p-value değerine sahip olanndeğişken ele alınır ve sayet P>Sl
# ise 4.adıma,değilse son adıma (6.adım) gidilir
# 4)Bu asamada , 3.adımda secilen ve en yüksek p-valur degerine sahip değişken sistedmen kaldırılır
#5)Makine öğrenmesi güncellenir ve 3.adımda geri döönülür
#6)Makine öğrenmesi sonlandırılır

#İLERİYE SECİM
#1)Significance Level (Sl) seçilir (genelde 0,05)
#2)ütün değişkenler kullanılarak bir model insa edilir
#3)En düsük p-value değerine sahip olan değişken ele alınır
#4)Bu asamada, 3.adımda secilen değişken sabait tutularak yeni bir değişken 
#daha seçilir ve sisteme eklenir
#5)Makine öğrenmesi güncellenir ve 3.adıma geri dönülür , sayet en düşük p-degere sahip
#değişken için p<SL sarti saglanıyorsa 3.Adıma dönülür.
#Sağlanmıyorsa biter(6.Adıma geçilir)
#6)Makine öğrenmesi sonlandırılır

# ÇİFT YÖNLÜ ELEME

#1).Significance Level(SL) secilir (genelde 0.05)
#2)Bütün değişkenler kullanılarak bir model olusturulıur.
#3)En düşük p-value değerine sahip olan değişken ele alınır
#4)Bu asamada , 3.adımda seçilen değişken sabit tutularak diger
#bütün değişkenler sisteme dahil edilir ve en düşük p değerine sahip
#olan sistemde kalır
#5)SL değerini altında olan değişkenler sistemde kalır ve eski değişkenlerden 
#hiçbirisi sistemden çıkarılamaz
#6)Makline öğrenmesi sonlandırılır.



# -*- coding: utf-8 -*-

#1.kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#2.veri onisleme
#2.1.veri yukleme
veriler = pd.read_csv('veriler.csv')
#pd.read_csv("veriler.csv")
#test
print(veriler)

#encoder: Kategorik -> Numeric
ulke = veriler.iloc[:,0:1].values
print(ulke)

from sklearn import preprocessing

le = preprocessing.LabelEncoder()

ulke[:,0] = le.fit_transform(veriler.iloc[:,0])

print(ulke)


ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()
print(ulke)

#encoder: Kategorik -> Numeric
c = veriler.iloc[:,-1:].values
print(c)


from sklearn import preprocessing

le = preprocessing.LabelEncoder()

c[:,-1] = le.fit_transform(veriler.iloc[:,-1])

print(c)


ohe = preprocessing.OneHotEncoder()
c = ohe.fit_transform(c).toarray()
print(c)



#numpy dizileri dataframe donusumu
sonuc = pd.DataFrame(data=ulke, index = range(22), columns = ['fr','tr','us'])
print(sonuc)
yas=veriler.iloc[:,1:4].values
sonuc2 = pd.DataFrame(data=yas, index = range(22), columns = ['boy','kilo','yas'])
print(sonuc2)

cinsiyet = veriler.iloc[:,-1].values
print(cinsiyet)

sonuc3 = pd.DataFrame(data = c[:,:1], index = range(22), columns = ['cinsiyet'])
print(sonuc3)


 
#dataframe birlestirme islemi
s=pd.concat([sonuc,sonuc2], axis=1)
print(s)

s2=pd.concat([s,sonuc3], axis=1)
print(s2)

#verilerin egitim ve test icin bolunmesi
from sklearn.model_selection import train_test_split

x_train, x_test,y_train,y_test = train_test_split(s,sonuc3,test_size=0.33, random_state=0)
















































