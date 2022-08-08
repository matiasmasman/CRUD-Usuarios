from tkinter import *
from tkinter import messagebox
import sqlite3

#------- FUNCIONES -------

def conexionBBDD():
    conexion = sqlite3.connect('Usuarios')
    puntero = conexion.cursor()

    try:
        puntero.execute("""
            CREATE TABLE datos_usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR (20), 
                password VARCHAR (20),
                apellido VARCHAR (20),
                direccion VARCHAR (50),
                comentario VARCHAR (100)
            )
        """)
        messagebox.showinfo('BBDD', 'BBDD creada con exito')
    except:
        messagebox.showwarning('Error', 'La BBDD ya existe')

def salirPrograma():
    respuesta = messagebox.askquestion('Salir', 'Desea salir del programa?')

    if respuesta == 'yes':
        root.destroy()

def limpiarCampos():
    miId.set('')
    miNombre.set('')
    miPassword.set('')
    miApellido.set('')
    miDireccion.set('')
    textoComentario.delete(1.0, END)

def crear():
    conexion = sqlite3.connect('Usuarios')
    puntero = conexion.cursor()

    datos = [
        miNombre.get(),
        miPassword.get(),
        miApellido.get(),
        miDireccion.get(),
        textoComentario.get(1.0, END)
    ]

    puntero.execute("INSERT INTO datos_usuarios VALUES (NULL, ?, ?, ?, ?, ?)", datos)

    conexion.commit()

    messagebox.showinfo('BBDD', 'Registro insertado con exito')

def leer():
    conexion = sqlite3.connect('Usuarios')
    puntero = conexion.cursor()

    puntero.execute("SELECT * FROM datos_usuarios WHERE id = ?", miId.get())

    usuario = puntero.fetchall()

    for x in usuario:
        miId.set(x[0]),
        miNombre.set(x[1]),
        miPassword.set(x[2]),
        miApellido.set(x[3]),
        miDireccion.set(x[4]),
        textoComentario.insert(1.0, x[5])

    conexion.commit()

def actualizar():
    conexion = sqlite3.connect('Usuarios')
    puntero = conexion.cursor()
    
    datos = [
        miNombre.get(),
        miPassword.get(),
        miApellido.get(),
        miDireccion.get(),
        textoComentario.get(1.0, END)
    ]

    puntero.execute("UPDATE datos_usuarios SET nombre = ?, password = ?, apellido = ?, direccion = ?, comentario = ?" + "WHERE id =" + miId.get(), datos)

    conexion.commit()

    messagebox.showinfo('BBDD', 'Registro actualizado con exito')

def eliminar():
    conexion = sqlite3.connect('Usuarios')
    puntero = conexion.cursor()
    
    puntero.execute("DELETE FROM datos_usuarios WHERE id = ?", miId.get())

    conexion.commit()

    messagebox.showinfo('BBDD', 'Registro eliminado con exito')

#--------------------------

root = Tk()
root.resizable(0, 0)

#------- BARRA MENU -------

barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label='Conectar', command=conexionBBDD)
bbddMenu.add_command(label='Salir', command=salirPrograma)

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label='Borrar campos', command=limpiarCampos)

crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(label='Crear', command=crear)
crudMenu.add_command(label='Leer', command=leer)
crudMenu.add_command(label='Actualizar', command=actualizar)
crudMenu.add_command(label='Eliminar', command=eliminar)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label='Licencia')
ayudaMenu.add_command(label='Acerca de...')

barraMenu.add_cascade(label='BBDD', menu=bbddMenu)
barraMenu.add_cascade(label='Borrar', menu=borrarMenu)
barraMenu.add_cascade(label='CRUD', menu=crudMenu)
barraMenu.add_cascade(label='Ayuda', menu=ayudaMenu)

#------- COMIENZO DE CAMPOS -------

miFrame = Frame(root)
miFrame.pack()

miId = StringVar()
miNombre = StringVar()
miPassword = StringVar()
miApellido = StringVar()
miDireccion = StringVar()


cuadroId = Entry(miFrame, textvariable=miId)
cuadroId.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre = Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg='red', justify='right')

cuadroPassword = Entry(miFrame, textvariable=miPassword)
cuadroPassword.grid(row=2, column=1, padx=10, pady=10)
cuadroPassword.config(show='*')

cuadroApellido = Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroDireccion = Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

textoComentario = Text(miFrame, width=20, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky='nsew')

textoComentario.config(yscrollcommand=scrollVert.set)

#------- COMIENZO DE LABEL -------

idLabel = Label(miFrame, text='Id:')
idLabel.grid(row=0, column=0, sticky='e', padx=10, pady=10)

nombreLabel = Label(miFrame, text='Nombre:')
nombreLabel.grid(row=1, column=0, sticky='e', padx=10, pady=10)

passwordLabel = Label(miFrame, text='Password:')
passwordLabel.grid(row=2, column=0, sticky='e', padx=10, pady=10)

apellidoLabel = Label(miFrame, text='Apellido:')
apellidoLabel.grid(row=3, column=0, sticky='e', padx=10, pady=10)

direccionLabel = Label(miFrame, text='Direccion:')
direccionLabel.grid(row=4, column=0, sticky='e', padx=10, pady=10)

comentariosLabel = Label(miFrame, text='Comentarios:')
comentariosLabel.grid(row=5, column=0, sticky='e', padx=10, pady=10)

#------- COMIENZO DE BOTONES -------

miFrame2 = Frame(root)
miFrame2.pack()

botonCrear = Button(miFrame2, text='Create', command=crear)
botonCrear.grid(row=1, column=0, sticky='e', padx=10, pady=10)

botonLeer = Button(miFrame2, text='Read', command=leer)
botonLeer.grid(row=1, column=1, sticky='e', padx=10, pady=10)

botonActualizar = Button(miFrame2, text='Update', command=actualizar)
botonActualizar.grid(row=1, column=2, sticky='e', padx=10, pady=10)

botonBorrar = Button(miFrame2, text='Delete', command=eliminar)
botonBorrar.grid(row=1, column=3, sticky='e', padx=10, pady=10)

#-----------------------------------
root.mainloop()