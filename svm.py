from matplotlib.pyplot import table
import numpy as np
import pickle
import random
from sklearn import svm

input = open('dataset.pkl', 'rb')
dataset = np.array(pickle.load(input))
input.close()

birad1 = []
birad2 = []
birad3 = []
birad4 = []

for instance in range(100):
    birad1.append([np.reshape(dataset[0][instance], 15), 1])
    birad2.append([np.reshape(dataset[1][instance], 15), 2])
    birad3.append([np.reshape(dataset[2][instance], 15), 3])
    birad4.append([np.reshape(dataset[3][instance], 15), 4])

random.shuffle(birad1)
random.shuffle(birad2)
random.shuffle(birad3)
random.shuffle(birad4)

training_data = []
test_data = []

for instance in range(75):
    training_data.append(birad1[instance])
    training_data.append(birad2[instance])
    training_data.append(birad3[instance])
    training_data.append(birad4[instance])

training_data = np.array(training_data, dtype=object)

for instance in range(75, 100):
    test_data.append(birad1[instance])
    test_data.append(birad2[instance])
    test_data.append(birad3[instance])
    test_data.append(birad4[instance])

test_data = np.array(test_data, dtype=object)

random.shuffle(training_data)
random.shuffle(test_data)

train_X = []
train_y = []

for descritor, classe in training_data:
    train_X.append(descritor)
    train_y.append(classe)

train_X = np.array(train_X)
train_y = np.array(train_y)

test_X = []
test_y = []

for descritor, classe in test_data:
    test_X.append(descritor)
    test_y.append(classe)

test_X = np.array(test_X)
test_y = np.array(test_y)

clf = svm.SVC(gamma=0.01, C=100)
clf.fit(train_X, train_y)


errados = 0
certos = 0
for i in range(len(test_X)):
    prediction = clf.predict(test_X[i].reshape(1, -1))
    print (prediction, test_y[i])
    if(prediction == test_y[i]):
        certos+=1
    else:
        errados+=1
print (certos, errados)