# Biblioteca: skimage
# https://scikit-image.org/docs/0.19.x/
from array import array
import os
from tkinter.ttk import Treeview
import numpy as np
from PIL import ImageTk
import PIL.Image
import time

from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

from skimage import io

from descritores_haralick import calcula_descritores_uma_imagem
import matplotlib.pyplot as plt

from gerador_matrizes import calcula_matrizes_uma_imagem
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class main:
    def __init__(self, master):
        self.master = master
        self.caminhoDaImagem = ''
        self.numeroDeTons = 32

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

        menuRede = Menu(menu)
        menu.add_cascade(label='Rede Neural', menu=menuRede)
        menuRede.add_command(label='Treinar', command=self.selectFilesDirectory) 
        menuRede.add_command(label='Testar', command=self.selectFilesDirectory) 

        menuSVM = Menu(menu)
        menu.add_cascade(label='SVM', menu=menuRede)
        menuSVM.add_command(label='Treinar', command=self.selectFilesDirectory) 
        menuSVM.add_command(label='Testar', command=self.selectFilesDirectory) 

        menuImagem = Menu(menu)
        menu.add_cascade(label='Imagem', menu=menuImagem)
        menuImagem.add_command(label='Selecionar imagem', command=self.selectImages)
        
        # Criação do frame e do botão para calcular os descritores da imagem selecionada
        self.frame_inferior = Frame(self.master, padx = 5, pady = 5)
        self.frame_inferior.pack(side=BOTTOM)
        self.botao_calculo_descritores = Button(self.frame_inferior, text='Calcular descritores', width=15, command=lambda: self.exibir_descritores_imagem(imagePath=self.caminhoDaImagem))
        self.botao_calculo_descritores.grid(row=1, column=3, padx=10, pady=5)

        self.slider_reamostragem = Scale(self.frame_inferior, from_=2, to=32, orient=HORIZONTAL)
        self.slider_reamostragem.set(32)
        self.slider_reamostragem.grid(row=0, column=2, padx=10, pady=5)

        self.botao_reamostrar = Button(self.frame_inferior, text='Reamostrar', width=15, command=self.reamostrar_imagem)
        self.botao_reamostrar.grid(row=1, column=2, padx=10, pady=5)

        self.botao_classificar_svm = Button(self.frame_inferior, text='Classificar (SVM)', width=15, command=lambda: self.exibir_descritores_imagem(imagePath=self.caminhoDaImagem))
        self.botao_classificar_svm.grid(row=1, column=4, padx=10, pady=5)

        self.botao_classificar_rede = Button(self.frame_inferior, text='Classificar (RN)', width=15, command=lambda: self.exibir_descritores_imagem(imagePath=self.caminhoDaImagem))
        self.botao_classificar_rede.grid(row=0, column=4, padx=10, pady=5)


    def selectFilesDirectory(self): 
        # selecionar um diretorio de imagens
        fileDirectory = fd.askdirectory()
        if(fileDirectory):
            return fileDirectory
            #chama função do Pedro

            # # obter os subdiretórios do diretório selecionado
            # subdirectories = os.listdir(filedirectory)
            # descriptorsMatrix = []
            # if(subdirectories):
            #     for index, subdirectory in enumerate(subdirectories):
            #         descriptorsMatrix.append(subdirectory)
            #         descriptorsMatrix[index] = []
            #         imagesPathsList = os.listdir(filedirectory + '/' + subdirectory)
            #         # filtrar os caminhos obtidos para obter somente arquivos .png e .jpg e então formatá-lo
            #         filteredPaths = filter(lambda image: ".png" in image or ".jpg" in image, imagesPathsList)
            #         formatedFilteredPaths = list(map(lambda path: filedirectory + '/' + subdirectory + '/' + path, filteredPaths))

            #         # obter os descritores para as imagens por diretório
            #         if(formatedFilteredPaths):  
            #             descriptorsMatrix[index].append(calculateHaralickDescriptorsForAllImages(formatedFilteredPaths))





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
            self.caminhoDaImagem = filenames
            image = PIL.Image.open(filenames[0])
            # fazer resize da imagem só para exibir a imagem. Nos cálculos é utilizada a imagem com o tamanho original
            resized_image= image.resize((500,500))
            tkImage = ImageTk.PhotoImage(resized_image)
            # criar imagem no canvas e realizar o seu bind (ancoragem)
            openedImage = self.canvas.create_image((0,0), anchor=NW, image=tkImage)
            openedImage.pack(side = "center", fill = "both", expand = "yes")

            
    def exibir_descritores_imagem(self, imagePath):
        print(imagePath)
        # Obtenção dos descritores de Haralick para a imagem selecionada
        tempoInicial = time.time()
        matrizesCoocorrencia = calcula_matrizes_uma_imagem(str(imagePath[0]))
        descritores = calcula_descritores_uma_imagem(matrizes=matrizesCoocorrencia)
        totalTime = "Tempo de execução: {:.2f} segundos\n".format(time.time() - tempoInicial) 

        # Criação da janela auxiliar para a exibição da tabela de descritores
        janelaDeDescritores = Toplevel(self.master)
        janelaDeDescritores.title("Descritores de Haralick da imagem selecionada")
        janelaDeDescritores.geometry("630x180")
        
        # Criação do frame de informações de execução
        execution_frame = Frame(janelaDeDescritores)
        execution_frame.pack()

        # Criação do frame da tabela
        table_frame = Frame(janelaDeDescritores)
        table_frame.pack()

        # Label de informação do tempo de execução
        time_label = Label(execution_frame, text=totalTime)
        time_label.grid(row=0, column=0, padx=10)

        # Instanciação da tabela e definição das suas colunas
        tabelaDeDescritores = Treeview(table_frame)
        tabelaDeDescritores['columns'] = ('Matriz de Coocorrência','Homogeneidade', 'Entropia', 'Energia', 'Contraste')

        tabelaDeDescritores.column("#0", width=0,  stretch=NO)
        tabelaDeDescritores.column("Matriz de Coocorrência",anchor=CENTER, width=140)
        tabelaDeDescritores.column("Homogeneidade",anchor=CENTER,width=120)
        tabelaDeDescritores.column("Entropia",anchor=CENTER,width=120)
        tabelaDeDescritores.column("Energia",anchor=CENTER,width=120)
        tabelaDeDescritores.column("Contraste",anchor=CENTER,width=120)

        # Criação do cabeçalho da tabela
        tabelaDeDescritores.heading("#0",text="",anchor=CENTER)
        tabelaDeDescritores.heading("Matriz de Coocorrência",text="Matriz de Coocorrência",anchor=CENTER)
        tabelaDeDescritores.heading("Homogeneidade",text="Homogeneidade",anchor=CENTER)
        tabelaDeDescritores.heading("Entropia",text="Entropia",anchor=CENTER)
        tabelaDeDescritores.heading("Energia",text="Energia",anchor=CENTER)
        tabelaDeDescritores.heading("Contraste",text="Contraste",anchor=CENTER)

        # Populando a tabela com os dados dos descritores
        tabelaDeDescritores.insert(parent='',index='end',iid=0,text='',
        values=('C1',descritores[0][0],descritores[0][1],descritores[0][2], descritores[0][3] ))
        tabelaDeDescritores.insert(parent='',index='end',iid=1,text='',
        values=('C2',descritores[1][0],descritores[1][1],descritores[1][2], descritores[1][3]))
        tabelaDeDescritores.insert(parent='',index='end',iid=2,text='',
        values=('C4',descritores[2][0],descritores[2][1],descritores[2][2], descritores[2][3]))
        tabelaDeDescritores.insert(parent='',index='end',iid=3,text='',
        values=('C8',descritores[3][0],descritores[3][1],descritores[3][2], descritores[3][3]))
        tabelaDeDescritores.insert(parent='',index='end',iid=4,text='',
        values=('C16',descritores[4][0],descritores[4][1],descritores[4][2], descritores[4][3]))

        tabelaDeDescritores.pack()
        

    def reamostrar_imagem(self):
        self.numeroDeTons = self.slider_reamostragem.get() - 1
        imagem = io.imread(self.caminhoDaImagem[0])
        imagem = np.array(imagem)
        maiorTom = imagem.max()
        # print(maiorTom)
        # Reamostrar imagem para 32 tons de cinza
        for i in range(len(imagem)):
            for j in range(len(imagem)):
                imagem[i][j] = int(imagem[i][j]/maiorTom * (self.numeroDeTons))

        imagemReamostrada = plt.imshow(imagem, cmap='gray', vmax=(self.numeroDeTons))
        plt.colorbar(imagemReamostrada)
        plt.show()

    def treinar_rede_neural(self):
        return



if __name__ == '__main__':
    interface = Tk()
    main(interface)
    interface.title('Trabalho de Processamento de Imagens Digitais')
    interface.mainloop()