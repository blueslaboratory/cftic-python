# Day 23 - 29/06/2023

'''
3.Librería Tkinter

Deseas crear una interfaz gráfica simple para una aplicación de lista de tareas.
La interfaz debe tener un campo de entrada de texto donde los usuarios puedan
escribir nuevas tareas y un botón "Agregar" que agregue la tarea a una lista.
Además, la interfaz debe mostrar la lista de tareas agregadas en una caja de texto.

Implementa la interfaz gráfica utilizando la biblioteca Tkinter y las siguientes
 especificaciones:

* La ventana principal debe tener el título "Lista de Tareas".
* Debe haber un campo de entrada de texto donde los usuarios puedan escribir
nuevas tareas.
* Debe haber un botón "Agregar" que, al hacer clic, agregue la tarea escrita
en el campo de entrada a una lista de tareas y actualice la caja de texto
mostrando la lista actualizada de tareas.
* La caja de texto debe mostrar la lista de tareas en líneas separadas.
'''

from tkinter import *
from tkinter import ttk, messagebox, filedialog


def agregar_tarea():
	tarea = entrada.get()
	if tarea:
		tareas.append(tarea)
		actualizar_lista()


def actualizar_lista():
	lista_texto.delete("1.0", END)
	for tarea in tareas:
		lista_texto.insert(END, tarea + "\n")


def salir():
	if messagebox.askokcancel('Salir', '¿Estas seguro que deseas salir?'):
		v_ppal.destroy()


v_ppal = Tk()
v_ppal.title('Lista de Tareas')
v_ppal.geometry('270x300')

# create a menubar
menubar = Menu(v_ppal)
v_ppal.config(menu=menubar)

# create a menu
file_menu = Menu(menubar)

# add a menu item to the menu
file_menu.add_command(
	label='Exit',
	command=v_ppal.destroy
)

# add the File menu to the menubar
menubar.add_cascade(
	label="File",
	menu=file_menu
)

frm = ttk.Frame(v_ppal, padding=10, border=1)
frm.grid(column=0, row=0)

ttk.Label(frm, text="Campo de entrada: ").grid(column=0, row=0)

entrada = ttk.Entry(frm)
entrada.grid(column=0, row=1, pady=5)

boton_agregar = ttk.Button(frm, text="Agregar", command=agregar_tarea)
boton_agregar.grid(column=0, row=2, pady=5)

lista_texto = Text(frm, height=8, width=30)
lista_texto.grid(column=0, row=3, pady=5)

# Lista para almacenar las tareas
tareas = []

v_ppal.protocol('WM_DELETE_WINDOW', salir)
v_ppal.mainloop()