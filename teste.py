import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

image_path = "./imagens/1/p_d_left_cc(12).png"
image = cv2.imread(image_path, 0)
image = np.array(image)
print(image)

for i in range(len(image)):
    for j in range(len(image[0])):
        image[i][j] = int(image[i][j]/255 * 31)

print(image)
plt.imshow(image, cmap="gray", vmin=0, vmax=31)
plt.show()
