import numpy as np
import pandas as pd

data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)
print(df)

groupedData = df.groupby("Company")
print("")
print(groupedData.mean())
print("")
print(groupedData.sum())
print("")
print(groupedData.std())
print("")
print(groupedData.sum().loc["FB"])
print("")
print(df.groupby("Company").sum().loc["GOOG"])
print("")
print(df.groupby("Company").count())
print("")
print(df.groupby("Company").describe())