import gerador_matrizes as gm
import descritores_haralick as dh
import pickle
import numpy as np

# Calcular set de matrizes de todas imagens / diretorio default / número de tons default (argumento -> numero_tons)
# set_matrizes_todas_imagens = gm.calcula_matrizes_varias_imagens(gravar_arquivo="True")

# Carregar set_matrizes_todas_imagens  do arquivo dataset_matrizes.pkl
input = open('dataset_matrizes.pkl', 'rb')
set_matrizes_todas_imagens = np.array(pickle.load(input))
input.close()

# Calcular set de matrizes de uma imagem / número de tons default (argumento -> numero_tons)
set_matrizes_uma_imagem = gm.calcula_matrizes_uma_imagem(path="./imagens/1/p_d_left_cc(12).png")

# Calcular descritores para todas matrizes de todas imagens
descritores_todas_imagens = dh.calcula_descritores_varias_imagens(set_matrizes_todas_imagens)


# Calcular descritores para matrizes de uma única imagem
descritores_uma_imagem = dh.calcula_descritores_uma_imagem(set_matrizes_uma_imagem)


print(len(descritores_todas_imagens))
print(len(descritores_todas_imagens[0]))
print(len(descritores_todas_imagens[0][0]))
print(len(descritores_todas_imagens[0][0][0]))
