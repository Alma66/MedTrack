import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import messagebox
from db.tables.medicamento import Medicamento

# Función para obtener todos los medicamentos
def obtener_medicamentos():
    medicamento = Medicamento()
    return medicamento.mostrar_medicamentos()

# Función para mostrar la tabla de medicamentos en la interfaz gráfica
def mostrar_tabla():
    for widget in frame_tabla.winfo_children():
        widget.destroy()

    medicamentos = obtener_medicamentos()

    for i, med in enumerate(medicamentos):
        tk.Label(frame_tabla, text=med[0]).grid(row=i+1, column=0)  # id_med
        tk.Label(frame_tabla, text=med[1]).grid(row=i+1, column=1)  # nombre
        tk.Label(frame_tabla, text=med[2]).grid(row=i+1, column=2)  # detalles
        tk.Label(frame_tabla, text=med[3]).grid(row=i+1, column=3)  # efec_secun

        # Botones para eliminar y editar
        tk.Button(frame_tabla, text="Eliminar", command=lambda id=med[0]: eliminar_medicamento(id)).grid(row=i+1, column=4)
        tk.Button(frame_tabla, text="Editar", command=lambda id=med[0]: abrir_editar_medicamento(id)).grid(row=i+1, column=5)

# Función para eliminar un medicamento
def eliminar_medicamento(id_med):
    medicamento = Medicamento(id_med=id_med)
    medicamento.eliminar_medicamento()
    mostrar_tabla()

# Función para abrir la ventana de edición
def abrir_editar_medicamento(id_med):
    def editar():
        medicamento = Medicamento(id_med=id_med, nombre=entry_nombre.get(), detalles=entry_detalles.get(),
                                  efec_secun=entry_efec_secun.get())
        medicamento.editar_medicamento()
        mostrar_tabla()
        ventana_editar.destroy()

    ventana_editar = tk.Toplevel(root)
    ventana_editar.title(f"Editar Medicamento {id_med}")

    # Obtener datos del medicamento
    medicamento = next((med for med in obtener_medicamentos() if med[0] == id_med), None)

    if medicamento:
        # Campos para editar
        tk.Label(ventana_editar, text="Nombre").grid(row=0, column=0)
        tk.Label(ventana_editar, text="Detalles").grid(row=1, column=0)
        tk.Label(ventana_editar, text="Efectos Secundarios").grid(row=2, column=0)

        entry_nombre = tk.Entry(ventana_editar)
        entry_nombre.insert(0, medicamento[1])
        entry_nombre.grid(row=0, column=1)

        entry_detalles = tk.Entry(ventana_editar)
        entry_detalles.insert(0, medicamento[2])
        entry_detalles.grid(row=1, column=1)

        entry_efec_secun = tk.Entry(ventana_editar)
        entry_efec_secun.insert(0, medicamento[3])
        entry_efec_secun.grid(row=2, column=1)

        tk.Button(ventana_editar, text="Guardar", command=editar).grid(row=3, column=1)

# Función para agregar un nuevo medicamento
def agregar():
    id_med = entry_id_med.get()
    nombre = entry_nombre.get()
    detalles = entry_detalles.get()
    efec_secun = entry_efec_secun.get()
    medicamento = Medicamento(id_med=id_med, nombre=nombre, detalles=detalles, efec_secun=efec_secun)
    medicamento.insertar_medicamento()
    mostrar_tabla()

# Interfaz gráfica
root = tk.Tk()
root.title("Gestión de Medicamentos")

# Entrada de datos para agregar medicamentos
tk.Label(root, text="ID Medicamento").grid(row=0, column=0)
tk.Label(root, text="Nombre").grid(row=1, column=0)
tk.Label(root, text="Detalles").grid(row=2, column=0)
tk.Label(root, text="Efectos Secundarios").grid(row=3, column=0)

entry_id_med = tk.Entry(root)
entry_id_med.grid(row=0, column=1)

entry_nombre = tk.Entry(root)
entry_nombre.grid(row=1, column=1)

entry_detalles = tk.Entry(root)
entry_detalles.grid(row=2, column=1)

entry_efec_secun = tk.Entry(root)
entry_efec_secun.grid(row=3, column=1)

tk.Button(root, text="Agregar Medicamento", command=agregar).grid(row=4, column=1)

# Frame para la tabla
frame_tabla = tk.Frame(root)
frame_tabla.grid(row=5, column=0, columnspan=2)

# Mostrar la tabla de medicamentos
mostrar_tabla()

root.mainloop()
