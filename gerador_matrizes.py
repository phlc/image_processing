import numpy as np
import os
import cv2
import pickle
import matriz_circular as mc


# Calcula todas as matrizes de co-ocorrência de todas as imagens de um diretório com 4 pastas de birads
# @param path do diretório, opção de salvar em arquivo
# @return lista de listas de birads cada um com a lista das matrizes de cada imagem no diretório
def calcula_matrizes_varias_imagens(diretorio="./imagens", gravar_arquivo=False):
    # Declarações
    BIRADS = ["1", "2", "3", "4"]
    dataset = [[], [], [], []] #uma lista de matrizes para cada imagem em cada birad

    count = 1 #contador para mostrar terminal

    # Passar pela pasta de cada Birad
    for birad in BIRADS:
        path = os.path.join(diretorio,birad)

        # Passar por cada imagem na pasta da Birad
        for image_name in os.listdir(path):

            # Testar tipo do arquivo
            if(not(image_name.endswith(".png") or image_name.endswith(".jpg" ))):
                continue

            #Abrir Imagem
            image = cv2.imread(os.path.join(path,image_name), 0)

            # Reamostrar imagem para 32 tons de cinza
            for i in range(len(image)):
                for j in range(len(image[0])):
                    image[i][j] = int(image[i][j]/255 * 31)  

            # Calcular descritores a partir das matrizes de coocorrência circulares C1, C2, C4, C8 e C16
            c1 = mc.c1(np.array(image), 32)
            c2 = mc.c2(np.array(image), 32)
            c4 = mc.c4(np.array(image), 32)
            c8 = mc.c8(np.array(image), 32)
            c16 = mc.c16(np.array(image), 32)

            # Inserir matrizes no dataset
            dataset[int(birad)-1].append([c1, c2, c4, c8, c16])
            print(count)
            count+=1

    # Gravar datatset
    if (gravar_arquivo):
        output = open('dataset_matrizes.pkl', 'wb')
        pickle.dump(dataset, output)

    return dataset

# Calcula todas as matrizes de co-ocorrência de uma imagem
# @param path da imagem
# @return lista das matrizes da imagem 
def calcula_matrizes_uma_imagem(path):
    
    # Testar tipo do arquivo
    if(not(path.endswith(".png") or path.endswith(".jpg" ))):
        return None

    # Abrir Imagem
    image = cv2.imread(path, 0)

    # Reamostrar imagem para 32 tons de cinza
    for i in range(len(image)):
        for j in range(len(image[0])):
            image[i][j] = int(image[i][j]/255 * 31)  

    # Calcular descritores a partir das matrizes de coocorrência circulares C1, C2, C4, C8 e C16
    c1 = mc.c1(np.array(image), 32)
    c2 = mc.c2(np.array(image), 32)
    c4 = mc.c4(np.array(image), 32)
    c8 = mc.c8(np.array(image), 32)
    c16 = mc.c16(np.array(image), 32)

    return[c1, c2, c4, c8, c16]

    