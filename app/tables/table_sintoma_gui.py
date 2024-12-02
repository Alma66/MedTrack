import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import messagebox
from db.tables.sintoma import Sintoma

# Función para obtener todos los síntomas
def obtener_sintomas():
    sintoma = Sintoma()
    return sintoma.mostrar_sintomas()

# Función para mostrar la tabla de síntomas en la interfaz gráfica
def mostrar_tabla():
    for widget in frame_tabla.winfo_children():
        widget.destroy()

    sintomas = obtener_sintomas()

    for i, sint in enumerate(sintomas):
        tk.Label(frame_tabla, text=sint[0]).grid(row=i+1, column=0)  # id_sintoma
        tk.Label(frame_tabla, text=sint[1]).grid(row=i+1, column=1)  # nombre
        tk.Label(frame_tabla, text=sint[2]).grid(row=i+1, column=2)  # descripcion

        # Botones para eliminar y editar
        tk.Button(frame_tabla, text="Eliminar", command=lambda id=sint[0]: eliminar_sintoma(id)).grid(row=i+1, column=3)
        tk.Button(frame_tabla, text="Editar", command=lambda id=sint[0]: abrir_editar_sintoma(id)).grid(row=i+1, column=4)

# Función para eliminar un síntoma
def eliminar_sintoma(id_sintoma):
    sintoma = Sintoma(id_sintoma=id_sintoma)
    sintoma.eliminar_sintoma()
    mostrar_tabla()

# Función para abrir la ventana de edición
def abrir_editar_sintoma(id_sintoma):
    def editar():
        sintoma = Sintoma(id_sintoma=id_sintoma, nombre=entry_nombre.get(), descripcion=entry_descripcion.get())
        sintoma.editar_sintoma()
        mostrar_tabla()
        ventana_editar.destroy()

    ventana_editar = tk.Toplevel(root)
    ventana_editar.title(f"Editar Sintoma {id_sintoma}")

    # Obtener datos del síntoma
    sintoma = next((sint for sint in obtener_sintomas() if sint[0] == id_sintoma), None)

    if sintoma:
        # Campos para editar
        tk.Label(ventana_editar, text="Nombre").grid(row=0, column=0)
        tk.Label(ventana_editar, text="Descripción").grid(row=1, column=0)

        entry_nombre = tk.Entry(ventana_editar)
        entry_nombre.insert(0, sintoma[1])
        entry_nombre.grid(row=0, column=1)

        entry_descripcion = tk.Entry(ventana_editar)
        entry_descripcion.insert(0, sintoma[2])
        entry_descripcion.grid(row=1, column=1)

        tk.Button(ventana_editar, text="Guardar", command=editar).grid(row=2, column=1)

# Función para agregar un nuevo síntoma
def agregar():
    id_sintoma = entry_id_sintoma.get()
    nombre = entry_nombre.get()
    descripcion = entry_descripcion.get()
    sintoma = Sintoma( id_sintoma=id_sintoma, nombre=nombre, descripcion=descripcion)
    sintoma.insertar_sintoma()
    mostrar_tabla()

# Interfaz gráfica
root = tk.Tk()
root.title("Gestión de Síntomas")

# Entrada de datos para agregar síntomas
tk.Label(root, text="ID Síntoma").grid(row=0, column=0)
tk.Label(root, text="Nombre").grid(row=1, column=0)
tk.Label(root, text="Descripción").grid(row=2, column=0)

entry_id_sintoma = tk.Entry(root)
entry_id_sintoma.grid(row=0, column=1)

entry_nombre = tk.Entry(root)
entry_nombre.grid(row=1, column=1)

entry_descripcion = tk.Entry(root)
entry_descripcion.grid(row=2, column=1)

tk.Button(root, text="Agregar Síntoma", command=agregar).grid(row=3, column=1)

# Frame para la tabla
frame_tabla = tk.Frame(root)
frame_tabla.grid(row=4, column=0, columnspan=2)

# Mostrar la tabla de síntomas
mostrar_tabla()

root.mainloop()
