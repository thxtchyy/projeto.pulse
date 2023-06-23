from tkinter import *
from tkinter import font
from tkinter import Tk
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title("pulse")  
root.geometry("800x600")

def janela_inicial():

    inicio = Toplevel(root)
    inicio.title("pulse")  
    inicio.geometry("800x600")
    inicio.resizable(width=FALSE, height=FALSE)
    # CRIAÇÃO DE LABEL COM A IMAGEM
    imagem_inicial = PhotoImage(file="pgn.inicial.png")
    label_inicial = Label(inicio, image=imagem_inicial)
    label_inicial.place(x=0, y=0, relwidth=1, relheight=1)
    # BOTÕES - PGN INICIAL
     
    bt01 = Button(inicio, text="objetivo", command=janela_objetivo)
    bt01.place(x=460, y=104, width=280, height=63)
    bt01.config(bg='#90ADC6', font=('Bahnschrift SemiLight', 25))
    bt02 = Button(inicio, text="neuróbico", command=janela_neurobico)
    bt02.place(x=460, y=269, width=280, height=63)
    bt02.config(bg='#90ADC6', font=('Bahnschrift SemiLight', 25))
    bt03 = Button(inicio, text="jogo", command=janela_logo)
    bt03.place(x=460, y=433, width=280, height=63)
    bt03.config(bg='#90ADC6', font=('Bahnschrift SemiLight', 25))
    #  bt03 = Button(pulse, bd=0, highlightthickness=0, fg='#000000')

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

def janela_logo():
    logo = Toplevel(root)
    logo.title("pulse")
    logo.geometry("800x600")

    # IMAGEM E CRIAÇÃO DE LABEL
    inicio_logo = PhotoImage(file="logoinicial.png")
    label_logo = Label(logo, image=inicio_logo)
    label_logo.place(x=0, y=0, relwidth=1, relheight=1)

    # BOTÕES E IMAGENS
    logo_bt01 = PhotoImage(file="btvoltar.logo.png") # voltar
    logo_voltar = Button(logo, image=logo_bt01, command=janela_inicial)
    logo_voltar.place(x=60, y= 392, width= 302, height=98)

    logo_bt02 = PhotoImage(file="btjogar.png") # jogar
    logo_jogar = Button(logo, image=logo_bt02, command=comecarlogo)
    logo_jogar.place(x=60, y= 437, width= 302, height=98)

class comecarlogo:
    def __init__(self, root):
        self.root = root
        self.root.title("pulse")
        self.root.geometry("800x600")
        self.score = 0
        self.current_question = 0

        # Lista de perguntas com suas respostas corretas
        self.questions = [
            {
                "image_path": "1twitter.png",
                "answer": "twitter"
            },
            {
                "image_path": "2mitsubishi.png",
                "answer": "Mitsubishi"
            },
            {
                "image_path": "3hk.png",
                "answer": "hello kitty"
            },
            {
                "image_path": "4pepsi.png",
                "answer": ["pepsi", "pepsi cola"]
            },
            {
                "image_path": "5pinterest.png",
                "answer": "pinterest"
            },
            {
                "image_path": "6photoshop.png",
                "answer": ["photoshop", "photo shop"]
            },
            {
                "image_path": "7apple.png",
                "answer": "apple"
            },
            {
                "image_path": "8formula1.png",
                "answer": ["formula 1", "fórmula 1"]
            },
            {
                "image_path": "9bitcoin.png",
                "answer": ["bitcoin", "bit"]
            },
            {
                "image_path": "10facebook.png",
                "answer": "facebook"
            },
            {
                "image_path": "11kfc.png",
                "answer": "kfc"
            },
            {
                "image_path": "12mortalkombat.png",
                "answer": "facebook"
            },
            {
                "image_path": "13shopee.png",
                "answer": "shopee"
            },
            {
                "image_path": "14lacoste.png",
                "answer": "lacoste"
            },
            {
                "image_path": "15pacman.png",
                "answer": ["pacman", "pac"]
            },
            {
                "image_path": "16barcelona.png",
                "answer": ["barça", "barcelona"]
            },
            {
                "image_path": "17history.png",
                "answer": ["history tv", "history"]
            },
            {
                "image_path": "18toyota.png",
                "answer": "toyota"
            },
            {
                "image_path": "19pokemon.png",
                "answer": "pokemon"
            },
            {
                "image_path": "20whatsapp.png",
                "answer": "whatsapp"
            },
            {
                "image_path": "21puma.png",
                "answer": "puma"
            },
            {
                "image_path": "22chicagobulls.png",
                "answer": ["chicago bulls", "chicago", "bulls"]
            },
            {
                "image_path": "23lg.png",
                "answer": "lg"
            },
            {
                "image_path": "24rolex.png",
                "answer": "rolex"
            }
        ]

        # Carregar a imagem de fundo da pergunta
        self.question_image = ImageTk.PhotoImage(Image.open(self.questions[self.current_question]["image_path"]))
        self.image_label = Label(root, image=self.question_image)
        self.image_label.pack()

        # Campo de texto para a resposta
        self.answer_entry = Entry(root, bg="#E9EAEC")
        self.answer_entry.place(x=43, y=294, width=393, height=72)

        # Botão de verificar
        bt_verif = PhotoImage(file="bt.verif.png")
        self.check_button = Button(root, image=bt_verif, command=self.check_answer)
        self.check_button.place(x=127, y=420, width=224, height=73)

        # Botão de pular
        bt_pular = PhotoImage(file="bt.pular.png")
        self.skip_button = Button(root, image=bt_pular, command=self.next_question)
        self.skip_button.place(x=540, y=420, width=156, height=73)

        # Caixa de texto para exibir a pontuação final
        self.score_label = Text(root, height=1, width=20)
        self.score_label.pack()


    def check_answer(self):
        user_answer = self.answer_entry.get().lower()
        correct_answer = self.questions[self.current_question]["answer"]

        if user_answer in correct_answer:
            self.score += 1
            messagebox.showinfo("Resposta", "Correta!")
        else:
            messagebox.showinfo("Resposta", "Incorreta!")

        self.next_question()

    def next_question(self):
        self.current_question += 1

        if self.current_question < len(self.questions):
            # Carregar a próxima imagem de fundo da pergunta
            self.question_image = ImageTk.PhotoImage(Image.open(self.questions[self.current_question]["image_path"]))
                                                                
comecarlogo(root)
root.mainloop()
