from math import log
import numpy as np
import matriz_circular

# Calcula Entropia, Homogeneidade, Energia e Contraste de Haralick
# @param matriz de co-ocorrência; Opções: homogeneidade, entropia, energia, contraste
# @return [homogeneidade, entropia, energia, contraste]
def __descritores(matriz, entropia=True, homogeneidade=True, energia=True, contraste=False ):
    # Inicializações
    descritores = []
    valor_entropia = 0.0
    valor_homogeneidade = 0.0
    valor_energia = 0.0
    valor_contraste = 0.0

    # Passar por cada pixel da imagem
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):

            # Calcular Entropia
            if (matriz[linha][coluna] > 0):
                valor_entropia -= matriz[linha][coluna] * log(matriz[linha][coluna], 2)

            # Calcular Homogeneidade
            valor_homogeneidade += matriz[linha][coluna] / (1 + abs(linha - coluna))

            # Calcular Energia
            valor_energia += matriz[linha][coluna] ** 2

            # Calcular Contraste
            valor_contraste += (linha - coluna) ** 2 * matriz[linha][coluna]
    
    # Criar lista de descritores de acordo com opções
    if(homogeneidade):
        descritores.append(valor_homogeneidade)
    if(entropia):
        descritores.append(valor_entropia)
    if(energia):
        descritores.append(valor_energia)
    if(contraste):
        descritores.append(valor_contraste)

    return descritores

# Calcula os descritores de Haralick para um conjunto de matrizes de várias imagens separadas por birads
# @param lista 3D de [imagem][matrizes][matriz]
# @return array de descritores de todas as imagens
def calcula_descritores_varias_imagens(set_matrizes, entropia=True, homogeneidade=True, energia=True, contraste=False):
    # Lista de lista de descritores para cada matriz
    set_descritores = []

    # Passa por cada matriz do conjunto de matrizes de cada imagem
    for birads in set_matrizes:
        set_birad = []
        for matrizes in birads:
            descritores_imagem = []
            for matriz in matrizes:
                    descritores_imagem.append(__descritores(matriz, entropia, homogeneidade, energia, contraste))
        
            set_birad.append(descritores_imagem)
        set_descritores.append(set_birad)

    return set_descritores


# Calcula os descritores de Haralick para um conjunto de matrizes uma imagem
# @param lista 2d de [matrizes][matriz] 
# @return array de descritores da imagem
def calcula_descritores_uma_imagem(matrizes, entropia=True, homogeneidade=True, energia=True, contraste=False):
    # Lista de descritores para cada matriz
    descritores_imagem = []

    # Passa por cada matriz das matrizes de uma imagem
    for matriz in matrizes:
            descritores_imagem.append(__descritores(matriz, entropia, homogeneidade, energia, contraste))

    return descritores_imagem
