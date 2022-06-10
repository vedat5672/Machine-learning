import pandas as pd
titanic = pd.read_csv("titanic.csv")
titanic["Name"].str.lower()
titanic["Name"].str.split(",")
titanic["Surname"] = titanic["Name"].str.split(",").str.get(0)
titanic["Name"].str.contains("Countess")
 #    PassengerId  Survived  Pclass   Name     Sex   Age  SibSp  Parch  Ticket  Fare Cabin Embarked Surname
# 759          760         1       1  Rothes, the Countess. of (Lucy Noel Martha Dye...  female  33.0      0      0  110152  86.5   B77        S  Rothes
titanic["Name"].str.len()
titanic["Name"].str.len().idxmax() #307
titanic.loc[titanic["Name"].str.len().idxmax(), "Name"]
# =============================================================================
# Out[12]: 'Penasco y Castellana, Mrs. Victor de Satode (Maria Josefa Perez de Soto y Vallejo)'
# =============================================================================
titanic["Sex_short"] = titanic["Sex"].replace({"male": "M", "female": "F"})