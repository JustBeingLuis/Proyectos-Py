from pytube import YouTube
import os
from tkinter import *
from tkinter import messagebox as Messagebox

print(os.getcwd())

carpeta_descarga=os.path.join(os.path.expanduser('~'), 'Downloads')

def accion():
    enlace=videos.get()
    video= YouTube(enlace)
    descarga = video.streams.get_highest_resolution()
    descarga.download(carpeta_descarga)
    
def popup():
    Messagebox.showinfo("Hola","Hola")


root = Tk()
root.config(bd=15)
root.title("Script descargar videos")

instruccion = Label(root, text="Script creado en Python para poder descargar videos de Youtube\n")
instruccion.grid(row=0,column=1)

videos= Entry(root)
videos.grid
videos.grid(row=1,column=1)

boton = Button(root, text="Descargar", command=accion)
boton.grid(row=2,column=1)

root.mainloop()