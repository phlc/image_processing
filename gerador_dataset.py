import numpy as np
import os
import cv2
import pickle
import descritores_haralick as dh

DATADIR = "./imagens"
BIRADS = ["1", "2", "3", "4"]

dataset = [[], [], [], []]

count = 1
for birad in BIRADS:
    path = os.path.join(DATADIR,birad)
    for image_name in os.listdir(path):
        image = cv2.imread(os.path.join(path,image_name), 0)
        dataset[int(birad)-1].append(dh.calculateHaralickDescriptors(image))
        print(count)
        count+=1

output = open('dataset.pkl', 'wb')
pickle.dump(dataset, output)
