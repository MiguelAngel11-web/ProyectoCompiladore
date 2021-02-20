from tkinter import *
""" Para cambair el icono de la ventana
necesitamos un archivo .ico, y tenerlo en tu carpeta.
Cambié ela extensión del archivo de py a pyw, para que al momento
de abrir la interfaz no se abra la terminal por atras."""



""" Crear ventana raiz de tkinter """
raiz = Tk()
""" Cambiar el titulo de la ventana """""" 
raiz.title("Proyecto de compiladores") """
""" 
miFrame = Frame(raiz, width=1200,height=600)
miFrame.pack()
 """



""" Método para redimensionar ventana
raiz.resizable(0,0)
los valores son(widt,height)
No se podra dimensionar la ventana
"""
""" Para cambiar el icono usamos
raiz.iconbitmap("ruta del icono")
"""

""" Tamaño de la ventana (ancho x alto)"""
""" raiz.geometry("650x350") """

""" Color de fondo de nuestra ventana 
raiz.config(bg="black")"""



""" Labels """""" 
cuadroNombre = Entry(miFrame) """
""" Personalizar elementos y GRID """""" 
cuadroNombre.grid(row=0,column=0,padx=10,pady=10,sticky="w") """
""" Hacemos un tabla y lo colocamos en la posición 0,0.
Agregamos un padding en X (derecha e izquiera) y en Y(abajo y arriba)
con sticky podemos alinear el elemento, esto se hace con las corrdenadas
Norte(Northe) , Sur(South), Este(East), Oeste(West)

Para el estilo de nuestro cuadro, color, typografia etc

cuadroNombre.config(fg="red",justify="center") """



""" Para una password podemos hacer que se muestre con * al escribir 
cuadroPass= Entry(miFrame)
cuadroPass.grid(row=1,column=0,padx=10,pady=10,sticky="w")
cuadroPass.config(show="*")"""


""" Para crear un menú utilizamos los siguientes lineas
root = Tk() Iniciamos de igual forma el tkinter

Aquí es donde crearemos nuestro menú
barraMenu = Menu(root)
root.config(menu=barraMenu)

Para el tamaño de nuestra ventana sería agregando a root.config lo siguiente

root.config(menu=barraMenu, width=300, height = 300)



¿Cómo se llamara nuestro menú?
-> archivoMenu = Menu(barraMenu) -> Decimos a que barra pertenece nuestro menú

¿Cuanto elementos quieres en tu menú? Copiamos y pegamos lo de arriba cuantas veces sean las opciones del menú
Por ejemplo yo quiero cinco opciones: Archivo Editar Formato Compilar Ayuda
Agregamos cuatro más:

editarMenu = Menu(barraMenu) 
formatoMenu = Menu(barraMenu) 
compilarMenu = Menu(barraMenu) 
ayudaMenu = Menu(barraMenu) 

Ahora agregaremos el texo que tendra nuestro menú

barraMenu.add_cascade(label = "Archivo", menu=archivoMenu)
Aquí decimos que el elemento archivoMenu tiene que tener ese texto 
Y esto con todos los elementos del menu.

¿Elementos para sub menu?
Ahora para un sub menu
Por ejemplo para la pestaña archivo:
archivoMenu.add_command(label="Guardar")
Si queremos más elementos añadimos está misma linea tantas veces queramos
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Seleccionar todo")
archivoMenu.add_command(label="Salir")

Quitamos una barra horizontal que sale por defecto
ayudaMenu = Menu(barraMenu, tearoff=0)

Separar grupos de opciones en nuestro sub menú. Sería de la siguente manera
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_separator()
archivoMenu.add_command(label="Seleccionar todo")
archivoMenu.add_command(label="Salirs")


"""



""" Con el método mainloop podemos mantener la ventana abierta.
Lo que hace es dejarlo en un bluce infinito para que permanesca abierta.

SIEMPRE AL FINAL """
raiz.mainloop()