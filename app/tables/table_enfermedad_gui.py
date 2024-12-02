import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import messagebox
from db.tables.enfermedad import Enfermedad

# Función para obtener todas las enfermedades
def obtener_enfermedades():
    return Enfermedad.lista_enfermedades

# Función para mostrar la tabla de enfermedades en la interfaz gráfica
def mostrar_tabla():
    for widget in frame_tabla.winfo_children():
        widget.destroy()

    enfermedades_entries = obtener_enfermedades()

    for i, enfermedad in enumerate(enfermedades_entries):
        tk.Label(frame_tabla, text=enfermedad.id_enf).grid(row=i+1, column=0)
        tk.Label(frame_tabla, text=enfermedad.nombre).grid(row=i+1, column=1)
        tk.Label(frame_tabla, text=enfermedad.descripcion).grid(row=i+1, column=2)

        # Botones para eliminar y editar
        tk.Button(frame_tabla, text="Eliminar", command=lambda id=enfermedad.id_enf: eliminar_enfermedad(id)).grid(row=i+1, column=3)
        tk.Button(frame_tabla, text="Editar", command=lambda id=enfermedad.id_enf: abrir_editar_enfermedad(id)).grid(row=i+1, column=4)

# Función para eliminar una enfermedad
def eliminar_enfermedad(id_enf):
    enfermedad = Enfermedad(None)  # Se pasa None porque el cursor no es necesario para este caso
    enfermedad.eliminar_enfermedad()
    mostrar_tabla()

# Función para abrir la ventana de edición
def abrir_editar_enfermedad(id_enf):
    def editar():
        enfermedad = Enfermedad(None, id_enf=id_enf, nombre=entry_nombre.get(), descripcion=entry_descripcion.get())
        enfermedad.editar_enfermedad()
        mostrar_tabla()
        ventana_editar.destroy()

    ventana_editar = tk.Toplevel(root)
    ventana_editar.title(f"Editar Enfermedad {id_enf}")

    # Obtener datos de la enfermedad
    enfermedad = next((entry for entry in obtener_enfermedades() if entry.id_enf == id_enf), None)

    if enfermedad:
        # Campos para editar
        tk.Label(ventana_editar, text="Nombre").grid(row=0, column=0)
        tk.Label(ventana_editar, text="Descripción").grid(row=1, column=0)

        entry_nombre = tk.Entry(ventana_editar)
        entry_nombre.insert(0, enfermedad.nombre)
        entry_nombre.grid(row=0, column=1)

        entry_descripcion = tk.Entry(ventana_editar)
        entry_descripcion.insert(0, enfermedad.descripcion)
        entry_descripcion.grid(row=1, column=1)

        tk.Button(ventana_editar, text="Guardar", command=editar).grid(row=2, column=1)

# Función para agregar una nueva enfermedad
def agregar():
    id_enf = entry_id_enf.get()
    nombre = entry_nombre.get()
    descripcion = entry_descripcion.get()

    enfermedad = Enfermedad(None, id_enf=id_enf, nombre=nombre, descripcion=descripcion)
    enfermedad.insertar_enfermedad()
    mostrar_tabla()

# Interfaz gráfica
root = tk.Tk()
root.title("Gestión de Enfermedades")

# Entrada de datos para agregar enfermedad
tk.Label(root, text="ID Enfermedad").grid(row=0, column=0)
tk.Label(root, text="Nombre").grid(row=1, column=0)
tk.Label(root, text="Descripción").grid(row=2, column=0)

entry_id_enf = tk.Entry(root)
entry_id_enf.grid(row=0, column=1)

entry_nombre = tk.Entry(root)
entry_nombre.grid(row=1, column=1)

entry_descripcion = tk.Entry(root)
entry_descripcion.grid(row=2, column=1)

tk.Button(root, text="Agregar Enfermedad", command=agregar).grid(row=3, column=1)

# Frame para la tabla
frame_tabla = tk.Frame(root)
frame_tabla.grid(row=4, column=0, columnspan=2)

# Mostrar la tabla de enfermedades
mostrar_tabla()

root.mainloop()
