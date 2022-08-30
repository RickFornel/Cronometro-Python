from cgitb import text
from ctypes.wintypes import HCOLORSPACE
from tkinter import *
from tkinter import ttk

import pyglet
pyglet.font.add_file("digital-7.ttf")

# cores

preto = "#3d3d3d"
branco = "#fafcff"
verde = "#21c25c"
vermelho = "#eb463b"
cinza = "#dedcdc"
azul = "#3080f0"

# criando janela 

janela = Tk()
janela.title("")
janela.geometry("460x180")
janela.resizable(width=False, height=False)
janela.config(bg=preto)

# frame

frame_pricipal = Frame(janela, bg=preto, width=460, height=250)
frame_pricipal.grid(row=0, column=0, sticky=NSEW)

# funções

global contador, horas, hora

hora = "0:0:0"

contador = 0
minutos = 0
horas = 0
comando = False

def iniciar():
    
    global comando, contador, minutos, horas
    
    if comando:

        if contador < 60:
            label_relogio['text'] = str(horas) + ':' + str(minutos) + ':'+str(contador)
            label_relogio.after( 1000, iniciar )
            contador +=1 
        else: 
            contador = 1 
            minutos +=1
            label_relogio['text'] = str(horas) + ':' + str(minutos) + ':'+str(contador)
            iniciar()

        if minutos >= 60:
            minutos = 0
            horas +=1
            label_relogio['text'] = str(horas) +':' + str(minutos) + ':'+str(contador)
            iniciar()
                    
def start():
    global comando
    comando = True
    iniciar()

def stop():
    global comando
    comando = False

def clear():
    global comando, contador, minutos, hora
    contador = 0
    minutos = 0
    label_relogio["text"] = str(hora)

# label

label_relogio = Label(frame_pricipal, bg=preto, fg=azul, text=hora, font="digital-7 80",  anchor=CENTER, width=9, padx=5, justify=CENTER)
label_relogio.place(x=0, y=0)

# buttons

but_iniciar = Button(frame_pricipal, text= 'Iniciar', width=10, command=start)
but_iniciar.place(x=75, y=125)

but_pausar = Button(frame_pricipal, text= 'Pausar', width=10, command=stop)
but_pausar.place(x=175, y=125)

but_zerar = Button(frame_pricipal, text= 'Zerar', width=10, command=clear)
but_zerar.place(x=275, y=125)

janela.mainloop()