from tkinter import filedialog
from pytube import YouTube
import os
from tkinter import *
from tkinter import messagebox as MessageBox
from pytube.cli import on_progress
from tkinter import ttk


os.getcwd()

def ingresaRuta ():
        
        ruta = filedialog.askdirectory()
        os.chdir(ruta)
        os.getcwd()
 

    
    
def progress_Check(stream, chunk, bytes_remaining):
    #Gets the percentage of the file that has been downloaded.
    percent = round((100*(Tsize-bytes_remaining))/Tsize)
    text2=percent
    prog.step(percent)
    
    
    
      

def accion():
    enlace=videos.get()  
    try:
        video = YouTube(enlace,on_progress_callback=progress_Check)
        
    except:
        print("ERROR. Prueba tu conexion o url YouTube  verifica tu URL")   
    descarga = video.streams.get_highest_resolution()
    global Tsize
    Tsize=descarga.filesize
    play = Label(root, text="ESPERE DESCARGANDO:"+video.title,font=("Verdana",11),foreground="red")
    play.grid(row=4, column=1)
    descarga.download(ingresaRuta())
    MessageBox.showinfo("DESCARGA FINALIZADA", "Descarga finalizada con exito")
    play.destroy()
    play = Label(root, text="Listo descarga completada",font=("Verdana",15),foreground="green")
    play.grid(row=4, column=1)
    

 
   




def popup():
    MessageBox.showinfo("Sobre mí","")

 
root = Tk()
root.config(bd=20)
root.title("Script descargar vídeos")
root.resizable = False

imagen = PhotoImage(file="youtube.png")
foto = Label(root, image=imagen, bd=0)
foto.grid(row=0, column=0)

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)


menubar.add_cascade(label="Para más información", menu=helpmenu)
helpmenu.add_command(label="Información del autor",command=popup)

menubar.add_command(label="Salir", command=root.destroy)


instrucciones = Label(root, text="Programa creado para descargar vídeos de Youtube\n")
instrucciones.grid(row=0, column=1)
txt1="Copie el Link del video y peguelo aqui abajo ↓\n"
instrucciones2 = Label(root, text=txt1)
instrucciones2.grid(row=1, column=1)


videos = Entry(root)
videos.config(width=60, borderwidth=5,bg='lightgreen')
videos.grid(row=2, column=1)

txt2="%"
instrucciones5 = Label(root, text=txt2)
instrucciones5.grid(row=6, column=1)

boton = Button(root, text="Descargar :)", command=accion,font=("Verdana",15),foreground="red")
boton.grid(row=3, column=1)
boton.config(borderwidth=5,bg='gray58')

prog= ttk.Progressbar(root)
prog.config(length=200,maximum=100)
prog.grid(row=5, column=1)




root.mainloop()