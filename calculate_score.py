import pandas as pd 

from sklearn.model_selection import train_test_split


dataset = pd.read_csv("dataset.csv")

#print(dataset.head())

data = dataset.iloc[:,3:10]

print(data.head())

target = dataset.iloc[:,2].values

print(target)


data_training, data_test, target_training, target_test = train_test_split(data, target, test_size = 0.25, random_state = 0)

print(data_training.head())
print(data_test.head())
print(target_training)
print(target_test)

print(data.shape)
print(target.shape)
print(data_training.shape)
print(data_test.shape)
print(target_training.shape)
print(target_test.shape)





