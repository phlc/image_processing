# Biblioteca: skimage
# https://scikit-image.org/docs/0.19.x/
from array import array
import os
import numpy

from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

from descritores_haralick import calculateHaralickDescriptorsForAllImages
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
            descriptorsMatrix = []
            if(subdirectories):
                for index, subdirectory in enumerate(subdirectories):
                    descriptorsMatrix.append(subdirectory)
                    descriptorsMatrix[index] = []
                    imagesPathsList = os.listdir(filedirectory + '/' + subdirectory)
                    # filtrar os caminhos obtidos para obter somente arquivos .png e .jpg e então formatá-lo
                    filteredPaths = filter(lambda image: ".png" in image or ".jpg" in image, imagesPathsList)
                    formatedFilteredPaths = list(map(lambda path: filedirectory + '/' + subdirectory + '/' + path, filteredPaths))

                    # obter os descritores para as imagens por diretório
                    if(formatedFilteredPaths):  
                        descriptorsMatrix[index].append(calculateHaralickDescriptorsForAllImages(formatedFilteredPaths))


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