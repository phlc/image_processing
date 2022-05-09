from math import log
import numpy as np
import matriz_circular
from skimage import io

# Calcula Entropia, Homogeneidade, Energia e Contraste de Haralick
# @param matriz de co-ocorrência
# @return [homogeneidade, entropia, energia, contraste]
def allDescriptors(matriz):
    entropia = 0.0
    homogeneidade = 0.0
    energia = 0.0
    contraste = 0.0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
            if matriz[linha][coluna] > 0:
                entropia -= matriz[linha][coluna] * log(matriz[linha][coluna], 2)
            homogeneidade += matriz[linha][coluna] / (1 + abs(linha - coluna))
            energia += matriz[linha][coluna] ** 2
            contraste += (linha - coluna) ** 2 * matriz[linha][coluna]
    return [homogeneidade, entropia, energia, contraste]

# Chama a função que calcula os descritores para cada imagem
# @param caminhos de todas as imagens
# @return array de descritores de todas as imagens
def calculateHaralickDescriptorsForAllImages(imagesPaths):
    AllImagesHaralickDescriptors = []

    for imagePath in imagesPaths:
        image = io.imread(imagePath)

        AllImagesHaralickDescriptors.append(calculateHaralickDescriptors(image=image))

    return AllImagesHaralickDescriptors


# Função que calcula os descritores para cada imagem
# @param caminhos da imagem
# @return array de descritores da imagem
def calculateHaralickDescriptors(image):
    # Reamostrar imagem para 32 tons de cinza
    image = np.array(np.rint(((image / 255) * 31)), dtype=int)
    # Parâmetros: imagem, numero de tons
    # Retorna Matriz de co-ocorrência de tons de cinza
    # Calcular descritores a partir das matrizes de coocorrência circulares C1, C2, C4, C8 e C16
    C1CoocurencyMatrix = matriz_circular.c1(np.array(image), 32)
    C2CoocurencyMatrix = matriz_circular.c2(np.array(image), 32)
    C4CoocurencyMatrix = matriz_circular.c4(np.array(image), 32)
    C8CoocurencyMatrix = matriz_circular.c8(np.array(image), 32)
    C16CoocurencyMatrix = matriz_circular.c16(np.array(image), 32)

    # Parâmetros: Matriz de co-ocorrência
    # Cálculo de todos os descritores de Haralick utilizados (Homogeneidade, entropia, energia e contraste)
    allDescriptorsC1 = allDescriptors(C1CoocurencyMatrix)
    allDescriptorsC2 = allDescriptors(C2CoocurencyMatrix)
    allDescriptorsC4 = allDescriptors(C4CoocurencyMatrix)
    allDescriptorsC8 = allDescriptors(C8CoocurencyMatrix)
    allDescriptorsC16 = allDescriptors(C16CoocurencyMatrix)

    # [0] -> Homogeneidade, [1] -> Entropia, [2] -> Energia, [3] -> Contraste
    HaralickDescriptorsArray = [
        [allDescriptorsC1[0], allDescriptorsC2[0], allDescriptorsC4[0], allDescriptorsC8[0], allDescriptorsC16[0]],
        [allDescriptorsC1[1], allDescriptorsC2[1], allDescriptorsC4[1], allDescriptorsC8[1], allDescriptorsC16[1]],
        [allDescriptorsC1[2], allDescriptorsC2[2], allDescriptorsC4[2], allDescriptorsC8[2], allDescriptorsC16[2]],
        [allDescriptorsC1[3], allDescriptorsC2[3], allDescriptorsC4[3], allDescriptorsC8[3], allDescriptorsC16[3]]]

    return HaralickDescriptorsArray

    