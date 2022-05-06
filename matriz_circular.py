import numpy as np

# Cálcula a matriz circular de co-ocorrência de raio 1
# @param img -> matriz 2d de tons de cinza da imagem, tons -> quantização dos tons de cinza
def c1(img, tons):
    # Matriz de co-ocorrência número de tons x número de tons
    matriz = np.zeros(tons*tons).reshape(tons, tons)

    # Contador de pontos inseridos
    contador_pontos = 0

    # Verificar co-ocorrência pixel a pixel
    for linha_pixel in range(len(img)):
        for coluna_pixel in range(len(img[0])):

            # Verificar co-ocorrência entre o pixel e todos os pontos do círculos
            if (linha_pixel + 0 < len(img)) and (coluna_pixel + 1 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 0][img[coluna_pixel+ 1]]] += 1
                contador_pontos += 1
            if (linha_pixel + 1 < len(img)) and (coluna_pixel + 0 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 1][img[coluna_pixel+ 0]]] += 1
                contador_pontos += 1
            if (linha_pixel + -1 < len(img)) and (coluna_pixel + 0 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -1][img[coluna_pixel+ 0]]] += 1
                contador_pontos += 1
            if (linha_pixel + 0 < len(img)) and (coluna_pixel + -1 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 0][img[coluna_pixel+ -1]]] += 1
                contador_pontos += 1

    # Calcular Probabilidade de cada co-ocorrência
    for linha_pixel in range(tons):
        for coluna_pixel in range(tons):
            matriz[linha_pixel][coluna_pixel] /= contador_pontos
    return matriz

# Cálcula a matriz circular de co-ocorrência de raio 2
# @param img -> matriz 2d de tons de cinza da imagem, tons -> quantização dos tons de cinza
def c2(img, tons):
    # Matriz de co-ocorrência número de tons x número de tons
    matriz = np.zeros(tons*tons).reshape(tons, tons)

    # Contador de pontos inseridos
    contador_pontos = 0

    # Verificar co-ocorrência pixel a pixel
    for linha_pixel in range(len(img)):
        for coluna_pixel in range(len(img[0])):

            # Verificar co-ocorrência entre o pixel e todos os pontos do círculos
            if (linha_pixel + 2 < len(img)) and (coluna_pixel + -1 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 2][img[coluna_pixel+ -1]]] += 1
                contador_pontos += 1
            if (linha_pixel + 1 < len(img)) and (coluna_pixel + 2 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 1][img[coluna_pixel+ 2]]] += 1
                contador_pontos += 1
            if (linha_pixel + -1 < len(img)) and (coluna_pixel + -2 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -1][img[coluna_pixel+ -2]]] += 1
                contador_pontos += 1
            if (linha_pixel + 2 < len(img)) and (coluna_pixel + 1 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 2][img[coluna_pixel+ 1]]] += 1
                contador_pontos += 1
            if (linha_pixel + -2 < len(img)) and (coluna_pixel + -1 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -2][img[coluna_pixel+ -1]]] += 1
                contador_pontos += 1
            if (linha_pixel + -2 < len(img)) and (coluna_pixel + 1 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -2][img[coluna_pixel+ 1]]] += 1
                contador_pontos += 1
            if (linha_pixel + 2 < len(img)) and (coluna_pixel + 0 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 2][img[coluna_pixel+ 0]]] += 1
                contador_pontos += 1
            if (linha_pixel + 1 < len(img)) and (coluna_pixel + -2 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 1][img[coluna_pixel+ -2]]] += 1
                contador_pontos += 1
            if (linha_pixel + -2 < len(img)) and (coluna_pixel + 0 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -2][img[coluna_pixel+ 0]]] += 1
                contador_pontos += 1
            if (linha_pixel + 0 < len(img)) and (coluna_pixel + 2 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 0][img[coluna_pixel+ 2]]] += 1
                contador_pontos += 1
            if (linha_pixel + -1 < len(img)) and (coluna_pixel + 2 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -1][img[coluna_pixel+ 2]]] += 1
                contador_pontos += 1
            if (linha_pixel + 0 < len(img)) and (coluna_pixel + -2 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 0][img[coluna_pixel+ -2]]] += 1
                contador_pontos += 1

    # Calcular Probabilidade de cada co-ocorrência
    for linha_pixel in range(tons):
        for coluna_pixel in range(tons):
            matriz[linha_pixel][coluna_pixel] /= contador_pontos
    return matriz

# Cálcula a matriz circular de co-ocorrência de raio 4
# @param img -> matriz 2d de tons de cinza da imagem, tons -> quantização dos tons de cinza
def c4(img, tons):
    # Matriz de co-ocorrência número de tons x número de tons
    matriz = np.zeros(tons*tons).reshape(tons, tons)

    # Contador de pontos inseridos
    contador_pontos = 0

    # Verificar co-ocorrência pixel a pixel
    for linha_pixel in range(len(img)):
        for coluna_pixel in range(len(img[0])):

            # Verificar co-ocorrência entre o pixel e todos os pontos do círculos
            if (linha_pixel + 4 < len(img)) and (coluna_pixel + 0 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 4][img[coluna_pixel+ 0]]] += 1
                contador_pontos += 1
            if (linha_pixel + 3 < len(img)) and (coluna_pixel + -2 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 3][img[coluna_pixel+ -2]]] += 1
                contador_pontos += 1
            if (linha_pixel + -3 < len(img)) and (coluna_pixel + -3 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -3][img[coluna_pixel+ -3]]] += 1
                contador_pontos += 1
            if (linha_pixel + 0 < len(img)) and (coluna_pixel + -4 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 0][img[coluna_pixel+ -4]]] += 1
                contador_pontos += 1
            if (linha_pixel + -3 < len(img)) and (coluna_pixel + 3 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -3][img[coluna_pixel+ 3]]] += 1
                contador_pontos += 1
            if (linha_pixel + -4 < len(img)) and (coluna_pixel + -1 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -4][img[coluna_pixel+ -1]]] += 1
                contador_pontos += 1
            if (linha_pixel + -4 < len(img)) and (coluna_pixel + 1 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -4][img[coluna_pixel+ 1]]] += 1
                contador_pontos += 1
            if (linha_pixel + -1 < len(img)) and (coluna_pixel + 4 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -1][img[coluna_pixel+ 4]]] += 1
                contador_pontos += 1
            if (linha_pixel + 3 < len(img)) and (coluna_pixel + -3 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 3][img[coluna_pixel+ -3]]] += 1
                contador_pontos += 1
            if (linha_pixel + 3 < len(img)) and (coluna_pixel + 3 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 3][img[coluna_pixel+ 3]]] += 1
                contador_pontos += 1
            if (linha_pixel + -3 < len(img)) and (coluna_pixel + 2 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -3][img[coluna_pixel+ 2]]] += 1
                contador_pontos += 1
            if (linha_pixel + 1 < len(img)) and (coluna_pixel + -4 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 1][img[coluna_pixel+ -4]]] += 1
                contador_pontos += 1
            if (linha_pixel + 0 < len(img)) and (coluna_pixel + 4 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 0][img[coluna_pixel+ 4]]] += 1
                contador_pontos += 1
            if (linha_pixel + -4 < len(img)) and (coluna_pixel + 0 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -4][img[coluna_pixel+ 0]]] += 1
                contador_pontos += 1
            if (linha_pixel + -2 < len(img)) and (coluna_pixel + -3 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -2][img[coluna_pixel+ -3]]] += 1
                contador_pontos += 1
            if (linha_pixel + -2 < len(img)) and (coluna_pixel + 3 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -2][img[coluna_pixel+ 3]]] += 1
                contador_pontos += 1
            if (linha_pixel + 4 < len(img)) and (coluna_pixel + -1 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 4][img[coluna_pixel+ -1]]] += 1
                contador_pontos += 1
            if (linha_pixel + 3 < len(img)) and (coluna_pixel + 2 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 3][img[coluna_pixel+ 2]]] += 1
                contador_pontos += 1
            if (linha_pixel + 4 < len(img)) and (coluna_pixel + 1 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 4][img[coluna_pixel+ 1]]] += 1
                contador_pontos += 1
            if (linha_pixel + -3 < len(img)) and (coluna_pixel + -2 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -3][img[coluna_pixel+ -2]]] += 1
                contador_pontos += 1
            if (linha_pixel + 2 < len(img)) and (coluna_pixel + -3 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 2][img[coluna_pixel+ -3]]] += 1
                contador_pontos += 1
            if (linha_pixel + 1 < len(img)) and (coluna_pixel + 4 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 1][img[coluna_pixel+ 4]]] += 1
                contador_pontos += 1
            if (linha_pixel + 2 < len(img)) and (coluna_pixel + 3 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 2][img[coluna_pixel+ 3]]] += 1
                contador_pontos += 1
            if (linha_pixel + -1 < len(img)) and (coluna_pixel + -4 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -1][img[coluna_pixel+ -4]]] += 1
                contador_pontos += 1

    # Calcular Probabilidade de cada co-ocorrência
    for linha_pixel in range(tons):
        for coluna_pixel in range(tons):
            matriz[linha_pixel][coluna_pixel] /= contador_pontos
    return matriz

# Cálcula a matriz circular de co-ocorrência de raio 8
# @param img -> matriz 2d de tons de cinza da imagem, tons -> quantização dos tons de cinza
def c8(img, tons):
    # Matriz de co-ocorrência número de tons x número de tons
    matriz = np.zeros(tons*tons).reshape(tons, tons)

    # Contador de pontos inseridos
    contador_pontos = 0

    # Verificar co-ocorrência pixel a pixel
    for linha_pixel in range(len(img)):
        for coluna_pixel in range(len(img[0])):

            # Verificar co-ocorrência entre o pixel e todos os pontos do círculos
            if (linha_pixel + -1 < len(img)) and (coluna_pixel + 8 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -1][img[coluna_pixel+ 8]]] += 1
                contador_pontos += 1
            if (linha_pixel + -2 < len(img)) and (coluna_pixel + 8 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -2][img[coluna_pixel+ 8]]] += 1
                contador_pontos += 1
            if (linha_pixel + -6 < len(img)) and (coluna_pixel + -5 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -6][img[coluna_pixel+ -5]]] += 1
                contador_pontos += 1
            if (linha_pixel + -5 < len(img)) and (coluna_pixel + -6 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -5][img[coluna_pixel+ -6]]] += 1
                contador_pontos += 1
            if (linha_pixel + 3 < len(img)) and (coluna_pixel + 7 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 3][img[coluna_pixel+ 7]]] += 1
                contador_pontos += 1
            if (linha_pixel + 8 < len(img)) and (coluna_pixel + 0 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 8][img[coluna_pixel+ 0]]] += 1
                contador_pontos += 1
            if (linha_pixel + -5 < len(img)) and (coluna_pixel + 6 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -5][img[coluna_pixel+ 6]]] += 1
                contador_pontos += 1
            if (linha_pixel + -8 < len(img)) and (coluna_pixel + -1 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -8][img[coluna_pixel+ -1]]] += 1
                contador_pontos += 1
            if (linha_pixel + -8 < len(img)) and (coluna_pixel + -2 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -8][img[coluna_pixel+ -2]]] += 1
                contador_pontos += 1
            if (linha_pixel + -8 < len(img)) and (coluna_pixel + 1 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -8][img[coluna_pixel+ 1]]] += 1
                contador_pontos += 1
            if (linha_pixel + 0 < len(img)) and (coluna_pixel + 8 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 0][img[coluna_pixel+ 8]]] += 1
                contador_pontos += 1
            if (linha_pixel + -7 < len(img)) and (coluna_pixel + -4 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -7][img[coluna_pixel+ -4]]] += 1
                contador_pontos += 1
            if (linha_pixel + -2 < len(img)) and (coluna_pixel + -8 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -2][img[coluna_pixel+ -8]]] += 1
                contador_pontos += 1
            if (linha_pixel + -1 < len(img)) and (coluna_pixel + -8 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -1][img[coluna_pixel+ -8]]] += 1
                contador_pontos += 1
            if (linha_pixel + 2 < len(img)) and (coluna_pixel + 8 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 2][img[coluna_pixel+ 8]]] += 1
                contador_pontos += 1
            if (linha_pixel + 7 < len(img)) and (coluna_pixel + 4 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 7][img[coluna_pixel+ 4]]] += 1
                contador_pontos += 1
            if (linha_pixel + -4 < len(img)) and (coluna_pixel + 7 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -4][img[coluna_pixel+ 7]]] += 1
                contador_pontos += 1
            if (linha_pixel + 6 < len(img)) and (coluna_pixel + 5 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 6][img[coluna_pixel+ 5]]] += 1
                contador_pontos += 1
            if (linha_pixel + 4 < len(img)) and (coluna_pixel + -7 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 4][img[coluna_pixel+ -7]]] += 1
                contador_pontos += 1
            if (linha_pixel + 5 < len(img)) and (coluna_pixel + -6 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 5][img[coluna_pixel+ -6]]] += 1
                contador_pontos += 1
            if (linha_pixel + -3 < len(img)) and (coluna_pixel + -7 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -3][img[coluna_pixel+ -7]]] += 1
                contador_pontos += 1
            if (linha_pixel + 5 < len(img)) and (coluna_pixel + 6 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 5][img[coluna_pixel+ 6]]] += 1
                contador_pontos += 1
            if (linha_pixel + 2 < len(img)) and (coluna_pixel + -8 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 2][img[coluna_pixel+ -8]]] += 1
                contador_pontos += 1
            if (linha_pixel + 8 < len(img)) and (coluna_pixel + 2 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 8][img[coluna_pixel+ 2]]] += 1
                contador_pontos += 1
            if (linha_pixel + 0 < len(img)) and (coluna_pixel + -8 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 0][img[coluna_pixel+ -8]]] += 1
                contador_pontos += 1
            if (linha_pixel + -8 < len(img)) and (coluna_pixel + 0 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -8][img[coluna_pixel+ 0]]] += 1
                contador_pontos += 1
            if (linha_pixel + 7 < len(img)) and (coluna_pixel + -3 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 7][img[coluna_pixel+ -3]]] += 1
                contador_pontos += 1
            if (linha_pixel + -7 < len(img)) and (coluna_pixel + 4 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -7][img[coluna_pixel+ 4]]] += 1
                contador_pontos += 1
            if (linha_pixel + 6 < len(img)) and (coluna_pixel + -5 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 6][img[coluna_pixel+ -5]]] += 1
                contador_pontos += 1
            if (linha_pixel + 1 < len(img)) and (coluna_pixel + 8 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 1][img[coluna_pixel+ 8]]] += 1
                contador_pontos += 1
            if (linha_pixel + 7 < len(img)) and (coluna_pixel + 3 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 7][img[coluna_pixel+ 3]]] += 1
                contador_pontos += 1
            if (linha_pixel + 3 < len(img)) and (coluna_pixel + -7 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 3][img[coluna_pixel+ -7]]] += 1
                contador_pontos += 1
            if (linha_pixel + 4 < len(img)) and (coluna_pixel + 7 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 4][img[coluna_pixel+ 7]]] += 1
                contador_pontos += 1
            if (linha_pixel + 8 < len(img)) and (coluna_pixel + -1 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 8][img[coluna_pixel+ -1]]] += 1
                contador_pontos += 1
            if (linha_pixel + 8 < len(img)) and (coluna_pixel + -2 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 8][img[coluna_pixel+ -2]]] += 1
                contador_pontos += 1
            if (linha_pixel + 1 < len(img)) and (coluna_pixel + -8 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 1][img[coluna_pixel+ -8]]] += 1
                contador_pontos += 1
            if (linha_pixel + -6 < len(img)) and (coluna_pixel + 5 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -6][img[coluna_pixel+ 5]]] += 1
                contador_pontos += 1
            if (linha_pixel + 8 < len(img)) and (coluna_pixel + 1 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 8][img[coluna_pixel+ 1]]] += 1
                contador_pontos += 1
            if (linha_pixel + -3 < len(img)) and (coluna_pixel + 7 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -3][img[coluna_pixel+ 7]]] += 1
                contador_pontos += 1
            if (linha_pixel + -8 < len(img)) and (coluna_pixel + 2 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -8][img[coluna_pixel+ 2]]] += 1
                contador_pontos += 1
            if (linha_pixel + -7 < len(img)) and (coluna_pixel + -3 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -7][img[coluna_pixel+ -3]]] += 1
                contador_pontos += 1
            if (linha_pixel + -4 < len(img)) and (coluna_pixel + -7 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -4][img[coluna_pixel+ -7]]] += 1
                contador_pontos += 1
            if (linha_pixel + -7 < len(img)) and (coluna_pixel + 3 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -7][img[coluna_pixel+ 3]]] += 1
                contador_pontos += 1
            if (linha_pixel + 7 < len(img)) and (coluna_pixel + -4 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 7][img[coluna_pixel+ -4]]] += 1
                contador_pontos += 1

    # Calcular Probabilidade de cada co-ocorrência
    for linha_pixel in range(tons):
        for coluna_pixel in range(tons):
            matriz[linha_pixel][coluna_pixel] /= contador_pontos
    return matriz

# Cálcula a matriz circular de co-ocorrência de raio 16
# @param img -> matriz 2d de tons de cinza da imagem, tons -> quantização dos tons de cinza
def c16(img, tons):
    # Matriz de co-ocorrência número de tons x número de tons
    matriz = np.zeros(tons*tons).reshape(tons, tons)

    # Contador de pontos inseridos
    contador_pontos = 0

    # Verificar co-ocorrência pixel a pixel
    for linha_pixel in range(len(img)):
        for coluna_pixel in range(len(img[0])):

            # Verificar co-ocorrência entre o pixel e todos os pontos do círculos
            if (linha_pixel + 10 < len(img)) and (coluna_pixel + -12 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 10][img[coluna_pixel+ -12]]] += 1
                contador_pontos += 1
            if (linha_pixel + 2 < len(img)) and (coluna_pixel + -16 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 2][img[coluna_pixel+ -16]]] += 1
                contador_pontos += 1
            if (linha_pixel + -15 < len(img)) and (coluna_pixel + -5 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -15][img[coluna_pixel+ -5]]] += 1
                contador_pontos += 1
            if (linha_pixel + 15 < len(img)) and (coluna_pixel + -4 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 15][img[coluna_pixel+ -4]]] += 1
                contador_pontos += 1
            if (linha_pixel + -15 < len(img)) and (coluna_pixel + 4 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -15][img[coluna_pixel+ 4]]] += 1
                contador_pontos += 1
            if (linha_pixel + 15 < len(img)) and (coluna_pixel + 5 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 15][img[coluna_pixel+ 5]]] += 1
                contador_pontos += 1
            if (linha_pixel + -1 < len(img)) and (coluna_pixel + 16 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -1][img[coluna_pixel+ 16]]] += 1
                contador_pontos += 1
            if (linha_pixel + -2 < len(img)) and (coluna_pixel + 16 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -2][img[coluna_pixel+ 16]]] += 1
                contador_pontos += 1
            if (linha_pixel + -10 < len(img)) and (coluna_pixel + 12 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -10][img[coluna_pixel+ 12]]] += 1
                contador_pontos += 1
            if (linha_pixel + -14 < len(img)) and (coluna_pixel + 8 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -14][img[coluna_pixel+ 8]]] += 1
                contador_pontos += 1
            if (linha_pixel + 0 < len(img)) and (coluna_pixel + 16 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 0][img[coluna_pixel+ 16]]] += 1
                contador_pontos += 1
            if (linha_pixel + -13 < len(img)) and (coluna_pixel + -9 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -13][img[coluna_pixel+ -9]]] += 1
                contador_pontos += 1
            if (linha_pixel + 12 < len(img)) and (coluna_pixel + -10 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 12][img[coluna_pixel+ -10]]] += 1
                contador_pontos += 1
            if (linha_pixel + -12 < len(img)) and (coluna_pixel + -10 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -12][img[coluna_pixel+ -10]]] += 1
                contador_pontos += 1
            if (linha_pixel + -11 < len(img)) and (coluna_pixel + -12 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -11][img[coluna_pixel+ -12]]] += 1
                contador_pontos += 1
            if (linha_pixel + -16 < len(img)) and (coluna_pixel + 1 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -16][img[coluna_pixel+ 1]]] += 1
                contador_pontos += 1
            if (linha_pixel + -13 < len(img)) and (coluna_pixel + 9 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -13][img[coluna_pixel+ 9]]] += 1
                contador_pontos += 1
            if (linha_pixel + 8 < len(img)) and (coluna_pixel + -14 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 8][img[coluna_pixel+ -14]]] += 1
                contador_pontos += 1
            if (linha_pixel + -14 < len(img)) and (coluna_pixel + -8 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -14][img[coluna_pixel+ -8]]] += 1
                contador_pontos += 1
            if (linha_pixel + 14 < len(img)) and (coluna_pixel + 8 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 14][img[coluna_pixel+ 8]]] += 1
                contador_pontos += 1
            if (linha_pixel + -1 < len(img)) and (coluna_pixel + -16 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -1][img[coluna_pixel+ -16]]] += 1
                contador_pontos += 1
            if (linha_pixel + -2 < len(img)) and (coluna_pixel + -16 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -2][img[coluna_pixel+ -16]]] += 1
                contador_pontos += 1
            if (linha_pixel + -8 < len(img)) and (coluna_pixel + 14 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -8][img[coluna_pixel+ 14]]] += 1
                contador_pontos += 1
            if (linha_pixel + -16 < len(img)) and (coluna_pixel + 3 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -16][img[coluna_pixel+ 3]]] += 1
                contador_pontos += 1
            if (linha_pixel + 7 < len(img)) and (coluna_pixel + 14 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 7][img[coluna_pixel+ 14]]] += 1
                contador_pontos += 1
            if (linha_pixel + -12 < len(img)) and (coluna_pixel + 10 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -12][img[coluna_pixel+ 10]]] += 1
                contador_pontos += 1
            if (linha_pixel + 9 < len(img)) and (coluna_pixel + -13 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 9][img[coluna_pixel+ -13]]] += 1
                contador_pontos += 1
            if (linha_pixel + 0 < len(img)) and (coluna_pixel + -16 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 0][img[coluna_pixel+ -16]]] += 1
                contador_pontos += 1
            if (linha_pixel + -5 < len(img)) and (coluna_pixel + 15 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -5][img[coluna_pixel+ 15]]] += 1
                contador_pontos += 1
            if (linha_pixel + 16 < len(img)) and (coluna_pixel + 1 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 16][img[coluna_pixel+ 1]]] += 1
                contador_pontos += 1
            if (linha_pixel + 15 < len(img)) and (coluna_pixel + -5 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 15][img[coluna_pixel+ -5]]] += 1
                contador_pontos += 1
            if (linha_pixel + 15 < len(img)) and (coluna_pixel + 4 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 15][img[coluna_pixel+ 4]]] += 1
                contador_pontos += 1
            if (linha_pixel + 16 < len(img)) and (coluna_pixel + 3 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 16][img[coluna_pixel+ 3]]] += 1
                contador_pontos += 1
            if (linha_pixel + -16 < len(img)) and (coluna_pixel + -1 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -16][img[coluna_pixel+ -1]]] += 1
                contador_pontos += 1
            if (linha_pixel + -16 < len(img)) and (coluna_pixel + -2 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -16][img[coluna_pixel+ -2]]] += 1
                contador_pontos += 1
            if (linha_pixel + -9 < len(img)) and (coluna_pixel + 13 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -9][img[coluna_pixel+ 13]]] += 1
                contador_pontos += 1
            if (linha_pixel + -15 < len(img)) and (coluna_pixel + 6 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -15][img[coluna_pixel+ 6]]] += 1
                contador_pontos += 1
            if (linha_pixel + 11 < len(img)) and (coluna_pixel + -12 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 11][img[coluna_pixel+ -12]]] += 1
                contador_pontos += 1
            if (linha_pixel + -14 < len(img)) and (coluna_pixel + 7 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -14][img[coluna_pixel+ 7]]] += 1
                contador_pontos += 1
            if (linha_pixel + 13 < len(img)) and (coluna_pixel + -9 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 13][img[coluna_pixel+ -9]]] += 1
                contador_pontos += 1
            if (linha_pixel + 6 < len(img)) and (coluna_pixel + -15 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 6][img[coluna_pixel+ -15]]] += 1
                contador_pontos += 1
            if (linha_pixel + -3 < len(img)) and (coluna_pixel + 16 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -3][img[coluna_pixel+ 16]]] += 1
                contador_pontos += 1
            if (linha_pixel + 13 < len(img)) and (coluna_pixel + 9 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 13][img[coluna_pixel+ 9]]] += 1
                contador_pontos += 1
            if (linha_pixel + 15 < len(img)) and (coluna_pixel + 6 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 15][img[coluna_pixel+ 6]]] += 1
                contador_pontos += 1
            if (linha_pixel + -12 < len(img)) and (coluna_pixel + -11 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -12][img[coluna_pixel+ -11]]] += 1
                contador_pontos += 1
            if (linha_pixel + -16 < len(img)) and (coluna_pixel + 0 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -16][img[coluna_pixel+ 0]]] += 1
                contador_pontos += 1
            if (linha_pixel + 1 < len(img)) and (coluna_pixel + 16 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 1][img[coluna_pixel+ 16]]] += 1
                contador_pontos += 1
            if (linha_pixel + -5 < len(img)) and (coluna_pixel + -15 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -5][img[coluna_pixel+ -15]]] += 1
                contador_pontos += 1
            if (linha_pixel + 6 < len(img)) and (coluna_pixel + 15 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 6][img[coluna_pixel+ 15]]] += 1
                contador_pontos += 1
            if (linha_pixel + 12 < len(img)) and (coluna_pixel + 10 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 12][img[coluna_pixel+ 10]]] += 1
                contador_pontos += 1
            if (linha_pixel + 14 < len(img)) and (coluna_pixel + 7 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 14][img[coluna_pixel+ 7]]] += 1
                contador_pontos += 1
            if (linha_pixel + -8 < len(img)) and (coluna_pixel + -14 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -8][img[coluna_pixel+ -14]]] += 1
                contador_pontos += 1
            if (linha_pixel + 3 < len(img)) and (coluna_pixel + 16 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 3][img[coluna_pixel+ 16]]] += 1
                contador_pontos += 1
            if (linha_pixel + 4 < len(img)) and (coluna_pixel + 15 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 4][img[coluna_pixel+ 15]]] += 1
                contador_pontos += 1
            if (linha_pixel + 7 < len(img)) and (coluna_pixel + -14 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 7][img[coluna_pixel+ -14]]] += 1
                contador_pontos += 1
            if (linha_pixel + 16 < len(img)) and (coluna_pixel + -2 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 16][img[coluna_pixel+ -2]]] += 1
                contador_pontos += 1
            if (linha_pixel + 16 < len(img)) and (coluna_pixel + -1 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 16][img[coluna_pixel+ -1]]] += 1
                contador_pontos += 1
            if (linha_pixel + 10 < len(img)) and (coluna_pixel + 12 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 10][img[coluna_pixel+ 12]]] += 1
                contador_pontos += 1
            if (linha_pixel + -10 < len(img)) and (coluna_pixel + -12 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -10][img[coluna_pixel+ -12]]] += 1
                contador_pontos += 1
            if (linha_pixel + -16 < len(img)) and (coluna_pixel + 2 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -16][img[coluna_pixel+ 2]]] += 1
                contador_pontos += 1
            if (linha_pixel + -7 < len(img)) and (coluna_pixel + 14 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -7][img[coluna_pixel+ 14]]] += 1
                contador_pontos += 1
            if (linha_pixel + -3 < len(img)) and (coluna_pixel + -16 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -3][img[coluna_pixel+ -16]]] += 1
                contador_pontos += 1
            if (linha_pixel + -14 < len(img)) and (coluna_pixel + -7 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -14][img[coluna_pixel+ -7]]] += 1
                contador_pontos += 1
            if (linha_pixel + 1 < len(img)) and (coluna_pixel + -16 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 1][img[coluna_pixel+ -16]]] += 1
                contador_pontos += 1
            if (linha_pixel + 16 < len(img)) and (coluna_pixel + 0 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 16][img[coluna_pixel+ 0]]] += 1
                contador_pontos += 1
            if (linha_pixel + -15 < len(img)) and (coluna_pixel + -6 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -15][img[coluna_pixel+ -6]]] += 1
                contador_pontos += 1
            if (linha_pixel + 3 < len(img)) and (coluna_pixel + -16 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 3][img[coluna_pixel+ -16]]] += 1
                contador_pontos += 1
            if (linha_pixel + 14 < len(img)) and (coluna_pixel + -7 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 14][img[coluna_pixel+ -7]]] += 1
                contador_pontos += 1
            if (linha_pixel + -11 < len(img)) and (coluna_pixel + 12 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -11][img[coluna_pixel+ 12]]] += 1
                contador_pontos += 1
            if (linha_pixel + 15 < len(img)) and (coluna_pixel + -6 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 15][img[coluna_pixel+ -6]]] += 1
                contador_pontos += 1
            if (linha_pixel + 16 < len(img)) and (coluna_pixel + 2 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 16][img[coluna_pixel+ 2]]] += 1
                contador_pontos += 1
            if (linha_pixel + -16 < len(img)) and (coluna_pixel + -3 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -16][img[coluna_pixel+ -3]]] += 1
                contador_pontos += 1
            if (linha_pixel + -15 < len(img)) and (coluna_pixel + -4 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -15][img[coluna_pixel+ -4]]] += 1
                contador_pontos += 1
            if (linha_pixel + -15 < len(img)) and (coluna_pixel + 5 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -15][img[coluna_pixel+ 5]]] += 1
                contador_pontos += 1
            if (linha_pixel + 12 < len(img)) and (coluna_pixel + -11 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 12][img[coluna_pixel+ -11]]] += 1
                contador_pontos += 1
            if (linha_pixel + 4 < len(img)) and (coluna_pixel + -15 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 4][img[coluna_pixel+ -15]]] += 1
                contador_pontos += 1
            if (linha_pixel + -9 < len(img)) and (coluna_pixel + -13 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -9][img[coluna_pixel+ -13]]] += 1
                contador_pontos += 1
            if (linha_pixel + 5 < len(img)) and (coluna_pixel + -15 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 5][img[coluna_pixel+ -15]]] += 1
                contador_pontos += 1
            if (linha_pixel + -6 < len(img)) and (coluna_pixel + -15 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -6][img[coluna_pixel+ -15]]] += 1
                contador_pontos += 1
            if (linha_pixel + -7 < len(img)) and (coluna_pixel + -14 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -7][img[coluna_pixel+ -14]]] += 1
                contador_pontos += 1
            if (linha_pixel + -4 < len(img)) and (coluna_pixel + -15 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -4][img[coluna_pixel+ -15]]] += 1
                contador_pontos += 1
            if (linha_pixel + 5 < len(img)) and (coluna_pixel + 15 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 5][img[coluna_pixel+ 15]]] += 1
                contador_pontos += 1
            if (linha_pixel + 16 < len(img)) and (coluna_pixel + -3 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 16][img[coluna_pixel+ -3]]] += 1
                contador_pontos += 1
            if (linha_pixel + -6 < len(img)) and (coluna_pixel + 15 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -6][img[coluna_pixel+ 15]]] += 1
                contador_pontos += 1
            if (linha_pixel + 9 < len(img)) and (coluna_pixel + 13 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 9][img[coluna_pixel+ 13]]] += 1
                contador_pontos += 1
            if (linha_pixel + 8 < len(img)) and (coluna_pixel + 14 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 8][img[coluna_pixel+ 14]]] += 1
                contador_pontos += 1
            if (linha_pixel + 2 < len(img)) and (coluna_pixel + 16 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 2][img[coluna_pixel+ 16]]] += 1
                contador_pontos += 1
            if (linha_pixel + -4 < len(img)) and (coluna_pixel + 15 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -4][img[coluna_pixel+ 15]]] += 1
                contador_pontos += 1
            if (linha_pixel + 12 < len(img)) and (coluna_pixel + 11 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 12][img[coluna_pixel+ 11]]] += 1
                contador_pontos += 1
            if (linha_pixel + -12 < len(img)) and (coluna_pixel + 11 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + -12][img[coluna_pixel+ 11]]] += 1
                contador_pontos += 1
            if (linha_pixel + 11 < len(img)) and (coluna_pixel + 12 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 11][img[coluna_pixel+ 12]]] += 1
                contador_pontos += 1
            if (linha_pixel + 14 < len(img)) and (coluna_pixel + -8 < len(img[0])):
                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + 14][img[coluna_pixel+ -8]]] += 1
                contador_pontos += 1

    # Calcular Probabilidade de cada co-ocorrência
    for linha_pixel in range(tons):
        for coluna_pixel in range(tons):
            matriz[linha_pixel][coluna_pixel] /= contador_pontos
    return matriz

