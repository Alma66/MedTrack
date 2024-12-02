import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import messagebox
from db.tables.relacionales.med_enf import MedEnf
from db.tables.enfermedad import Enfermedad
from db.tables.medicamento import Medicamento

# Función para obtener todos los registros de enf_med
def obtener_enf_med():
    return MedEnf.obtener_todos()

# Función para mostrar la tabla enf_med
def mostrar_tabla():
    for widget in frame_tabla.winfo_children():
        widget.destroy()

    registros = obtener_enf_med()

    for i, registro in enumerate(registros):
        tk.Label(frame_tabla, text=registro[0]).grid(row=i+1, column=0)
        tk.Label(frame_tabla, text=registro[1]).grid(row=i+1, column=1)
        tk.Label(frame_tabla, text=registro[2]).grid(row=i+1, column=2)

        # Botones para eliminar y editar
        tk.Button(frame_tabla, text="Eliminar", command=lambda id=registro[0]: eliminar_enf_med(id)).grid(row=i+1, column=3)
        tk.Button(frame_tabla, text="Editar", command=lambda id=registro[0]: abrir_editar_enf_med(id)).grid(row=i+1, column=4)

# Función para eliminar un registro de enf_med
def eliminar_enf_med(id_enfmed):
    MedEnf.eliminar( id_enfmed)
    mostrar_tabla()

# Función para abrir la ventana de edición
def abrir_editar_enf_med(id_enfmed):
    def editar():
        enfmed = MedEnf(id_enfmed, entry_id_med.get(), entry_id_enf.get())
        enfmed.actualizar()
        mostrar_tabla()
        ventana_editar.destroy()

    ventana_editar = tk.Toplevel(root)
    ventana_editar.title(f"Editar Relación de Medicamento con Enfermedad {id_enfmed}")

    # Obtener los datos de enf_med
    registro = MedEnf.obtener_por_id( id_enfmed)

    if registro:
        # Campos para editar
        tk.Label(ventana_editar, text="ID Medicamento").grid(row=0, column=0)
        tk.Label(ventana_editar, text="ID Enfermedad").grid(row=1, column=0)

        entry_id_med = tk.Entry(ventana_editar)
        entry_id_med.insert(0, registro[1])  # Asignar valor del ID de medicamento
        entry_id_med.grid(row=0, column=1)

        entry_id_enf = tk.Entry(ventana_editar)
        entry_id_enf.insert(0, registro[2])  # Asignar valor del ID de enfermedad
        entry_id_enf.grid(row=1, column=1)

        tk.Button(ventana_editar, text="Guardar", command=editar).grid(row=2, column=1)

# Función para agregar un nuevo registro de enf_med
def agregar():
    id_med = entry_id_med.get()
    id_enf = entry_id_enf.get()

    enfmed = MedEnf(id_med=id_med, id_enf=id_enf)
    enfmed.insertar()
    mostrar_tabla()

# Interfaz gráfica
root = tk.Tk()
root.title("Gestión de Medicamento-Enfermedad")

# Entrada de datos para agregar relación medicamento-enfermedad
tk.Label(root, text="ID Medicamento").grid(row=0, column=0)
tk.Label(root, text="ID Enfermedad").grid(row=1, column=0)

entry_id_med = tk.Entry(root)
entry_id_med.grid(row=0, column=1)

entry_id_enf = tk.Entry(root)
entry_id_enf.grid(row=1, column=1)

tk.Button(root, text="Agregar Relación", command=agregar).grid(row=2, column=1)

# Frame para la tabla
frame_tabla = tk.Frame(root)
frame_tabla.grid(row=3, column=0, columnspan=2)

# Mostrar la tabla de relaciones medicamento-enfermedad
mostrar_tabla()

root.mainloop()
