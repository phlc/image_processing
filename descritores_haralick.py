from math import log
import numpy as np

def entropia(matriz):
    resultado = 0.0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
           resultado += matriz[linha][coluna] * log(matriz[linha][coluna], 2)
    return -resultado

def homogeneidade(matriz):
    resultado = 0.0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
            resultado += matriz[linha][coluna] / (1 + abs(linha - coluna))
    return resultado

def energia(matriz):
    resultado = 0.0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
            resultado+= matriz[linha][coluna]**2
    return resultado

def contraste(matriz):
    resultado = 0.0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
            resultado+= (linha - coluna)**2 * matriz[linha][coluna]
    return resultado