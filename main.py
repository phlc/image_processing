# Biblioteca: skimage
# https://scikit-image.org/docs/0.19.x/
from array import array
import os
import numpy
from PIL import ImageTk
import PIL.Image

from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

from descritores_haralick import calculateHaralickDescriptorsForAllImages
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class main:
    def __init__(self, master):
        self.master = master
        self.imagePathOpened = ''

        # Configurações gerais
        self.corBackground = 'white'

        # Criação dos frames da interface
        self.frame_cabecalho = Frame(master, padx = 5, pady = 5)
        self.canvas = Canvas(self.master, width=500, height=500)
        
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
         
        
        menuOpcoes.add_command(label='Sair', command=self.master.destroy) 

        menuDiretorio = Menu(menu)
        menu.add_cascade(label='Diretórios', menu=menuDiretorio)
        menuDiretorio.add_command(label='Selecionar diretorio para treino', command=self.selectFilesDirectory) 
        menuDiretorio.add_command(label='Selecionar diretorio para teste', command=self.selectFilesDirectory) 

        menuImagem = Menu(menu)
        menu.add_cascade(label='Imagem', menu=menuImagem)
        menuImagem.add_command(label='Selecionar imagem', command=self.selectImages)
        
        


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

        # Abrir a imagem no canvas
        if(filenames):
            self.frame_inferior = Frame(self.master, padx = 5, pady = 5)
            self.frame_inferior.pack(side=BOTTOM)
            self.botao_calculo_descritores = Button(self.frame_inferior, text='Calcular descritores', width=15, command=lambda: calculateHaralickDescriptorsForAllImages(imagesPaths=self.imagePathOpened))
            self.botao_calculo_descritores.grid(row=1, column=4, padx=10, pady=5)
            
            self.imagePathOpened = filenames
            image = PIL.Image.open(filenames[0])
            # fazer resize da imagem só para exibir a imagem. Nos cálculos é utilizada a imagem com o tamanho original
            resized_image= image.resize((500,500))
            tkImage = ImageTk.PhotoImage(resized_image)
            # criar imagem no canvas e realizar o seu bind (ancoragem)
            openedImage = self.canvas.create_image((0,0), anchor=NW, image=tkImage)
            openedImage.pack(side = "center", fill = "both", expand = "yes")

            



if __name__ == '__main__':
    interface = Tk()
    main(interface)
    interface.title('Trabalho de Processamento de Imagens Digitais')
    interface.mainloop()