from cgi import test
from matplotlib.pyplot import table
import numpy as np
import pickle
import random

input = open('dataset.pkl', 'rb')
dataset = np.array(pickle.load(input))
input.close()

birad1 = []
birad2 = []
birad3 = []
birad4 = []

for instance in range(100):
    birad1.append([np.reshape(dataset[0][instance], 20), 0])
    birad2.append([np.reshape(dataset[1][instance], 20), 1])
    birad3.append([np.reshape(dataset[2][instance], 20), 2])
    birad4.append([np.reshape(dataset[3][instance], 20), 3])

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

for sample in training_data:
    print(sample[0])