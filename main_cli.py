import gerador_matrizes as gm
import descritores_haralick as dh
import ia_svm
import pickle
import numpy as np
from sklearn import svm
from sklearn import metrics

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

# Treinar uma SVM (argumento numero_descritores Default)
(modelo_svm, metricas) = ia_svm.treinar_svm(descritores_todas_imagens=descritores_todas_imagens, gravar_svm=True)

# Classificar uma imagem (a partir de seus descritores)
classe = ia_svm.classificar_svm(modelo_svm, descritores_uma_imagem)

print(metricas)
print(classe)
