from math import log
import numpy as np

# Calcúla Entropia de Haralick
# @param matriz de co-ocorrência
# @return entropia
def entropia(matriz):
    resultado = 0.0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
           resultado += matriz[linha][coluna] * log(matriz[linha][coluna], 2)
    return -resultado

# Calcúla Homogeneidade de Haralick
# @param matriz de co-ocorrência
# @return homogeneidade
def homogeneidade(matriz):
    resultado = 0.0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
            resultado += matriz[linha][coluna] / (1 + abs(linha - coluna))
    return resultado

# Calcúla Energia de Haralick
# @param matriz de co-ocorrência
# @return energia
def energia(matriz):
    resultado = 0.0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
            resultado+= matriz[linha][coluna]**2
    return resultado

# Calcúla Contraste de Haralick
# @param matriz de co-ocorrência
# @return contraste
def contraste(matriz):
    resultado = 0.0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
            resultado+= (linha - coluna)**2 * matriz[linha][coluna]
    return resultado