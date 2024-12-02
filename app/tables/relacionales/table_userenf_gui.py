import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import messagebox
from db.tables.relacionales.user_enf import UserEnf
from db.tables.enfermedad import Enfermedad
from db.tables.usuario import Usuario

# Función para obtener todos los registros de user_enf
def obtener_user_enf():
    return UserEnf.obtener_todos()

# Función para mostrar la tabla user_enf
def mostrar_tabla():
    for widget in frame_tabla.winfo_children():
        widget.destroy()

    registros = obtener_user_enf()

    for i, registro in enumerate(registros):
        tk.Label(frame_tabla, text=registro[0]).grid(row=i+1, column=0)
        tk.Label(frame_tabla, text=registro[1]).grid(row=i+1, column=1)
        tk.Label(frame_tabla, text=registro[2]).grid(row=i+1, column=2)

        # Botones para eliminar y editar
        tk.Button(frame_tabla, text="Eliminar", command=lambda id=registro[0]: eliminar_user_enf(id)).grid(row=i+1, column=3)
        tk.Button(frame_tabla, text="Editar", command=lambda id=registro[0]: abrir_editar_user_enf(id)).grid(row=i+1, column=4)

# Función para eliminar un registro de user_enf
def eliminar_user_enf(id_userenf):
    UserEnf.eliminar( id_userenf)
    mostrar_tabla()

# Función para abrir la ventana de edición
def abrir_editar_user_enf(id_userenf):
    def editar():
        userenf = UserEnf(id_userenf, entry_id_user.get(), entry_id_enf.get())
        userenf.actualizar()
        mostrar_tabla()
        ventana_editar.destroy()

    ventana_editar = tk.Toplevel(root)
    ventana_editar.title(f"Editar Relación de Usuario con Enfermedad {id_userenf}")

    # Obtener los datos de user_enf
    registro = UserEnf.obtener_por_id( id_userenf)

    if registro:
        # Campos para editar
        tk.Label(ventana_editar, text="ID Usuario").grid(row=0, column=0)
        tk.Label(ventana_editar, text="ID Enfermedad").grid(row=1, column=0)

        entry_id_user = tk.Entry(ventana_editar)
        entry_id_user.insert(0, registro[1])  # Asignar valor del ID de usuario
        entry_id_user.grid(row=0, column=1)

        entry_id_enf = tk.Entry(ventana_editar)
        entry_id_enf.insert(0, registro[2])  # Asignar valor del ID de enfermedad
        entry_id_enf.grid(row=1, column=1)

        tk.Button(ventana_editar, text="Guardar", command=editar).grid(row=2, column=1)

# Función para agregar un nuevo registro de user_enf
def agregar():
    id_user = entry_id_user.get()
    id_enf = entry_id_enf.get()

    userenf = UserEnf(id_user=id_user, id_enf=id_enf)
    userenf.insertar()
    mostrar_tabla()

# Interfaz gráfica
root = tk.Tk()
root.title("Gestión de Usuario-Enfermedad")

# Entrada de datos para agregar relación usuario-enfermedad
tk.Label(root, text="ID Usuario").grid(row=0, column=0)
tk.Label(root, text="ID Enfermedad").grid(row=1, column=0)

entry_id_user = tk.Entry(root)
entry_id_user.grid(row=0, column=1)

entry_id_enf = tk.Entry(root)
entry_id_enf.grid(row=1, column=1)

tk.Button(root, text="Agregar Relación", command=agregar).grid(row=2, column=1)

# Frame para la tabla
frame_tabla = tk.Frame(root)
frame_tabla.grid(row=3, column=0, columnspan=2)

# Mostrar la tabla de relaciones usuario-enfermedad
mostrar_tabla()

root.mainloop()
