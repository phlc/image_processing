import tensorflow as tf
from matplotlib.pyplot import table
import numpy as np
import pickle
import random


def preparar_rede_neural():
    input = open('dataset.pkl', 'rb')
    dataset = np.array(pickle.load(input))
    input.close()

    birad1 = []
    birad2 = []
    birad3 = []
    birad4 = []

    for instance in range(100):
        birad1.append([np.reshape(dataset[0][instance], 15), [1,0,0,0]])
        birad2.append([np.reshape(dataset[1][instance], 15), [0,1,0,0]])
        birad3.append([np.reshape(dataset[2][instance], 15), [0,0,1,0]])
        birad4.append([np.reshape(dataset[3][instance], 15), [0,0,0,1]])

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

    pickle.dump(train_X, 'train_x.pkl')
    pickle.dump(train_y, 'train_y.pkl')
    pickle.dump(test_X, 'test_X.pkl')
    pickle.dump(test_y, 'test_y.pkl')


def treinar_rede_neural():
    train_X = open('train_X.pkl', 'rb')
    train_y = open('train_y.pkl', 'rb')
    test_X = open('test_X.pkl', 'rb')
    test_y = open('test_y.pkl', 'rb')
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(42, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(4, activation=tf.nn.softmax))

    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=['accuracy', tf.keras.metrics.Precision()])
    model.fit(x=train_X, y=train_y, epochs=500)

    model.evaluate(x=test_X, y=test_y)

    return(model)

# Salvar rede neural
# rede_file = open('rede_neural.pkl',  'wb')
# pickle.dump(model, rede_file)
# rede_file.close()

# Carregar rede neural
# rede_file = open('rede_neural.pkl',  'rb')
# model = pickle.load(rede_file)

# Matriz de confusão
# y_pred = model.predict(train_X)
# confusion_matrix = sklearn.metrics.confusion_matrix(train_y, np.rint(y_pred))