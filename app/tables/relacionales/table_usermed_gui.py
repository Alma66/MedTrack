import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import messagebox
from db.tables.relacionales.user_med import UserMed
from db.tables.medicamento import Medicamento
from db.tables.usuario import Usuario

# Función para obtener todos los registros de user_med
def obtener_user_med():
    return UserMed.obtener_todos()

# Función para mostrar la tabla user_med
def mostrar_tabla():
    for widget in frame_tabla.winfo_children():
        widget.destroy()

    registros = obtener_user_med()

    for i, registro in enumerate(registros):
        tk.Label(frame_tabla, text=registro[0]).grid(row=i+1, column=0)
        tk.Label(frame_tabla, text=registro[1]).grid(row=i+1, column=1)
        tk.Label(frame_tabla, text=registro[2]).grid(row=i+1, column=2)

        # Botones para eliminar y editar
        tk.Button(frame_tabla, text="Eliminar", command=lambda id=registro[0]: eliminar_user_med(id)).grid(row=i+1, column=3)
        tk.Button(frame_tabla, text="Editar", command=lambda id=registro[0]: abrir_editar_user_med(id)).grid(row=i+1, column=4)

# Función para eliminar un registro de user_med
def eliminar_user_med(id_usermed):
    UserMed.eliminar( id_usermed)
    mostrar_tabla()

# Función para abrir la ventana de edición
def abrir_editar_user_med(id_usermed):
    def editar():
        usermed = UserMed(id_usermed, entry_id_user.get(), entry_id_med.get())
        usermed.actualizar()
        mostrar_tabla()
        ventana_editar.destroy()

    ventana_editar = tk.Toplevel(root)
    ventana_editar.title(f"Editar Relación de Usuario con Medicamento {id_usermed}")

    # Obtener los datos de user_med
    registro = UserMed.obtener_por_id( id_usermed)

    if registro:
        # Campos para editar
        tk.Label(ventana_editar, text="ID Usuario").grid(row=0, column=0)
        tk.Label(ventana_editar, text="ID Medicamento").grid(row=1, column=0)

        entry_id_user = tk.Entry(ventana_editar)
        entry_id_user.insert(0, registro[1])  # Asignar valor del ID de usuario
        entry_id_user.grid(row=0, column=1)

        entry_id_med = tk.Entry(ventana_editar)
        entry_id_med.insert(0, registro[2])  # Asignar valor del ID de medicamento
        entry_id_med.grid(row=1, column=1)

        tk.Button(ventana_editar, text="Guardar", command=editar).grid(row=2, column=1)

# Función para agregar un nuevo registro de user_med
def agregar():
    id_user = entry_id_user.get()
    id_med = entry_id_med.get()

    usermed = UserMed(id_user=id_user, id_med=id_med)
    usermed.insertar()
    mostrar_tabla()

# Interfaz gráfica
root = tk.Tk()
root.title("Gestión de Usuario-Medicamento")

# Entrada de datos para agregar relación usuario-medicamento
tk.Label(root, text="ID Usuario").grid(row=0, column=0)
tk.Label(root, text="ID Medicamento").grid(row=1, column=0)

entry_id_user = tk.Entry(root)
entry_id_user.grid(row=0, column=1)

entry_id_med = tk.Entry(root)
entry_id_med.grid(row=1, column=1)

tk.Button(root, text="Agregar Relación", command=agregar).grid(row=2, column=1)

# Frame para la tabla
frame_tabla = tk.Frame(root)
frame_tabla.grid(row=3, column=0, columnspan=2)

# Mostrar la tabla de relaciones usuario-medicamento
mostrar_tabla()

root.mainloop()
