import numpy as np

def c1(img, tons):
    matriz = np.zeros(4*tons*tons).reshape(4, tons, tons)
    print(matriz)

c1([], 4)