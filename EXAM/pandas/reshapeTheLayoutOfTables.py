# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 19:23:23 2022

@author: Monster
"""

import pandas as pd
titanic=pd.read_csv("titanic.csv")
air_quality=pd.read_csv("air_quality_long.csv",index_col="date.utc", parse_dates=True)
sırala=titanic.sort_values(by="Age").head()
print(sırala)

# =============================================================================
# Titanik verileri kabin sınıfına ve yaşına göre 
# azalan düzende sıralamak istiyorum.
titanic.sort_values(by=['Pclass', 'Age'], ascending=False).head()
# =============================================================================


# ikiser adet location olsun 
no2 = air_quality[air_quality["parameter"] == "no2"]
no2_subset = no2.sort_index().groupby(["location"]).head(2)
print(no2_subset)


# =============================================================================
#location value sütündaki degerleri

# =============================================================================
#                             city country location parameter  value   unit
# date.utc                                                                 
# 2019-06-21 00:00:00+00:00  Paris      FR  FR04014       no2   20.0  µg/m³
# 2019-06-20 23:00:00+00:00  Paris      FR  FR04014       no2   21.8  µg/m³
# 2019-06-20 22:00:00+00:00  Paris      FR  FR04014       no2   26.5  µg/m³
# 2019-06-20 21:00:00+00:00  Paris      FR  FR04014       no2   24.9  µg/m³
# 2019-06-20 20:00:00+00:00  Paris      FR  FR04014       no2   21.4  µg/m³
# =============================================================================
no2_subset.pivot(columns="location", values="value")
# =============================================================================
no2.pivot(columns="location", values="value").plot()
# =============================================================================
# Tablo formundaki istasyonların her birinde NO2 ve PM2.5 
#için ortalama konsantrasyonları istiyorum
pivotparam=air_quality.pivot_table(
    values="value", index="location", columns="parameter", aggfunc="mean"
)
# =============================================================================
# =============================================================================
# Out[15]: 
# parameter                 no2       pm25        All
# location                                           
# BETR801             26.950920  23.169492  24.982353
# FR04014             29.374284        NaN  29.374284
# London Westminster  29.740050  13.443568  21.491708
# All                 29.430316  14.386849  24.222743
# =============================================================================





no2_pivoted = no2.pivot(columns="location", values="value").reset_index()


#Tüm hava kalitesi NO2 ölçümlerini tek bir sütunda (uzun format) toplamak istiyorum.
# =============================================================================
# no_2 = no2_pivoted.mel#t(id_vars="date.utc")
# 
# no_2.head()
# Out[19]: 
#                    date.utc location  value
# 0 2019-04-09 01:00:00+00:00  BETR801   22.5
# 1 2019-04-09 02:00:00+00:00  BETR801   53.5
# 2 2019-04-09 03:00:00+00:00  BETR801   54.5
# 3 2019-04-09 04:00:00+00:00  BETR801   34.5
# 4 2019-04-09 05:00:00+00:00  BETR801   46.5
# 
# 
# 
# =============================================================================



# =============================================================================
# 
# Panda.veri çerçevesindeki melt() yöntemi, veri tablosunu geniş biçimden uzun biçime dönüştürür. Sütun başlıkları, yeni oluşturulan bir sütundaki değişken adları olur.
# 
# Çözüm, pandaların nasıl uygulanacağına dair kısa versiyondur.erimek(). Yöntem, ıd_vars içinde belirtilmeyen tüm sütunları birlikte iki sütuna eritir: Sütun başlığı adlarına sahip bir sütun ve değerlerin kendisine sahip bir sütun. İkinci sütun varsayılan olarak ad değerini alır.
# 
# Panda.melt() yöntemi daha ayrıntılı olarak tanımlanabilir:
# 
# 
no_2 = no2_pivoted.melt(
    id_vars="date.utc",
    value_vars=["BETR801", "FR04014", "London Westminster"],
    value_name="NO_2",
    var_name="id_location",
)


no_2.head()
# =============================================================================








