# Biblioteca: skimage
# https://scikit-image.org/docs/0.19.x/
from array import array
import os
from tkinter.ttk import Treeview
import numpy
from PIL import ImageTk
import PIL.Image
import time

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
        self.canvas = Canvas(self.master, width=500, height=500, background=self.corBackground)

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
        
        # Criação do frame e do botão para calcular os descritores da imagem selecionada
        self.frame_inferior = Frame(self.master, padx = 5, pady = 5)
        self.frame_inferior.pack(side=BOTTOM)
        self.botao_calculo_descritores = Button(self.frame_inferior, text='Calcular descritores', width=15, command=lambda: self.exhibitImageDescriptors(imagePath=self.imagePathOpened))
        self.botao_calculo_descritores.grid(row=1, column=4, padx=10, pady=5)


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
            self.imagePathOpened = filenames
            image = PIL.Image.open(filenames[0])
            # fazer resize da imagem só para exibir a imagem. Nos cálculos é utilizada a imagem com o tamanho original
            resized_image= image.resize((500,500))
            tkImage = ImageTk.PhotoImage(resized_image)
            # criar imagem no canvas e realizar o seu bind (ancoragem)
            openedImage = self.canvas.create_image((0,0), anchor=NW, image=tkImage)
            openedImage.pack(side = "center", fill = "both", expand = "yes")

            
    def exhibitImageDescriptors(self, imagePath):
        # Obtenção dos descritores de Haralick para a imagem selecionada
        startTime = time.time()
        descriptors = calculateHaralickDescriptorsForAllImages(imagesPaths=imagePath)[0]
        totalTime = "Tempo de execução: {:.2f} segundos\n".format(time.time() - startTime) 

        # Criação da janela auxiliar para a exibição da tabela de descritores
        descriptorsWindow = Toplevel(self.master)
        descriptorsWindow.title("Descritores de Haralick da imagem selecionada")
        descriptorsWindow.geometry("630x180")
        
        # Criação do frame de informações de execução
        execution_frame = Frame(descriptorsWindow)
        execution_frame.pack()

        # Criação do frame da tabela
        table_frame = Frame(descriptorsWindow)
        table_frame.pack()

        # Label de informação do tempo de execução
        time_label = Label(execution_frame, text=totalTime)
        time_label.grid(row=0, column=0, padx=10)

        # Instanciação da tabela e definição das suas colunas
        descriptorsTable = Treeview(table_frame)
        descriptorsTable['columns'] = ('Matriz de Coocorrência','Homogeneidade', 'Entropia', 'Energia', 'Contraste')

        descriptorsTable.column("#0", width=0,  stretch=NO)
        descriptorsTable.column("Matriz de Coocorrência",anchor=CENTER, width=140)
        descriptorsTable.column("Homogeneidade",anchor=CENTER,width=120)
        descriptorsTable.column("Entropia",anchor=CENTER,width=120)
        descriptorsTable.column("Energia",anchor=CENTER,width=120)
        descriptorsTable.column("Contraste",anchor=CENTER,width=120)

        # Criação do cabeçalho da tabela
        descriptorsTable.heading("#0",text="",anchor=CENTER)
        descriptorsTable.heading("Matriz de Coocorrência",text="Matriz de Coocorrência",anchor=CENTER)
        descriptorsTable.heading("Homogeneidade",text="Homogeneidade",anchor=CENTER)
        descriptorsTable.heading("Entropia",text="Entropia",anchor=CENTER)
        descriptorsTable.heading("Energia",text="Energia",anchor=CENTER)
        descriptorsTable.heading("Contraste",text="Contraste",anchor=CENTER)

        # Populando a tabela com os dados dos descritores
        descriptorsTable.insert(parent='',index='end',iid=0,text='',
        values=('C1',descriptors[0][0],descriptors[1][0],descriptors[2][0], descriptors[3][0]))
        descriptorsTable.insert(parent='',index='end',iid=1,text='',
        values=('C2',descriptors[0][1],descriptors[1][1],descriptors[2][1], descriptors[3][1]))
        descriptorsTable.insert(parent='',index='end',iid=2,text='',
        values=('C4',descriptors[0][2],descriptors[1][2],descriptors[2][2], descriptors[3][2]))
        descriptorsTable.insert(parent='',index='end',iid=3,text='',
        values=('C8',descriptors[0][3],descriptors[1][3],descriptors[2][3], descriptors[3][3]))
        descriptorsTable.insert(parent='',index='end',iid=4,text='',
        values=('C16',descriptors[0][4],descriptors[1][4],descriptors[2][4], descriptors[3][4]))

        descriptorsTable.pack()




if __name__ == '__main__':
    interface = Tk()
    main(interface)
    interface.title('Trabalho de Processamento de Imagens Digitais')
    interface.mainloop()