import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import os
import cv2

DATADIR = "/Users/pedrocarvalho/computacao/6per/proc_imagens/trabalho_pratico/imagens"
BIRADS = ["1", "2", "3", "4"]

for birad in BIRADS:
    path = os.path.join(DATADIR, birad)
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
        plt.imshow(img_array, cmap="gray", vmin = 0, vmax = 255)
        print(img)
        print(img_array)
        plt.show()
        break
    break


