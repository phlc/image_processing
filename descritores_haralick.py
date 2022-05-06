from math import log
import numpy as np
import matriz_circular
from skimage import io


# Calcula Entropia de Haralick
# @param matriz de co-ocorrência
# @return entropia
def entropia(matriz):
    resultado = 0.0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
            if matriz[linha][coluna] > 0:
                resultado += matriz[linha][coluna] * log(matriz[linha][coluna], 2)
    return -resultado


# Calcula Homogeneidade de Haralick
# @param matriz de co-ocorrência
# @return homogeneidade
def homogeneidade(matriz):
    resultado = 0.0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
            resultado += matriz[linha][coluna] / (1 + abs(linha - coluna))
    return resultado


# Calcula Energia de Haralick
# @param matriz de co-ocorrência
# @return energia
def energia(matriz):
    resultado = 0.0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
            resultado+= matriz[linha][coluna]**2
    return resultado


# Calcula Contraste de Haralick
# @param matriz de co-ocorrência
# @return contraste
def contraste(matriz):
    resultado = 0.0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
            resultado+= (linha - coluna)**2 * matriz[linha][coluna]
    return resultado


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
    # Cálculo de homogeneidade
    HomogeneityC1  = homogeneidade(C1CoocurencyMatrix)
    HomogeneityC2  = homogeneidade(C2CoocurencyMatrix)
    HomogeneityC4  = homogeneidade(C4CoocurencyMatrix)
    HomogeneityC8  = homogeneidade(C8CoocurencyMatrix)
    HomogeneityC16 = homogeneidade(C16CoocurencyMatrix)

    # Parâmetros: Matriz de co-ocorrência
    # Cálculo de entropia
    EntropyC1  = entropia(C1CoocurencyMatrix)
    EntropyC2  = entropia(C2CoocurencyMatrix)
    EntropyC4  = entropia(C4CoocurencyMatrix)
    EntropyC8  = entropia(C8CoocurencyMatrix)
    EntropyC16 = entropia(C16CoocurencyMatrix)

    # Parâmetros: Matriz de co-ocorrência
    # Cálculo de energia
    EnergyC1  = energia(C1CoocurencyMatrix)
    EnergyC2  = energia(C2CoocurencyMatrix)
    EnergyC4  = energia(C4CoocurencyMatrix)
    EnergyC8  = energia(C8CoocurencyMatrix)
    EnergyC16 = energia(C16CoocurencyMatrix)

    # Parâmetros: Matriz de co-ocorrência
    # Cálculo de contraste
    ContrastC1  = contraste(C1CoocurencyMatrix)
    ContrastC2  = contraste(C2CoocurencyMatrix)
    ContrastC4  = contraste(C4CoocurencyMatrix)
    ContrastC8  = contraste(C8CoocurencyMatrix)
    ContrastC16 = contraste(C16CoocurencyMatrix)


    HaralickDescriptorsArray = [[HomogeneityC1, HomogeneityC2, HomogeneityC4, HomogeneityC8, HomogeneityC16], 
                                [EntropyC1, EntropyC2, EntropyC4, EntropyC8, EntropyC16],
                                [EnergyC1, EnergyC2, EnergyC4, EnergyC8, EnergyC16],
                                [ContrastC1, ContrastC2, ContrastC4, ContrastC8, ContrastC16]]
    
    print(HaralickDescriptorsArray)
    return HaralickDescriptorsArray
    