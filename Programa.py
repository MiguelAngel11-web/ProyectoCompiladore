import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox
import tkinter.font as tkFont

from io import open
def beep_error(f):
    '''
    Decorador que permite emitir un beep cuando un método de instancia
    decorado de un widget produce una excepción
    '''
    def applicator(*args, **kwargs):
        try:
            f(*args, **kwargs)
        except:
            if args and isinstance(args[0], tk.Widget):
                args[0].bell()
    return applicator


class MyText(tk.Text):
    def __init__(self, parent=None, *args, **kwargs):
        tk.Text.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.bind('<Control-a>', self.seleccionar_todo)
        self.bind('<Control-x>', self.cortar)
        self.bind('<Control-c>', self.copiar)
        self.bind('<Control-v>', self.pegar)
        self.bind('<Control-z>', self.deshacer)
        self.bind('<Control-Shift-z>', self.rehacer)
        self.bind("<Button-3><ButtonRelease-3>", self.mostrar_menu)

    def mostrar_menu(self, event):
        '''
        Muestra un menú popup con las opciones copiar, pegar y cortar
        al hacer click derecho en el Text
        '''
        menu = tk.Menu(self, tearoff=0)
        menu.add_command(label="Cortar", command=self.cortar)
        menu.add_command(label="Copiar", command=self.copiar)
        menu.add_command(label="Pegar", command=self.pegar)
        menu.tk.call("tk_popup", menu, event.x_root, event.y_root)

    def copiar(self, event=None):
        self.event_generate("<<Copy>>")
        self.text_01.pack()
        self.see("insert")
        return 'break'

    def cortar(self, event=None):
        self.event_generate("<<Cut>>")
        return 'break'

    def pegar(self, event=None):
        self.event_generate("<<Paste>>")
        self.see("insert")
        return 'break'

    def seleccionar_todo(self, event=None):
        self.event_generate("<<SelectAll>>")
        #self.tag_add('sel', '1.0', 'end')   # < Otra alternativa
        return 'break'

    @beep_error
    def deshacer(self, event=None):
        self.tk.call(self, 'edit', 'undo')
        return 'break'

    @beep_error
    def rehacer(self, event=None):
        self.tk.call(self, 'edit', 'redo')
        return 'break'


        #De cajón
        self.mainloop()

class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title = "Proyecto de compiladores"
        self.icon = "./assets/favicon.ico"
        self.size = "950x600"
    
    def inicializarGui(self):
        self.menuGeneral()
        self.blockIzquierdo()
        self.menuEditar()
        self.menuArchivo()
        self.blockDerecho()
        self.buttons()
        
    def menuGeneral(self):
        #Menu
        self.barraMenu = tk.Menu(self,bg='black', fg='white')
        #Tamaño del menú.
        self.config(menu=self.barraMenu, width=300, height = 300)
        self.archivoMenu = tk.Menu(self.barraMenu)
        self.editarMenu = tk.Menu(self.barraMenu) 
        self.formatoMenu = tk.Menu(self.barraMenu) 
        self.compilarMenu = tk.Menu(self.barraMenu) 
        self.ayudaMenu = tk.Menu(self.barraMenu)
        #Mostrar menu agregando el texto
        self.archivoMenu = tk.Menu(self.barraMenu, tearoff=0) #Quitar barra horizontal
        self.editarMenu = tk.Menu(self.barraMenu, tearoff=0) #Quitar barra horizontal
        self.formatoMenu = tk.Menu(self.barraMenu, tearoff=0) #Quitar barra horizontal
        self.compilarMenu = tk.Menu(self.barraMenu, tearoff=0) #Quitar barra horizontal
        self.ayudaMenu = tk.Menu(self.barraMenu, tearoff=0) #Quitar barra horizontal
        self.barraMenu.add_cascade(label = "Archivo", menu=self.archivoMenu)
        self.barraMenu.add_cascade(label = "Editar", menu=self.editarMenu)
        self.barraMenu.add_cascade(label = "Formato", menu=self.formatoMenu)
        self.barraMenu.add_cascade(label = "Compilar", menu=self.compilarMenu)
        self.barraMenu.add_cascade(label = "Ayuda", menu=self.ayudaMenu)

    
    #Funciones
    def abreFichero(self):
        fichero = filedialog.askopenfilename(title="Abrir", filetypes=[("Texto plano", ".txt")])
        if fichero!='':
            archi1=open(fichero, "r", encoding="utf-8")
            contenido=archi1.read()

            archi1.close()
            self.textoIzq.delete("1.0", tk.END) 
            self.textoIzq.insert("1.0", contenido,'content')
            self.textoIzq.tag_config('content',foreground='red')
              
    def guardar(self):
        fichero=filedialog.asksaveasfilename(title = "Guardar como",filetypes = (("Texto plano","*.txt"),("todos los archivos","*.*")))
        if fichero!='':
            archi1=open(fichero, "w", encoding="utf-8")
            archi1.write(self.textoIzq.get("1.0", tk.END))
            archi1.close()
            messagebox.showinfo("Información","Los datos fueron guardados en el archivo.")
    def menuArchivo(self):
        #Submenu de archivo
        self.archivoMenu.add_command(label="Abrir", command=self.abreFichero)
        self.archivoMenu.add_command(label="Guardar", command=self.guardar)
        self.archivoMenu.add_command(label="Nuevo")
        self.archivoMenu.add_separator()
        self.archivoMenu.add_command(label="Seleccionar todo")
        self.archivoMenu.add_command(label="Salir",command=self.quit)

    #Bloques de texto
    def blockIzquierdo(self):
        #Cuadro izquierdo
        lblTextIzq = tk.Label(self, text="Código a compliar")
        lblTextIzq.grid(column=0, row=0, pady=10,padx=10, sticky=tk.NW)
        lblTextIzq.config(justify="right",font=("Arial Bold", 15))

        self.textoIzq = scrolledtext.ScrolledText(self,width=60,height=20)
        self.textoIzq.grid(row=1,column=0,pady=20,padx=10,sticky=tk.NW)
        self.text_font = tkFont.Font(family='Consolas', size=12)
        self.text_01 = MyText(self.textoIzq, wrap=tk.WORD, bd=0, undo=True)
        self.text_01.config(bd=0, padx=6, pady=4, font=self.text_font,
                            selectbackground='lightblue',
                            width=44, height=16,
                            bg='#242424', fg='white',
                            insertbackground='white',
                            highlightbackground='black',
                            highlightcolor='white'
                            )
        self.text_01.grid(row=0,column=0)
          
    #Editar submenu
    def menuEditar(self):
        self.editarMenu.add_command(label='Deshacer',
                             command=self.text_01.deshacer,
                             accelerator='Ctrl+Z'
                             )
        self.editarMenu.add_command(label='Rehacer',
                             command=self.text_01.rehacer,
                             accelerator='Ctrl+Shift+Z'
                             )
        self.editarMenu.add_separator()
        self.editarMenu.add_command(label='Cortar',
                             command=self.text_01.cortar,
                             accelerator='Ctrl+X'
                             )
        self.editarMenu.add_command(label='Copiar',
                             command=self.text_01.copiar,
                             accelerator='Ctrl+C'
                             )
        self.editarMenu.add_command(label='Pegar',
                             command=self.text_01.pegar,
                             accelerator='Ctrl+V'
                             )
        self.editarMenu.add_command(label='Seleccionar todo',
                             command=self.text_01.seleccionar_todo,
                             accelerator='Ctrl+A'
                             )
    
    def blockDerecho(self):
        #Cuadro derecho
        textoDerecho = scrolledtext.ScrolledText(self,width=40,height=20)
        textoDerecho.grid(row=1,column=1,pady=20,padx=10,sticky=tk.E)
        #Cuadro de abajo
        textoAbajo = scrolledtext.ScrolledText(self,width=90,height=5)
        textoAbajo.grid(row=2,column=0,columnspan=3,pady=20)

    def buttons(self):
        btnLex = tk.Button(self, text="Lexico", bg="white")
        btnLex.place(x=530,y=45)

        btnSin = tk.Button(self, text="Sintactico", bg="white")
        btnSin.place(x=580,y=45)

        btnSem = tk.Button(self, text="Semantico", bg="white")
        btnSem.place(x=650,y=45)

        btnCI = tk.Button(self, text="Codigo Intermedio", bg="white")
        btnCI.place(x=725,y=45)

        btnErr = tk.Button(self, text="Errores", bg="white")
        btnErr.place(x=80,y=410)
        btnRes = tk.Button(self, text="Resultados", bg="white")
        btnRes.place(x=140,y=410)
    
    def runCode(self):
        tk.mainloop()
