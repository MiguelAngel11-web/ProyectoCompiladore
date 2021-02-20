from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import filedialog

#Instanciar libreria tkinter
window = Tk()
window.title("Proyecto de compiladores")

#Ventana
window.geometry("950x600")
#Menu
barraMenu = Menu(window)
#Tamaño del menú.
window.config(menu=barraMenu, width=300, height = 300)
#Funciones
def abreFichero():

    fichero = filedialog.askopenfilename(title="Abrir", filetypes=[("Texto plano", ".txt")])
    print(fichero)
#Secciones menú
archivoMenu = Menu(barraMenu)
editarMenu = Menu(barraMenu) 
formatoMenu = Menu(barraMenu) 
compilarMenu = Menu(barraMenu) 
ayudaMenu = Menu(barraMenu) 
#Mostrar menu agregando el texto
archivoMenu = Menu(barraMenu, tearoff=0) #Quitar barra horizontal
barraMenu.add_cascade(label = "Archivo", menu=archivoMenu)
barraMenu.add_cascade(label = "Editar", menu=editarMenu)
barraMenu.add_cascade(label = "Formato", menu=formatoMenu)
barraMenu.add_cascade(label = "Compilar", menu=compilarMenu)
barraMenu.add_cascade(label = "Ayuda", menu=ayudaMenu)
#Submenu de archivo
archivoMenu.add_command(label="Abrir", command=abreFichero)
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_separator()
archivoMenu.add_command(label="Seleccionar todo")
archivoMenu.add_command(label="Salir")
#Cuadro izquierdo
lblTextIzq = Label(window, text="Código a compliar")
lblTextIzq.grid(column=0, row=0, pady=10,padx=10, sticky=NW)
lblTextIzq.config(justify="right",font=("Arial Bold", 15))
textoIzq = scrolledtext.ScrolledText(window,width=60,height=20)
textoIzq.grid(row=1,column=0,pady=20,padx=10,sticky=NW)
#Cuadro derecho
textoDerecho = scrolledtext.ScrolledText(window,width=40,height=20)
textoDerecho.grid(row=1,column=1,pady=20,padx=10,sticky=E)
#Opciones
""" def clicked():

    lbl.configure(text="Button was clicked !!")

btn = Button(window, text="Click Me", command=clicked) """

btnLex = Button(window, text="Lexico", bg="white")
btnLex.place(x=530,y=45)

btnSin = Button(window, text="Sintactico", bg="white")
btnSin.place(x=580,y=45)

btnSem = Button(window, text="Semantico", bg="white")
btnSem.place(x=650,y=45)

btnCI = Button(window, text="Codigo Intermedio", bg="white")
btnCI.place(x=725,y=45)

btnErr = Button(window, text="Errores", bg="white")
btnErr.place(x=80,y=410)
btnRes = Button(window, text="Resultados", bg="white")
btnRes.place(x=140,y=410)




#Cuadro de abajo
textoAbajo = scrolledtext.ScrolledText(window,width=90,height=5)
textoAbajo.grid(row=2,column=0,columnspan=3,pady=20)





#De cajón
window.mainloop()