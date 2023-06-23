from tkinter import *
from tkinter import font
from tkinter import Tk
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title("pulse")  
root.geometry("800x600")
root.resizable(width=FALSE, height=FALSE)

def janela_inicial():

    inicio = Toplevel(root)
    inicio.title("pulse")  
    inicio.geometry("800x600")
    # CRIAÇÃO DE LABEL COM A IMAGEM
    imagem_inicial = PhotoImage(file="pgn.inicial.png")
    label_inicial = Label(root, image=imagem_inicial)
    label_inicial.place(x=0, y=0, relwidth=1, relheight=1)
    # BOTÕES - PGN INICIAL
    bt01 = Button(inicio, command= janela_objetivo)
    bt01.place(x=460, y=104, width=280, height=63)
    bt01.config(bg='#90ADC6', text="objetivo", font=('Bahnschrift SemiLight', 25))

    bt02 = Button(inicio, command= janela_neurobico)
    bt02.place(x=460, y=269, width=280, height=63)
    bt02.config(bg='#90ADC6', text="neuróbico", font=('Bahnschrift SemiLight', 25))

def janela_objetivo():
    objetivo = Toplevel(root)
    objetivo.title("pulse")
    objetivo.geometry("800x600")

    # IMAGEM E CRIAÇÃO DE LABEL
    img_objetivo = PhotoImage(file="objetivo.png")
    label_objetivo = Label(objetivo, image=img_objetivo)
    label_objetivo.place(x=0, y=0, relwidth=1, relheight=1)

    # BOTÃO VOLTAR
    obj_bt = PhotoImage(file="obj_btvoltar.png")
    bt_obj = Button(objetivo, image=obj_bt, command=janela_inicial)
    bt_obj.place(x=49, y= 496, width= 198, height=58)
    
def janela_neurobico():
    neuro = Toplevel(root)
    neuro.title("pulse")
    neuro.geometry("800x600")

    # IMAGEM E CRIAÇÃO DE LABEL
    img_neuro = PhotoImage(file="neurobico.png")
    label_neuro = Label(neuro, image=img_neuro)
    label_neuro.place(x=0, y=0, relwidth=1, relheight=1)

    # BOTÕES E IMAGENS
    neu_bt01 = PhotoImage(file="btvoltar_amarelo.png") # voltar
    neu_voltar = Button(neuro, image=neu_bt01, command=janela_inicial)
    neu_voltar.place(x=49, y= 496, width= 198, height=58)

    neu_bt02 = PhotoImage(file="bt_prox.png") # próximo
    neu_prox = Button(neuro, image=neu_bt02, command=janela_exercicios)
    neu_prox.place(x=49, y= 496, width= 198, height=58)  

def janela_exercicios():
    exer = Toplevel(root)
    exer.title("pulse")
    exer.geometry("800x600")

    # IMAGEM E CRIAÇÃO DE LABEL
    img_exer = PhotoImage(file="exercicios.png")
    label_exer = Label(exer, image=img_exer)
    label_exer.place(x=0, y=0, relwidth=1, relheight=1)

    # BOTÕES E IMAGENS
    exer_bt01 = PhotoImage(file="btvoltar_amarelo.png") # voltar
    exer_voltar = Button(exer, image=exer_bt01, command=janela_neurobico)
    exer_voltar.place(x=49, y= 496, width= 192, height=58)

    exer_bt02 = PhotoImage(file="exer_btinicio.png") # próximo
    exer_inicio = Button(exer, image=exer_bt02, command=janela_inicial)
    exer_inicio.place(x=557, y= 496, width= 192, height=58)

root.mainloop()
