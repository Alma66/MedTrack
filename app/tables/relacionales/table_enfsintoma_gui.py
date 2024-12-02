import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import messagebox
from db.tables.relacionales.enf_sintoma import EnfSintoma
from db.tables.enfermedad import Enfermedad
from db.tables.sintoma import Sintoma


# Función para obtener todos los registros de enf_sintoma
def obtener_enf_sintomas():
    return EnfSintoma.obtener_todos()

# Función para mostrar la tabla enf_sintoma
def mostrar_tabla():
    for widget in frame_tabla.winfo_children():
        widget.destroy()

    registros = obtener_enf_sintomas()

    for i, registro in enumerate(registros):
        tk.Label(frame_tabla, text=registro[0]).grid(row=i+1, column=0)  # id_enfsintoma
        tk.Label(frame_tabla, text=registro[1]).grid(row=i+1, column=1)  # id_sintoma
        tk.Label(frame_tabla, text=registro[2]).grid(row=i+1, column=2)  # id_enf

        # Botones para eliminar y editar
        tk.Button(frame_tabla, text="Eliminar", command=lambda id=registro[0]: eliminar_enf_sintoma(id)).grid(row=i+1, column=3)
        tk.Button(frame_tabla, text="Editar", command=lambda id=registro[0]: abrir_editar_enf_sintoma(id)).grid(row=i+1, column=4)

# Función para eliminar un registro de enf_sintoma
def eliminar_enf_sintoma(id_enfsintoma):
    EnfSintoma.eliminar( id_enfsintoma)
    mostrar_tabla()

# Función para abrir la ventana de edición
def abrir_editar_enf_sintoma(id_enfsintoma):
    def editar():
        try:
            enf_sintoma = EnfSintoma(id_enfsintoma, entry_id_sintoma.get(), entry_id_enf.get())
            enf_sintoma.actualizar()
            mostrar_tabla()
            ventana_editar.destroy()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    ventana_editar = tk.Toplevel(root)
    ventana_editar.title(f"Editar Relación de Enfermedad y Síntoma {id_enfsintoma}")

    # Obtener los datos de enf_sintoma
    registro = EnfSintoma.obtener_por_id( id_enfsintoma)

    if registro:
        tk.Label(ventana_editar, text="ID Síntoma").grid(row=0, column=0)
        tk.Label(ventana_editar, text="ID Enfermedad").grid(row=1, column=0)

        entry_id_sintoma = tk.Entry(ventana_editar)
        entry_id_sintoma.insert(0, registro[1])
        entry_id_sintoma.grid(row=0, column=1)

        entry_id_enf = tk.Entry(ventana_editar)
        entry_id_enf.insert(0, registro[2])
        entry_id_enf.grid(row=1, column=1)

        tk.Button(ventana_editar, text="Guardar", command=editar).grid(row=2, column=1)

# Función para agregar un nuevo registro de enf_sintoma
def agregar():
    id_sintoma = entry_id_sintoma.get()
    id_enf = entry_id_enf.get()

    if not id_sintoma or not id_enf:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return

    enf_sintoma = EnfSintoma(id_sintoma=id_sintoma, id_enf=id_enf)
    enf_sintoma.insertar()
    mostrar_tabla()

# Interfaz gráfica
root = tk.Tk()
root.title("Gestión de Enfermedades y Síntomas")

# Entrada de datos para agregar relación enf_sintoma
tk.Label(root, text="ID Síntoma").grid(row=0, column=0)
tk.Label(root, text="ID Enfermedad").grid(row=1, column=0)

entry_id_sintoma = tk.Entry(root)
entry_id_sintoma.grid(row=0, column=1)

entry_id_enf = tk.Entry(root)
entry_id_enf.grid(row=1, column=1)

tk.Button(root, text="Agregar Relación", command=agregar).grid(row=2, column=1)

# Frame para la tabla
frame_tabla = tk.Frame(root)
frame_tabla.grid(row=3, column=0, columnspan=2)

# Mostrar la tabla de relaciones enf_sintoma
mostrar_tabla()

root.mainloop()
