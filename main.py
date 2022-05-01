# Biblioteca: skimage
# https://scikit-image.org/docs/0.19.x/
import os
import numpy
from skimage.feature import greycomatrix, greycoprops
from skimage import io
from math import log

from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class main:
    def __init__(self, master):
        self.master = master

        # Configurações gerais
        self.corBackground = 'white'

        # Criação dos frames da interface
        self.frame_cabecalho = Frame(master, padx = 5, pady = 5)
        self.canvas = Canvas(self.master, width=500, height=400, bg=self.corBackground)
        self.drawWidgets()


    # Função para calcular entropia de uma matriz de co-ocorrência de tons de cinza
    # Parâmetros: GCHistogram[li][lj][ld][la], li, lj, ld, la
    # Retorna matriz de entropia calculada [Ângulo m, Distância n]
    def entropy(self, GCHistogram, li, lj, ld, la):
        entropyMatrix = [[0 for x in range(ld)] for y in range(la)]
        for i in range(li):
            for j in range(lj):
                for d in range(ld):
                    for a in range(la):
                        if(GCHistogram[i][j][d][a] > 0.0):
                            entropyMatrix[a][d] -= GCHistogram[i][j][d][a] * log(GCHistogram[i][j][d][a], 2)
        return entropyMatrix

    def calculateHaralickDescriptorsForAllImages(self, imagesPaths):

        for imagePath in imagesPaths:
            # formatedPath = imagePath.replace("\\", "/")
            # print("formatedPath:", formatedPath)
            image = io.imread(imagePath)

            # Calcular descritores a partir de matriz de co-ocorrência circular com distância 1
            # Ângulos (Graus): 0, 90, 180, 270
            print("Matriz de co-corrência D1")
            self.calculateHaralickDescriptors(image=image, distance=[1], angles=[0, numpy.pi / 4, numpy.pi / 2, 3 * numpy.pi / 4]);

            #self.calculateHaralickDescriptors(image=image, distance=[1], angles=[0]);

    def calculateHaralickDescriptors(self, image, distance, angles):
        # Reamostrar imagem para 32 tons de cinza
        image = numpy.array(numpy.rint(((image / 255) * 32)), dtype=int)
        
        # github.com/scikit-image/scikit-image/blob/00177e14097237ef20ed3141ed454bc81b308f82/skimage/feature/texture.py#L15
        # Parâmetros: imagem, distâncias [], ângulos [], levels = 256, Simetria = false, Normalizar em 1 = true
        # Retorna Histograma de co-ocorrência de tons de cinza
        GCHistogram = greycomatrix(image, distance, angles, 32, False, True)

        # github.com/scikit-image/scikit-image/blob/00177e14097237ef20ed3141ed454bc81b308f82/skimage/feature/texture.py#L159
        # Parâmetros: Matriz de co-ocorrência, Propriedade calculada
        # Retorna matriz de propriedade calculada [Ângulo m, Distância n]

        # Cálculo de homogeneidade
        Homogeneity = greycoprops(GCHistogram, 'homogeneity')

        # Cálculo de energia
        Energy = greycoprops(GCHistogram, 'energy')

        # Cálculo de entropia
        Entropy = self.entropy(GCHistogram, len(GCHistogram), len(GCHistogram[0]), len(GCHistogram[0][0]), len(GCHistogram[0][0][0]))
        print(angles, distance)
        print('Homogeneity: ', Homogeneity)
        print('Energy: ', Energy)
        print('Entropy: ', Entropy)

    def drawWidgets(self):
        Label(self.frame_cabecalho, text='Alunos: Ana Laura Fernandes, Larissa Gomes, Pedro Henrique Lima',font=('arial 8')).grid(row=0, column=0)
        
        self.frame_cabecalho.pack(side=TOP)
        
        self.canvas.pack(fill=BOTH, expand=True)

        # Definição dos menus da interface gráfica
        menu = Menu(self.master)
        self.master.config(menu=menu)

        menuOpcoes = Menu(menu)
        menu.add_cascade(label='Opções', menu=menuOpcoes)
        menuOpcoes.add_command(label='Selecionar imagens', command=self.selectImages) 
        menuOpcoes.add_command(label='Selecionar diretorio', command=self.selectFilesDirectory) 
        menuOpcoes.add_command(label='Sair', command=self.master.destroy) 


    def selectFilesDirectory(self): 
        # selecionar um diretorio de imagens
        filedirectory = fd.askdirectory()
        if(filedirectory):
            # obter os subdiretórios do diretório selecionado
            subdirectories = os.listdir(filedirectory)
            
            if(subdirectories):
                # filtrar os caminhos obtidos para obter somente arquivos .png e .jpg e então formatá-lo
                for subdirectory in subdirectories:
                    imagesPathsList = os.listdir(filedirectory + '/' + subdirectory)
                    filteredPaths = filter(lambda image: ".png" in image or ".jpg" in image, imagesPathsList)
                    formatedFilteredPaths = map(lambda path: filedirectory + '/' + subdirectory + '/' + path, filteredPaths)

                    # obter os descritores para as imagens
                    if(formatedFilteredPaths):  
                        self.calculateHaralickDescriptorsForAllImages(formatedFilteredPaths)


    def selectImages(self):
        # obter imagens .png e .jpg
        filetypes = (
        ('image files', '*.png'),
        ('image files', '*.jpg'),
        ('All files', '*.*')
        )

        filenames = fd.askopenfilenames(
            title='Open files',
            initialdir='/',
            filetypes=filetypes)

        # calcular os descritores para as imagens
        if(filenames):
            self.calculateHaralickDescriptorsForAllImages(imagesPaths=filenames)


if __name__ == '__main__':
    interface = Tk()
    main(interface)
    interface.title('Trabalho de Processamento de Imagens Digitais')
    interface.mainloop()