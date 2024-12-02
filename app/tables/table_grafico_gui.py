import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import messagebox
from db.tables.grafico import Graficos

# Función para obtener todos los gráficos
def obtener_graficos():
    return Graficos.lista_graficos

# Función para mostrar la tabla de gráficos en la interfaz gráfica
def mostrar_tabla():
    for widget in frame_tabla.winfo_children():
        widget.destroy()

    graficos_entries = obtener_graficos()

    for i, grafico in enumerate(graficos_entries):
        tk.Label(frame_tabla, text=grafico.id_graf).grid(row=i+1, column=0)
        tk.Label(frame_tabla, text=grafico.titulo).grid(row=i+1, column=1)
        tk.Label(frame_tabla, text=grafico.id_user).grid(row=i+1, column=2)
        tk.Label(frame_tabla, text=grafico.id_rec).grid(row=i+1, column=3)
        tk.Label(frame_tabla, text=grafico.id_med).grid(row=i+1, column=4)
        tk.Label(frame_tabla, text=grafico.id_salud).grid(row=i+1, column=5)

        # Botones para eliminar y editar
        tk.Button(frame_tabla, text="Eliminar", command=lambda id=grafico.id_graf: eliminar_grafico(id)).grid(row=i+1, column=6)
        tk.Button(frame_tabla, text="Editar", command=lambda id=grafico.id_graf: abrir_editar_grafico(id)).grid(row=i+1, column=7)

# Función para eliminar un gráfico
def eliminar_grafico(id_graf):
    grafico = Graficos(None)  # Se pasa None porque el cursor no es necesario para este caso
    grafico.eliminar_grafico()
    mostrar_tabla()

# Función para abrir la ventana de edición
def abrir_editar_grafico(id_graf):
    def editar():
        grafico = Graficos(None, id_graf=id_graf, titulo=entry_titulo.get(), id_user=entry_id_user.get(),
                           id_rec=entry_id_rec.get(), id_med=entry_id_med.get(), id_salud=entry_id_salud.get())
        grafico.editar_grafico()
        mostrar_tabla()
        ventana_editar.destroy()

    ventana_editar = tk.Toplevel(root)
    ventana_editar.title(f"Editar Gráfico {id_graf}")

    # Obtener datos de gráfico
    grafico = next((entry for entry in obtener_graficos() if entry.id_graf == id_graf), None)

    if grafico:
        # Campos para editar
        tk.Label(ventana_editar, text="Título").grid(row=0, column=0)
        tk.Label(ventana_editar, text="ID Usuario").grid(row=1, column=0)
        tk.Label(ventana_editar, text="ID Recordatorio").grid(row=2, column=0)
        tk.Label(ventana_editar, text="ID Medicamento").grid(row=3, column=0)
        tk.Label(ventana_editar, text="ID Datos Salud").grid(row=4, column=0)

        entry_titulo = tk.Entry(ventana_editar)
        entry_titulo.insert(0, grafico.titulo)
        entry_titulo.grid(row=0, column=1)

        entry_id_user = tk.Entry(ventana_editar)
        entry_id_user.insert(0, grafico.id_user)
        entry_id_user.grid(row=1, column=1)

        entry_id_rec = tk.Entry(ventana_editar)
        entry_id_rec.insert(0, grafico.id_rec)
        entry_id_rec.grid(row=2, column=1)

        entry_id_med = tk.Entry(ventana_editar)
        entry_id_med.insert(0, grafico.id_med)
        entry_id_med.grid(row=3, column=1)

        entry_id_salud = tk.Entry(ventana_editar)
        entry_id_salud.insert(0, grafico.id_salud)
        entry_id_salud.grid(row=4, column=1)

        tk.Button(ventana_editar, text="Guardar", command=editar).grid(row=5, column=1)

# Función para agregar un nuevo gráfico
def agregar():
    id_graf = entry_id_graf.get()
    titulo = entry_titulo.get()
    id_user = entry_id_user.get()
    id_rec = entry_id_rec.get()
    id_med = entry_id_med.get()
    id_salud = entry_id_salud.get()

    grafico = Graficos(None, id_graf=id_graf, titulo=titulo, id_user=id_user, id_rec=id_rec, id_med=id_med, id_salud=id_salud)
    grafico.insertar_grafico()
    mostrar_tabla()

# Interfaz gráfica
root = tk.Tk()
root.title("Gestión de Gráficos")

# Entrada de datos para agregar gráfico
tk.Label(root, text="ID Gráfico").grid(row=0, column=0)
tk.Label(root, text="Título").grid(row=1, column=0)
tk.Label(root, text="ID Usuario").grid(row=2, column=0)
tk.Label(root, text="ID Recordatorio").grid(row=3, column=0)
tk.Label(root, text="ID Medicamento").grid(row=4, column=0)
tk.Label(root, text="ID Datos Salud").grid(row=5, column=0)

entry_id_graf = tk.Entry(root)
entry_id_graf.grid(row=0, column=1)

entry_titulo = tk.Entry(root)
entry_titulo.grid(row=1, column=1)

entry_id_user = tk.Entry(root)
entry_id_user.grid(row=2, column=1)

entry_id_rec = tk.Entry(root)
entry_id_rec.grid(row=3, column=1)

entry_id_med = tk.Entry(root)
entry_id_med.grid(row=4, column=1)

entry_id_salud = tk.Entry(root)
entry_id_salud.grid(row=5, column=1)

tk.Button(root, text="Agregar Gráfico", command=agregar).grid(row=6, column=1)

# Frame para la tabla
frame_tabla = tk.Frame(root)
frame_tabla.grid(row=7, column=0, columnspan=2)

# Mostrar la tabla de gráficos
mostrar_tabla()

root.mainloop()
