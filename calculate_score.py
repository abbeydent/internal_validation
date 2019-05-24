import pandas as pd 

dataset = pd.read_csv("dataset.csv")

print(dataset.head())

data = dataset.iloc[:,3:10]

print(data.head())

target = dataset.iloc[:,2].values

print(target)
