# Day 16 - 20/06/2023

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd


# funciones
# Importante tiene un parametro que es el evento
def button_second_click(event):
    print('Has pulsado el boton derecho')

def mostrar_mensaje():
    messagebox.showinfo('Mensaje', 'Mi mensaje')
    
def mostrar_warning():
    messagebox.showwarning('Warning', '¡Cuidadin!')
    
def mostrar_error():
    messagebox.showerror('Error', 'Te has colao bacalao')
    
def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    messagebox.showinfo(
        title='Selected File',
        message=filename
    )


# ventana principal
v_ppal = Tk()

# title
v_ppal.title('Primera prueba Clase') 

# size de la ventana
v_ppal.geometry('800x600')

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

# frame
frm = ttk.Frame(v_ppal, padding=10, border=1)

# grid
frm.grid(column=10,row=10)

# label
ttk.Label(frm, text="Hello World!").grid(column=3, row=0)


# buttons
# Si pulsas sobre con el boton derecho del raton llama a: button_second_click
# e imprime por consola: Has pulsado el boton derecho
btn = ttk.Button(frm, text="Quit", command=v_ppal.destroy).grid(column=6, row=5)
btn.bind("<Button-3>", button_second_click)

# ttk.Button(frm, text="Quit", command=v_ppal.destroy).grid(column=6, row=5)
ttk.Button(frm, text="Mostrar Mensaje", command=mostrar_mensaje).grid(column=2, row=1)
ttk.Button(frm, text="Mostrar Warning", command=mostrar_warning).grid(column=2, row=2)
ttk.Button(frm, text="Mostrar Error", command=mostrar_error).grid(column=2, row=3)
ttk.Button(frm, text="Seleccionar Fichero", command=select_file).grid(column=5, row=2)


'''
Esta linea inicia el bucle principal de la ventana, que espera a que ocurran 
eventos (como hacer clic en el botón) y responde a ellos. 
El programa seguira ejecutandose en este bucle hasta que se cierre la ventana.
'''
v_ppal.mainloop()