import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import messagebox
from db.tables.recordatorio import Recordatorio

# Función para obtener todos los recordatorios
def obtener_recordatorios():
    return Recordatorio.lista_recordatorios

# Función para mostrar la tabla de recordatorios en la interfaz gráfica
def mostrar_tabla():
    for widget in frame_tabla.winfo_children():
        widget.destroy()

    recordatorios = obtener_recordatorios()

    for i, recordatorio in enumerate(recordatorios):
        tk.Label(frame_tabla, text=recordatorio.id_rec).grid(row=i+1, column=0)
        tk.Label(frame_tabla, text=recordatorio.hora).grid(row=i+1, column=1)
        tk.Label(frame_tabla, text=recordatorio.dosis).grid(row=i+1, column=2)
        tk.Label(frame_tabla, text=recordatorio.estado).grid(row=i+1, column=3)
        tk.Label(frame_tabla, text=recordatorio.frecuencia).grid(row=i+1, column=4)
        tk.Label(frame_tabla, text=recordatorio.id_user).grid(row=i+1, column=5)
        tk.Label(frame_tabla, text=recordatorio.id_med).grid(row=i+1, column=6)

        # Botones para eliminar y editar
        tk.Button(frame_tabla, text="Eliminar", command=lambda id=recordatorio.id_rec: eliminar_recordatorio(id)).grid(row=i+1, column=7)
        tk.Button(frame_tabla, text="Editar", command=lambda id=recordatorio.id_rec: abrir_editar_recordatorio(id)).grid(row=i+1, column=8)

# Función para eliminar un recordatorio
def eliminar_recordatorio(id_rec):
    recordatorio = Recordatorio(None)  # Se pasa None porque el cursor no es necesario para este caso
    recordatorio.eliminar_recordatorio(id_rec)
    mostrar_tabla()

# Función para abrir la ventana de edición
def abrir_editar_recordatorio(id_rec):
    def editar():
        recordatorio = Recordatorio(None, id_rec=id_rec, hora=entry_hora.get(), dosis=entry_dosis.get(),
                                    estado=entry_estado.get(), frecuencia=entry_frecuencia.get(),
                                    id_user=entry_id_user.get(), id_med=entry_id_med.get())
        recordatorio.editar_recordatorio(id_rec)
        mostrar_tabla()
        ventana_editar.destroy()

    ventana_editar = tk.Toplevel(root)
    ventana_editar.title(f"Editar Recordatorio {id_rec}")

    # Obtener datos del recordatorio
    recordatorio = next((rec for rec in obtener_recordatorios() if rec.id_rec == id_rec), None)

    if recordatorio:
        # Campos para editar
        tk.Label(ventana_editar, text="Hora").grid(row=0, column=0)
        tk.Label(ventana_editar, text="Dosis").grid(row=1, column=0)
        tk.Label(ventana_editar, text="Estado").grid(row=2, column=0)
        tk.Label(ventana_editar, text="Frecuencia").grid(row=3, column=0)
        tk.Label(ventana_editar, text="ID Usuario").grid(row=4, column=0)
        tk.Label(ventana_editar, text="ID Medicamento").grid(row=5, column=0)

        entry_hora = tk.Entry(ventana_editar)
        entry_hora.insert(0, recordatorio.hora)
        entry_hora.grid(row=0, column=1)

        entry_dosis = tk.Entry(ventana_editar)
        entry_dosis.insert(0, recordatorio.dosis)
        entry_dosis.grid(row=1, column=1)

        entry_estado = tk.Entry(ventana_editar)
        entry_estado.insert(0, recordatorio.estado)
        entry_estado.grid(row=2, column=1)

        entry_frecuencia = tk.Entry(ventana_editar)
        entry_frecuencia.insert(0, recordatorio.frecuencia)
        entry_frecuencia.grid(row=3, column=1)

        entry_id_user = tk.Entry(ventana_editar)
        entry_id_user.insert(0, recordatorio.id_user)
        entry_id_user.grid(row=4, column=1)

        entry_id_med = tk.Entry(ventana_editar)
        entry_id_med.insert(0, recordatorio.id_med)
        entry_id_med.grid(row=5, column=1)

        tk.Button(ventana_editar, text="Guardar", command=editar).grid(row=6, column=1)

# Función para agregar un nuevo recordatorio
def agregar():
    id_rec = entry_id_rec.get()
    hora = entry_hora.get()
    dosis = entry_dosis.get()
    estado = entry_estado.get()
    frecuencia = entry_frecuencia.get()
    id_user = entry_id_user.get()
    id_med = entry_id_med.get()
    recordatorio = Recordatorio(None, id_rec=id_rec, hora=hora, dosis=dosis, estado=estado,
                                frecuencia=frecuencia, id_user=id_user, id_med=id_med)
    recordatorio.agregar_recordatorio(id_rec, hora, dosis, estado, frecuencia, id_user, id_med)
    mostrar_tabla()

# Interfaz gráfica
root = tk.Tk()
root.title("Gestión de Recordatorios")

# Entrada de datos para agregar recordatorios
tk.Label(root, text="ID Recordatorio").grid(row=0, column=0)
tk.Label(root, text="Hora").grid(row=1, column=0)
tk.Label(root, text="Dosis").grid(row=2, column=0)
tk.Label(root, text="Estado").grid(row=3, column=0)
tk.Label(root, text="Frecuencia").grid(row=4, column=0)
tk.Label(root, text="ID Usuario").grid(row=5, column=0)
tk.Label(root, text="ID Medicamento").grid(row=6, column=0)

entry_id_rec = tk.Entry(root)
entry_id_rec.grid(row=0, column=1)

entry_hora = tk.Entry(root)
entry_hora.grid(row=1, column=1)

entry_dosis = tk.Entry(root)
entry_dosis.grid(row=2, column=1)

entry_estado = tk.Entry(root)
entry_estado.grid(row=3, column=1)

entry_frecuencia = tk.Entry(root)
entry_frecuencia.grid(row=4, column=1)

entry_id_user = tk.Entry(root)
entry_id_user.grid(row=5, column=1)

entry_id_med = tk.Entry(root)
entry_id_med.grid(row=6, column=1)

tk.Button(root, text="Agregar Recordatorio", command=agregar).grid(row=7, column=1)

# Frame para la tabla
frame_tabla = tk.Frame(root)
frame_tabla.grid(row=8, column=0, columnspan=2)

# Mostrar la tabla de recordatorios
mostrar_tabla()

root.mainloop()
