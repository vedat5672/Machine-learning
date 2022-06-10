import pandas as pd

import matplotlib.pyplot as plt

air_quality = pd.read_csv("air_quality_no2_long.csv")

air_quality = air_quality.rename(columns={"date.utc": "datetime"})
air_quality.city.unique()
# =============================================================================
# array(['Paris', 'Antwerpen', 'London'], dtype=object)
# city sütününun essiz değerleri 
# =============================================================================
print(air_quality["datetime"]) # Name: datetime, Length: 2068, dtype:Name: datetime, Length: 2068, dtype: datetime64[ns, UTC]object
air_quality["datetime"] = pd.to_datetime(air_quality["datetime"])
print(air_quality["datetime"]) # Name: datetime, Length: 2068, dtype: datetime64[ns, UTC]

# =============================================================================
# As many data sets do contain datetime information in one of the columns,
# pandas input function like pandas.read_csv() and pandas.read_json() 
# can do the transformation to dates when reading the data using the 
# parse_dates parameter with a list of the columns to read as Timestamp:
# =============================================================================

minx=air_quality["datetime"].min(),
maxy=air_quality["datetime"].max()
print(minx)
print(maxy)
subDate=air_quality["datetime"].max() - air_quality["datetime"].min()
print(subDate)

# =============================================================================
# ?Veri çerçevesine yalnızca ölçümün ayını içeren yeni bir sütun
#  eklemek istiyorum
# =============================================================================
air_quality["month"] = air_quality["datetime"].dt.month 
# =============================================================================
#Ölcüm yerlerinin her biri için haftanın her günü için ortalama NO' konsantrasyonu nedir?
# =============================================================================
ölçüm=air_quality.groupby(
    [air_quality["datetime"].dt.weekday, "location"])["value"].mean()
# =============================================================================
# Tüm istasyonların zaman serimizin günü boyunca tipik NO2 modelini bir araya getirin. Ba
#  ka bir deyişle, günün her saati için ortalama değer nedir?
# =============================================================================
fig, axs = plt.subplots(figsize=(12, 4))

air_quality.groupby(air_quality["datetime"].dt.hour)["value"].mean().plot(
    kind='bar', rot=0, ax=axs
)



plt.xlabel("Hour of the day");  # custom x label using matplotlib

plt.ylabel("$NO_2 (µg/m^3)$");


# =============================================================================
# Dizin olarak Datetime
# Yeniden şekillendirmeyle ilgili öğreticide,
# ölçüm konumlarının her biriyle veri tablosunu
# ayrı bir sütun olarak yeniden şekillendirmek
# için pivot() tanıtıldı:
# =============================================================================

no_2 = air_quality.pivot(index="datetime", columns="location", values="value")

# =============================================================================
# Bir datetime dizini (yani DatetimeIndex) 
#ile çalışmak güçlü işlevler sağlar. Örneğin
#, zaman serisi özelliklerini almak için dt 
#erişimcisine ihtiyacımız yoktur, ancak bu 
#özelliklerin doğrudan dizinde kullanılabilir olması
#gerekir: 
    #no_2.index.year, no_2.index.weekday
# =============================================================================





# =============================================================================
# 20 Mayıs'tan 21 Mayıs'ın sonuna kadar farklı
# istasyonlarda NO2 değerlerinin bir grafiğini
# oluşturun
# =============================================================================

no_2["2019-05-20":"2019-05-21"].plot();




# =============================================================================
# BİR ZAMAN SERİSİNİ BASKA BİR FREKANSA YENİDEN ÖRNEKLEME
# =============================================================================


#Geçerli saatlik zaman serisi değerlerini 
#istasyonların her birinde aylık maksimum değere toplayın.


monthly_max = no_2.resample("M").max()
print(monthly_max)

# =============================================================================
# resample:
#     Datetime indeksine sahip zaman serisi verileri üzerinde çok güçlü bir yöntem, zaman serilerini başka bir frekansa yeniden örnekleme () yeteneğidir (örneğin, ikinci verileri 5 dakikalık verilere dönüştürme).
# 
# Resample() yöntemi bir groupby işlemine benzer:
# 
# hedef frekansı tanımlayan bir dize (örneğin M, 5H, ...) kullanarak zamana dayalı bir gruplama sağlar
# 
# mean, max gibi bir toplama işlevi gerektirir,…
# =============================================================================


no_2.resample("D").mean().plot(style="-o", figsize=(10, 5));











