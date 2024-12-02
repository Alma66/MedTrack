import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import messagebox
from db.tables.relacionales.info_datos import InfoDatos
from db.tables.infoEdu import InfoEdu
from db.tables.datosSalud import DatosSalud

# Función para obtener todos los registros de info_datos
def obtener_info_datos():
    return InfoDatos.obtener_todos()

# Función para mostrar la tabla info_datos
def mostrar_tabla():
    for widget in frame_tabla.winfo_children():
        widget.destroy()

    registros = obtener_info_datos()

    for i, registro in enumerate(registros):
        tk.Label(frame_tabla, text=registro[0]).grid(row=i+1, column=0)  # id_info_datos
        tk.Label(frame_tabla, text=registro[1]).grid(row=i+1, column=1)  # id_salud
        tk.Label(frame_tabla, text=registro[2]).grid(row=i+1, column=2)  # id_info

        # Botones para eliminar y editar
        tk.Button(frame_tabla, text="Eliminar", command=lambda id=registro[0]: eliminar_info_datos(id)).grid(row=i+1, column=3)
        tk.Button(frame_tabla, text="Editar", command=lambda id=registro[0]: abrir_editar_info_datos(id)).grid(row=i+1, column=4)

# Función para eliminar un registro de info_datos
def eliminar_info_datos(id_info_datos):
    InfoDatos.eliminar( id_info_datos)
    mostrar_tabla()

# Función para abrir la ventana de edición
def abrir_editar_info_datos(id_info_datos):
    def editar():
        try:
            info_datos = InfoDatos(id_info_datos, entry_id_salud.get(), entry_id_info.get())
            info_datos.actualizar()
            mostrar_tabla()
            ventana_editar.destroy()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    ventana_editar = tk.Toplevel(root)
    ventana_editar.title(f"Editar Relación de Datos Salud e Información {id_info_datos}")

    # Obtener los datos de info_datos
    registro = InfoDatos.obtener_por_id( id_info_datos)

    if registro:
        tk.Label(ventana_editar, text="ID Salud").grid(row=0, column=0)
        tk.Label(ventana_editar, text="ID Información").grid(row=1, column=0)

        entry_id_salud = tk.Entry(ventana_editar)
        entry_id_salud.insert(0, registro[1])
        entry_id_salud.grid(row=0, column=1)

        entry_id_info = tk.Entry(ventana_editar)
        entry_id_info.insert(0, registro[2])
        entry_id_info.grid(row=1, column=1)

        tk.Button(ventana_editar, text="Guardar", command=editar).grid(row=2, column=1)

# Función para agregar un nuevo registro de info_datos
def agregar():
    id_salud = entry_id_salud.get()
    id_info = entry_id_info.get()

    if not id_salud or not id_info:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return

    info_datos = InfoDatos(id_salud=id_salud, id_info=id_info)
    info_datos.insertar()
    mostrar_tabla()

# Interfaz gráfica
root = tk.Tk()
root.title("Gestión de Datos de Salud e Información Educativa")

# Entrada de datos para agregar relación datosSalud-infoEdu
tk.Label(root, text="ID Salud").grid(row=0, column=0)
tk.Label(root, text="ID Información").grid(row=1, column=0)

entry_id_salud = tk.Entry(root)
entry_id_salud.grid(row=0, column=1)

entry_id_info = tk.Entry(root)
entry_id_info.grid(row=1, column=1)

tk.Button(root, text="Agregar Relación", command=agregar).grid(row=2, column=1)

# Frame para la tabla
frame_tabla = tk.Frame(root)
frame_tabla.grid(row=3, column=0, columnspan=2)

# Mostrar la tabla de relaciones datosSalud-infoEdu
mostrar_tabla()

root.mainloop()

