# -*- coding: utf-8 -*
"""
Created on Wed Jun  8 15:51:10 2022

@author: Monster
"""


import pandas as pd
import matplotlib as plt

air=pd.read_csv("air_quality_no2.csv",index_col=0, parse_dates=True)
print(air)
# =============================================================================
# Index_col ve parse_dates parametrelerinin kullanılması read_csv işlevi,
#  ilk (0.) sütunu sonuç veri çerçevesinin dizini olarak tanımlamak ve 
#  sütundaki tarihleri sırasıyla Zaman Damgası nesnelerine dönüştürmek 
#  için kullanılır.
# =============================================================================
air.plot()
air["station_paris"].plot()
# =============================================================================
# Londra'da ölçülen N02 değerlerini Paris'e karşı görsel olarak karşılaştırmak istiyorum.
# =============================================================================
air.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
# =============================================================================
# Çizim işlevini kullanırken varsayılan çizgi çiziminin yanı sıra,
#verileri çizmek için bir dizi alternatif kullanılabilir. Mevcut çizim
 #yöntemlerine genel bir bakış elde etmek için bazı standart 
 #Python kullanalım:
# =============================================================================

# =============================================================================
# [
#     method_name
#     for method_name in dir(air_quality.plot)
#     if not method_name.startswith("_")
# ]
# =============================================================================
# =============================================================================
# ['area',
#  'bar',
#  'barh',
#  'box',
#  'density',
#  'hexbin',
#  'hist',
#  'kde',
#  'line',
#  'pie',
#  'scatter']
# =============================================================================



# =============================================================================
# Seçeneklerden biri Dataframe'dir.çizim.bir boxplot anlamına gelen box() . Box yöntemi, hava kalitesi
# örnek verilerinde uygulanabilir:
# =============================================================================
air.plot.box()



# =============================================================================
# Sütunların her birinin ayrı bir alt bölümde olmasını istiyorum.
# =============================================================================

xs = air.plot.area(figsize=(12, 4), subplots=True)


























