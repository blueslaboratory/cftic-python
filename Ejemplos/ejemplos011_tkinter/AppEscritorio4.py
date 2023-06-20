# Day 16 - 20/06/2023

import tkinter as tk


# Funcion para manejar la opcion "Salir" del menu
def salir():
    ventanaPrincipal.destroy()


ventanaPrincipal = tk.Tk()

# title
ventanaPrincipal.title('1º prueba de clase')

# size de la ventana
ventanaPrincipal.geometry('800x600')

# Crear el objeto Menu
menu_principal = tk.Menu(ventanaPrincipal)

# Crear el elemento "archivo" en el menu principal
menu_archivo = tk.Menu(menu_principal, tearoff=False)
menu_archivo.add_command(label="Salir", command=salir)

# Agregar el elemento "Archivo" al menu principal
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)

# Configurar el menu principal en la ventanaPrincipal
ventanaPrincipal.config(menu=menu_principal)


ventanaPrincipal.mainloop()