import pandas as pd

air_quality_no2 = pd.read_csv("air_quality_no2_long.csv",
                              parse_dates=True)
air_quality_no2 = air_quality_no2[["date.utc", "location",
                                   "parameter", "value"]]

air_quality_pm25 = pd.read_csv("air_quality_pm25_long.csv",
                               parse_dates=True)
air_quality_pm25 = air_quality_pm25[["date.utc", "location",
                                     "parameter", "value"]]

# =============================================================================
# Benzer bir yapıya sahip iki tablo olan NO2 ve PM25 
# ölçümlerini tek bir tabloda birleştirmek istiyorum
# =============================================================================

air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)
print('Shape of the ``air_quality_pm25`` table: ', air_quality_pm25.shape)
# =============================================================================
# Shape of the ``air_quality_pm25`` table:  (1110, 4)
# =============================================================================

print('Shape of the ``air_quality_no2`` table: ', air_quality_no2.shape)
# =============================================================================
# Shape of the ``air_quality_no2`` table:  (2068, 4)
# =============================================================================

print('Shape of the resulting ``air_quality`` table: ', air_quality.shape)
# =============================================================================
# Shape of the resulting ``air_quality`` table:  (3178, 4)
# =============================================================================


# =============================================================================
# !!!!!The axis argument will return in a number of pandas methods that can be applied along an axis. A DataFrame has two corresponding axes:
# the first running vertically downwards across rows (axis 0), and the second running horizontally across columns (axis 1). Most operations
#  like concatenation or summary statistics are by default across rows (axis 0), but can be applied across columns as well.
# =============================================================================
air_quality = air_quality.sort_values("date.utc")
print(air_quality.head())
air_quality_ = pd.concat([air_quality_pm25, air_quality_no2], keys=["PM25", "NO2"])


# =============================================================================
#  Merge() işlevini kullanarak, aır_qualıty tablosundaki
#  satırların her biri için karşılık gelen koordinatlar
#  aır_qualıty_statıons_coord tablosundan eklenir. Her iki 
#  tablo da, bilgileri birleştirmek için anahtar olarak 
#  kullanılan ortak sütun konumuna sahiptir. Sol 
#  birleştirmeyi seçerek, yalnızca aır_qualıty (sol)
#  tablosunda, yani FR04014, BETR801 ve London Westminster
#  de bulunan konumlar sonuçta elde edilen tabloda sonuçlanır.
#  Birleştirme işlevi, veritabanı stili işlemlerine benzer birden çok birleştirme seçeneğini destekler.
# =============================================================================
stations_coord = pd.read_csv("air_quality_stations.csv")
air_quality = pd.merge(air_quality, stations_coord, how="left", on="location")



# =============================================================================
# Önceki örnekle karşılaştırıldığında, ortak bir sütun adı yoktur.
# Ancak, aır_qualıty tablosundaki parametre sütunu ve aır_qualıty_parameters_name
# içindeki kimlik sütununun her ikisi de ölçülen değişkeni ortak bir
# biçimde sağlar. Left_on ve right_on bağımsız değişkenleri burada 
# (yalnızca açık yerine) iki tablo arasındaki bağlantıyı oluşturmak 
# için kullanılır.
# =============================================================================
air_quality_parameters = pd.read_csv("air_quality_parameters.csv")

air_quality = pd.merge(air_quality, air_quality_parameters,
                       how='left', left_on='parameter', right_on='id')