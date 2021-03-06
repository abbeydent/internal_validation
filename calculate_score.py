import pandas as pd 

from sklearn.model_selection import train_test_split
from sklearn import linear_model
from matplotlib import pyplot as plt 

from sklearn import metrics
from sklearn.model_selection import KFold

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


linear_machine = linear_model.LinearRegression()
linear_machine.fit(data_training, target_training)
prediction = linear_machine.predict(data_test)

print(prediction)

plt.scatter(target_test, prediction)
plt.xlabel('target test')
plt.ylabel('prediction')

plt.savefig("scatter_test_prediction.png")

print(metrics.r2_score(target_test, prediction))


#=======================================================


data = data.values

print(data)


kfold_machine = KFold(n_splits = 4)
kfold_machine.get_n_splits(data)
print(kfold_machine)

for training_index, test_index in kfold_machine.split(data):
	print("Training: ", training_index)
	print("Test: ", test_index)
	data_training, data_test = data[training_index], data[test_index]
	target_training, target_test = target[training_index], target[test_index]
	linear_machine = linear_model.LinearRegression()
	linear_machine.fit(data_training, target_training)
	prediction = linear_machine.predict(data_test)
	print(metrics.r2_score(target_test, prediction))

	



