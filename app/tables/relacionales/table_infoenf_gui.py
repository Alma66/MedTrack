import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import messagebox
from db.tables.relacionales.info_enf import InfoEnf
from db.tables.enfermedad import Enfermedad
from db.tables.infoEdu import InfoEdu

# Función para obtener todos los registros de info_enf
def obtener_info_enf():
    return InfoEnf.obtener_todos()

# Función para mostrar la tabla info_enf
def mostrar_tabla():
    for widget in frame_tabla.winfo_children():
        widget.destroy()

    registros = obtener_info_enf()

    for i, registro in enumerate(registros):
        tk.Label(frame_tabla, text=registro[0]).grid(row=i+1, column=0)
        tk.Label(frame_tabla, text=registro[1]).grid(row=i+1, column=1)
        tk.Label(frame_tabla, text=registro[2]).grid(row=i+1, column=2)

        # Botones para eliminar y editar
        tk.Button(frame_tabla, text="Eliminar", command=lambda id=registro[0]: eliminar_info_enf(id)).grid(row=i+1, column=3)
        tk.Button(frame_tabla, text="Editar", command=lambda id=registro[0]: abrir_editar_info_enf(id)).grid(row=i+1, column=4)

# Función para eliminar un registro de info_enf
def eliminar_info_enf(id_infoenf):
    InfoEnf.eliminar( id_infoenf)
    mostrar_tabla()

# Función para abrir la ventana de edición
def abrir_editar_info_enf(id_infoenf):
    def editar():
        infoenf = InfoEnf(id_infoenf, entry_id_enf.get(), entry_id_info.get())
        infoenf.actualizar()
        mostrar_tabla()
        ventana_editar.destroy()

    ventana_editar = tk.Toplevel(root)
    ventana_editar.title(f"Editar Relación de Enfermedad con Información Educativa {id_infoenf}")

    # Obtener los datos de info_enf
    registro = InfoEnf.obtener_por_id( id_infoenf)

    if registro:
        # Campos para editar
        tk.Label(ventana_editar, text="ID Enfermedad").grid(row=0, column=0)
        tk.Label(ventana_editar, text="ID Información Educativa").grid(row=1, column=0)

        entry_id_enf = tk.Entry(ventana_editar)
        entry_id_enf.insert(0, registro[1])  # Asignar valor del ID de enfermedad
        entry_id_enf.grid(row=0, column=1)

        entry_id_info = tk.Entry(ventana_editar)
        entry_id_info.insert(0, registro[2])  # Asignar valor del ID de info educativa
        entry_id_info.grid(row=1, column=1)

        tk.Button(ventana_editar, text="Guardar", command=editar).grid(row=2, column=1)

# Función para agregar un nuevo registro de info_enf
def agregar():
    id_enf = entry_id_enf.get()
    id_info = entry_id_info.get()

    infoenf = InfoEnf(id_enf=id_enf, id_info=id_info)
    infoenf.insertar()
    mostrar_tabla()

# Interfaz gráfica
root = tk.Tk()
root.title("Gestión de Enfermedad-Información Educativa")

# Entrada de datos para agregar relación enfermedad-infoEdu
tk.Label(root, text="ID Enfermedad").grid(row=0, column=0)
tk.Label(root, text="ID Información Educativa").grid(row=1, column=0)

entry_id_enf = tk.Entry(root)
entry_id_enf.grid(row=0, column=1)

entry_id_info = tk.Entry(root)
entry_id_info.grid(row=1, column=1)

tk.Button(root, text="Agregar Relación", command=agregar).grid(row=2, column=1)

# Frame para la tabla
frame_tabla = tk.Frame(root)
frame_tabla.grid(row=3, column=0, columnspan=2)

# Mostrar la tabla de relaciones enfermedad-información educativa
mostrar_tabla()

root.mainloop()
