import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import messagebox
from db.tables.relacionales.enf_datos import EnfDatos
from db.tables.enfermedad import Enfermedad
from db.tables.datosSalud import DatosSalud


# Función para obtener todos los registros de enf_datos
def obtener_enf_datos():
    return EnfDatos.obtener_todos()

# Función para mostrar la tabla enf_datos
def mostrar_tabla():
    for widget in frame_tabla.winfo_children():
        widget.destroy()

    registros = obtener_enf_datos()

    for i, registro in enumerate(registros):
        tk.Label(frame_tabla, text=registro[0]).grid(row=i+1, column=0)  # id_enfdatos
        tk.Label(frame_tabla, text=registro[1]).grid(row=i+1, column=1)  # id_salud
        tk.Label(frame_tabla, text=registro[2]).grid(row=i+1, column=2)  # id_enf

        # Botones para eliminar y editar
        tk.Button(frame_tabla, text="Eliminar", command=lambda id=registro[0]: eliminar_enf_dato(id)).grid(row=i+1, column=3)
        tk.Button(frame_tabla, text="Editar", command=lambda id=registro[0]: abrir_editar_enf_dato(id)).grid(row=i+1, column=4)

# Función para eliminar un registro de enf_datos
def eliminar_enf_dato(id_enfdatos):
    EnfDatos.eliminar( id_enfdatos)
    mostrar_tabla()

# Función para abrir la ventana de edición
def abrir_editar_enf_dato(id_enfdatos):
    def editar():
        try:
            enf_dato = EnfDatos(id_enfdatos, entry_id_salud.get(), entry_id_enf.get())
            enf_dato.actualizar()
            mostrar_tabla()
            ventana_editar.destroy()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    ventana_editar = tk.Toplevel(root)
    ventana_editar.title(f"Editar Relación de Salud y Enfermedad {id_enfdatos}")

    # Obtener los datos de enf_datos
    registro = EnfDatos.obtener_por_id( id_enfdatos)

    if registro:
        tk.Label(ventana_editar, text="ID Salud").grid(row=0, column=0)
        tk.Label(ventana_editar, text="ID Enfermedad").grid(row=1, column=0)

        entry_id_salud = tk.Entry(ventana_editar)
        entry_id_salud.insert(0, registro[1])
        entry_id_salud.grid(row=0, column=1)

        entry_id_enf = tk.Entry(ventana_editar)
        entry_id_enf.insert(0, registro[2])
        entry_id_enf.grid(row=1, column=1)

        tk.Button(ventana_editar, text="Guardar", command=editar).grid(row=2, column=1)

# Función para agregar un nuevo registro de enf_datos
def agregar():
    id_salud = entry_id_salud.get()
    id_enf = entry_id_enf.get()

    if not id_salud or not id_enf:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return

    enf_dato = EnfDatos(id_salud=id_salud, id_enf=id_enf)
    enf_dato.insertar()
    mostrar_tabla()

# Interfaz gráfica
root = tk.Tk()
root.title("Gestión de Salud y Enfermedades")

# Entrada de datos para agregar relación enf_datos
tk.Label(root, text="ID Salud").grid(row=0, column=0)
tk.Label(root, text="ID Enfermedad").grid(row=1, column=0)

entry_id_salud = tk.Entry(root)
entry_id_salud.grid(row=0, column=1)

entry_id_enf = tk.Entry(root)
entry_id_enf.grid(row=1, column=1)

tk.Button(root, text="Agregar Relación", command=agregar).grid(row=2, column=1)

# Frame para la tabla
frame_tabla = tk.Frame(root)
frame_tabla.grid(row=3, column=0, columnspan=2)

# Mostrar la tabla de relaciones enf_datos
mostrar_tabla()

root.mainloop()
