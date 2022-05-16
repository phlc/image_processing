# Biblioteca: skimage
# https://scikit-image.org/docs/0.19.x/
from array import array
from email import message
import os
import pickle
from tkinter.ttk import Treeview
import numpy as np
from PIL import ImageTk
import PIL.Image
import time

from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

from skimage import io

from descritores_haralick import calcula_descritores_uma_imagem, calcula_descritores_varias_imagens
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn

from gerador_matrizes import calcula_matrizes_uma_imagem, calcula_matrizes_varias_imagens
from ia_rede import classificar_rede, treinar_rede_neural
from ia_svm import classificar_svm, treinar_svm
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

        menuCoocor = Menu(menu)
        menuOpcoes.add_command(label='Sair', command=self.master.destroy)
        menu.add_cascade(label='Matrizes Treino', menu=menuCoocor)
        menuCoocor.add_command(label='Calcular Matrizes de co-ocorrência Treino', command=self.calcular_matrizes_teste)

        menuRede = Menu(menu)
        menu.add_cascade(label='Rede Neural', menu=menuRede)
        menuRede.add_command(label='Treinar', command=self.realizar_treino_rede_neural) 
        menuRede.add_command(label='Testar', command=self.testar_rede_neural) 

        menuSVM = Menu(menu)
        menu.add_cascade(label='SVM', menu=menuSVM)
        menuSVM.add_command(label='Treinar', command=self.realizar_treino_svm) 
        menuSVM.add_command(label='Testar', command=self.testar_svm) 

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

        self.botao_classificar_svm = Button(self.frame_inferior, text='Classificar (SVM)', width=15, command=self.classificar_imagem_svm )
        self.botao_classificar_svm.grid(row=1, column=4, padx=10, pady=5)

        self.botao_classificar_rede = Button(self.frame_inferior, text='Classificar (RN)', width=15, command=self.classificar_imagem_rede_neural )
        self.botao_classificar_rede.grid(row=0, column=4, padx=10, pady=5)


    def selecionar_diretorio_imagens(self): 
        # selecionar um diretorio de imagens
        fileDirectory = fd.askdirectory()
        if(fileDirectory):
            return fileDirectory




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
        self.descritoresImagemExibida = descritores

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
        tabelaDeDescritores['columns'] = ('Matriz de Co-ocorrência','Homogeneidade', 'Entropia', 'Energia', 'Contraste')

        tabelaDeDescritores.column("#0", width=0,  stretch=NO)
        tabelaDeDescritores.column("Matriz de Co-ocorrência",anchor=CENTER, width=140)
        tabelaDeDescritores.column("Homogeneidade",anchor=CENTER,width=120)
        tabelaDeDescritores.column("Entropia",anchor=CENTER,width=120)
        tabelaDeDescritores.column("Energia",anchor=CENTER,width=120)
        tabelaDeDescritores.column("Contraste",anchor=CENTER,width=120)

        # Criação do cabeçalho da tabela
        tabelaDeDescritores.heading("#0",text="",anchor=CENTER)
        tabelaDeDescritores.heading("Matriz de Co-ocorrência",text="Matriz de Co-ocorrência",anchor=CENTER)
        tabelaDeDescritores.heading("Homogeneidade",text="Homogeneidade",anchor=CENTER)
        tabelaDeDescritores.heading("Entropia",text="Entropia",anchor=CENTER)
        tabelaDeDescritores.heading("Energia",text="Energia",anchor=CENTER)
        tabelaDeDescritores.heading("Contraste",text="Contraste",anchor=CENTER)

        # Populando a tabela com os dados dos descritores
        tabelaDeDescritores.insert(parent='',index='end',iid=0,text='',
        values=('C1',descritores[0][0],descritores[0][1],descritores[0][2]))
        tabelaDeDescritores.insert(parent='',index='end',iid=1,text='',
        values=('C2',descritores[1][0],descritores[1][1],descritores[1][2]))
        tabelaDeDescritores.insert(parent='',index='end',iid=2,text='',
        values=('C4',descritores[2][0],descritores[2][1],descritores[2][2]))
        tabelaDeDescritores.insert(parent='',index='end',iid=3,text='',
        values=('C8',descritores[3][0],descritores[3][1],descritores[3][2]))
        tabelaDeDescritores.insert(parent='',index='end',iid=4,text='',
        values=('C16',descritores[4][0],descritores[4][1],descritores[4][2]))

        tabelaDeDescritores.pack()
        

    def reamostrar_imagem(self):
        self.numeroDeTons = self.slider_reamostragem.get() - 1
        imagem = io.imread(self.caminhoDaImagem[0])
        imagem = np.array(imagem)
        maiorTom = imagem.max()

        # Reamostrar imagem para 32 tons de cinza
        for i in range(len(imagem)):
            for j in range(len(imagem)):
                imagem[i][j] = int(imagem[i][j]/maiorTom * (self.numeroDeTons))

        imagemReamostrada = plt.imshow(imagem, cmap='gray', vmax=(self.numeroDeTons))
        plt.colorbar(imagemReamostrada)
        plt.show()


    def obter_descritores_das_imagens(self, matrizesDeTodasAsImagens):
        try:
            descritoresTodasAsImagens_arquivo = open("dados\\dataset.pkl", "rb")
            descritoresTodasAsImagens = np.array(pickle.load(descritoresTodasAsImagens_arquivo))
            descritoresTodasAsImagens_arquivo.close()
        except:
            showinfo(message="Obtendo descritores...")
            descritoresTodasAsImagens = calcula_descritores_varias_imagens(matrizesDeTodasAsImagens)
        return descritoresTodasAsImagens


    def obter_matrizes_coocorrencia(self):
        try:
            matrizesDeTodasAsImagens_arquivo = open("dados\\dataset_matrizes.pkl", "rb")
            matrizesDeTodasAsImagens = np.array(pickle.load(matrizesDeTodasAsImagens_arquivo))
            matrizesDeTodasAsImagens_arquivo.close()

        except:
            diretorioImagens = self.selecionar_diretorio_imagens()
            showinfo(message="Obtendo matrizes de co-ocorrência...")
            matrizesDeTodasAsImagens = calcula_matrizes_varias_imagens(diretorioImagens, self.numeroDeTons)
        return matrizesDeTodasAsImagens

    
    def realizar_treino_svm(self):
        matrizesDeTodasAsImagens = self.obter_matrizes_coocorrencia()
        descritoresTodasAsImagens = self.obter_descritores_das_imagens(matrizesDeTodasAsImagens)
        
        [modelo, metricas] = treinar_svm(descritores_todas_imagens=descritoresTodasAsImagens, numero_descritores=3, gravar_svm=True)

        self.modelo_svm = modelo
        self.metricas_svm = metricas
        print(self.metricas_svm)


    def testar_svm(self):
        if(self.metricas_svm):
            matrizFormatada = pd.DataFrame(self.metricas_svm[0], range(1, 5), range(1, 5))
            plt.figure(figsize=(4,4))
            plt.title("Matriz de confusão")
            sn.set(font_scale=1.4) 
            sn.heatmap(matrizFormatada, annot=True, annot_kws={"size": 16}) 
            plt.show()

    
    def realizar_treino_rede_neural(self):
        matrizesDeTodasAsImagens = self.obter_matrizes_coocorrencia()
        descritoresTodasAsImagens = self.obter_descritores_das_imagens(matrizesDeTodasAsImagens)
        
        [modelo, metricas] = treinar_rede_neural(descritores_todas_imagens=descritoresTodasAsImagens, numero_descritores=3, gravar_rede=True)

        self.modelo_rede = modelo
        self.metricas_rede = metricas
        print(self.metricas_rede)

    def calcular_matrizes_teste(self):
        diretorioImagens = self.selecionar_diretorio_imagens()
        showinfo(message="Calculando matrizes de co-ocorrência...")
        matrizesDeTodasAsImagens = calcula_matrizes_varias_imagens(diretorioImagens, self.numeroDeTons)
        showinfo(message="Matrizes de co-ocorrência calculadas com sucesso!")


    def testar_rede_neural(self):
        if(self.metricas_rede):
            matrizFormatada = pd.DataFrame(self.metricas_rede[0], range(1, 5), range(1, 5))
            plt.figure(figsize=(4,4))
            sn.set(font_scale=1.4) 
            sn.heatmap(matrizFormatada, annot=True, annot_kws={"size": 16}) 
            plt.show()


    def classificar_imagem_svm(self):
        classeDaImagem = classificar_svm(modelo_svm=self.modelo_svm, descritores=self.descritoresImagemExibida, numero_descritores=3)
        mensagem = "A imagem pertence à classe de BIRAD " + str(classeDaImagem)
        showinfo(message=mensagem)


    def classificar_imagem_rede_neural(self):
        classeDaImagem = classificar_rede(modelo_rede=self.modelo_rede, descritores=self.descritoresImagemExibida, numero_descritores=3)
        mensagem = "A imagem pertence à classe de BIRAD " + str(classeDaImagem)
        showinfo(message=mensagem)


if __name__ == '__main__':
    interface = Tk()
    main(interface)
    interface.title('Trabalho de Processamento de Imagens Digitais')
    interface.mainloop()