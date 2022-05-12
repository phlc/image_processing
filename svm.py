from matplotlib.pyplot import table
import numpy as np
import pickle
import random
from sklearn import svm
from sklearn import metrics


# Treina e testa uma SVM a partir de um conjunto de descritores de todas imagens
# @param conjunto de descritores de todas imagens, número de descritores, opção gravar SVM em arquivo
# @return [SVM, metricas do teste]
def treinar_svm(descritores_todas_imagens, numero_descritores=3, gravar_svm=False):

    birad1 = []
    birad2 = []
    birad3 = []
    birad4 = []

    for instance in range(len(descritores_todas_imagens[0])):
        birad1.append([np.reshape(descritores_todas_imagens[0][instance], numero_descritores*5), 1])
        birad2.append([np.reshape(descritores_todas_imagens[1][instance], numero_descritores*5), 2])
        birad3.append([np.reshape(descritores_todas_imagens[2][instance], numero_descritores*5), 3])
        birad4.append([np.reshape(descritores_todas_imagens[3][instance], numero_descritores*5), 4])

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

    clf = svm.SVC(gamma=0.1, C=100)
    clf.fit(train_X, train_y)

    predictions = clf.predict(test_X)
    print(metrics.accuracy_score(test_y, predictions))
    print(metrics.confusion_matrix(test_y, predictions))