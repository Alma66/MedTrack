import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import messagebox
from db.tables.relacionales.info_med import InfoMed
from db.tables.medicamento import Medicamento
from db.tables.infoEdu import InfoEdu

# Función para obtener todos los registros de info_med
def obtener_info_med():
    return InfoMed.obtener_todos()
# Función para mostrar la tabla info_med
def mostrar_tabla():
    for widget in frame_tabla.winfo_children():
        widget.destroy()

    registros = obtener_info_med()

    for i, registro in enumerate(registros):
        tk.Label(frame_tabla, text=registro[0]).grid(row=i+1, column=0)
        tk.Label(frame_tabla, text=registro[1]).grid(row=i+1, column=1)
        tk.Label(frame_tabla, text=registro[2]).grid(row=i+1, column=2)

        # Botones para eliminar y editar
        tk.Button(frame_tabla, text="Eliminar", command=lambda id=registro[0]: eliminar_info_med(id)).grid(row=i+1, column=3)
        tk.Button(frame_tabla, text="Editar", command=lambda id=registro[0]: abrir_editar_info_med(id)).grid(row=i+1, column=4)

# Función para eliminar un registro de info_med
def eliminar_info_med(id_infomed):
    InfoMed.eliminar( id_infomed)
    mostrar_tabla()

# Función para abrir la ventana de edición
def abrir_editar_info_med(id_infomed):
    def editar():
        infomed = InfoMed(id_infomed, entry_id_med.get(), entry_id_info.get())
        infomed.actualizar()
        mostrar_tabla()
        ventana_editar.destroy()

    ventana_editar = tk.Toplevel(root)
    ventana_editar.title(f"Editar Relación de Medicamento con Información Educativa {id_infomed}")

    # Obtener los datos de info_med
    registro = InfoMed.obtener_por_id( id_infomed)

    if registro:
        # Campos para editar
        tk.Label(ventana_editar, text="ID Medicamento").grid(row=0, column=0)
        tk.Label(ventana_editar, text="ID Información Educativa").grid(row=1, column=0)

        entry_id_med = tk.Entry(ventana_editar)
        entry_id_med.insert(0, registro[1])  # Asignar valor del ID de medicamento
        entry_id_med.grid(row=0, column=1)

        entry_id_info = tk.Entry(ventana_editar)
        entry_id_info.insert(0, registro[2])  # Asignar valor del ID de info educativa
        entry_id_info.grid(row=1, column=1)

        tk.Button(ventana_editar, text="Guardar", command=editar).grid(row=2, column=1)

# Función para agregar un nuevo registro de info_med
def agregar():
    id_med = entry_id_med.get()
    id_info = entry_id_info.get()

    infomed = InfoMed(id_med=id_med, id_info=id_info)
    infomed.insertar()
    mostrar_tabla()

# Interfaz gráfica
root = tk.Tk()
root.title("Gestión de Medicamento-Información Educativa")

# Entrada de datos para agregar relación medicamento-infoEdu
tk.Label(root, text="ID Medicamento").grid(row=0, column=0)
tk.Label(root, text="ID Información Educativa").grid(row=1, column=0)

entry_id_med = tk.Entry(root)
entry_id_med.grid(row=0, column=1)

entry_id_info = tk.Entry(root)
entry_id_info.grid(row=1, column=1)

tk.Button(root, text="Agregar Relación", command=agregar).grid(row=2, column=1)

# Frame para la tabla
frame_tabla = tk.Frame(root)
frame_tabla.grid(row=3, column=0, columnspan=2)

# Mostrar la tabla de relaciones medicamento-información educativa
mostrar_tabla()

root.mainloop()
