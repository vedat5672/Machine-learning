import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)
print("df")
print(df)

print("df.max()") # tabloyu yazdırır veri çercevesi olusturma
print(df.max()) # tabloyu yazdırır veri çercevesi olusturma

print("df.describe()") # tabloyu yazdırır veri çercevesi olusturma
print(df.describe()) # tabloyu yazdırır veri çercevesi olusturma sayısal
#veri tiplerini inceler

print("df[Age]") # Bir veri çercevesindeki her sütün bir veridir.
print(df["Age"]) # Bir veri çercevesindeki her sütün bir veridir.

ages = pd.Series([22, 35, 58], name="Age") # tablo serisi olusturma


print("df[Age].max()") # maksimumu yazdır
print(df["Age"].max()) # maksimumu yazdır

print("df[Age].describe()") # tablonun istatistikleri
print(df["Age"].describe()) # tablonun istatistikleri

############ TABLO VERİLERİNİ OKUMA VE YAZMA #############
titanic = pd.read_csv("titanic.csv")
print(titanic.head(8))
print(titanic.info)
print(titanic.head())
print(titanic["Age"].shape)


# Veri çerçevesi.şekil, satır ve sütun sayısını içeren bir pandalar Serisinin ve veriçerçevesinin
# bir özniteliğidir (okuma ve yazma öğreticisini hatırlayın, öznitelikler için parantez kullanmayın):
# (nrows, ncolumns). Pandalar Serisi 1 boyutludur ve yalnızca satır sayısı döndürülür.
age_sex = titanic[["Age", "Sex"]]
print(age_sex)
tip=type(titanic[["Age", "Sex"]])
print(tip)
above_35 = titanic[titanic["Age"] > 35] # 35 yasından buyuk yolcuları getir
print(above_35)
buyukmu=titanic["Age"] > 35
print(buyukmu)
print("####################################")

above_35.head()


print(above_35.shape)
class_23 = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]
print(class_23.head())

age_no_na = titanic[titanic["Age"].notna()] # yası bilinen yolcu verisi
print("yas bilinen")
print(age_no_na)
print(age_no_na.shape)
print("35 Yaşından büyük yolcuların isimleriyle ilgileniyorum.")
adult_names = titanic.loc[titanic["Age"] > 35, "Name"]
print(adult_names)
print("iloc")
titanic.iloc[9:25, 2:5]# 9 dan 25 satır , 2 den 5 e sütün
titanic.iloc[0:3, 3] = "anonymous"
sv=titanic.iloc[0:3, 3]
print(sv)
