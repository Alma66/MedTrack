import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import messagebox
from db.tables.datosSalud import DatosSalud

# Función para obtener todos los registros de datos de salud
def obtener_datos_salud():
    return DatosSalud.lista_datos_salud

# Función para mostrar la tabla de datos de salud en la interfaz gráfica
def mostrar_tabla():
    for widget in frame_tabla.winfo_children():
        widget.destroy()

    datos_salud_entries = obtener_datos_salud()

    for i, datos in enumerate(datos_salud_entries):
        tk.Label(frame_tabla, text=datos.id_salud).grid(row=i+1, column=0)
        tk.Label(frame_tabla, text=datos.id_user).grid(row=i+1, column=1)
        tk.Label(frame_tabla, text=datos.altura).grid(row=i+1, column=2)
        tk.Label(frame_tabla, text=datos.peso).grid(row=i+1, column=3)
        tk.Label(frame_tabla, text=datos.presion).grid(row=i+1, column=4)

        # Botones para eliminar y editar
        tk.Button(frame_tabla, text="Eliminar", command=lambda id=datos.id_salud: eliminar_datos_salud(id)).grid(row=i+1, column=5)
        tk.Button(frame_tabla, text="Editar", command=lambda id=datos.id_salud: abrir_editar_datos_salud(id)).grid(row=i+1, column=6)

# Función para eliminar los datos de salud
def eliminar_datos_salud(id_salud):
    datos = DatosSalud(None)  # Se pasa None porque el cursor no es necesario para este caso
    datos.eliminar_datosSalud()
    mostrar_tabla()

# Función para abrir la ventana de edición
def abrir_editar_datos_salud(id_salud):
    def editar():
        datos = DatosSalud(None, id_salud=id_salud, altura=entry_altura.get(), peso=entry_peso.get(), presion=entry_presion.get())
        datos.editar_datosSalud()
        mostrar_tabla()
        ventana_editar.destroy()

    ventana_editar = tk.Toplevel(root)
    ventana_editar.title(f"Editar Datos de Salud {id_salud}")

    # Obtener datos de salud
    datos = next((entry for entry in obtener_datos_salud() if entry.id_salud == id_salud), None)

    if datos:
        # Campos para editar
        tk.Label(ventana_editar, text="Altura").grid(row=0, column=0)
        tk.Label(ventana_editar, text="Peso").grid(row=1, column=0)
        tk.Label(ventana_editar, text="Presión").grid(row=2, column=0)

        entry_altura = tk.Entry(ventana_editar)
        entry_altura.insert(0, datos.altura)
        entry_altura.grid(row=0, column=1)

        entry_peso = tk.Entry(ventana_editar)
        entry_peso.insert(0, datos.peso)
        entry_peso.grid(row=1, column=1)

        entry_presion = tk.Entry(ventana_editar)
        entry_presion.insert(0, datos.presion)
        entry_presion.grid(row=2, column=1)

        tk.Button(ventana_editar, text="Guardar", command=editar).grid(row=3, column=1)

# Función para agregar un nuevo registro de datos de salud
def agregar():
    id_salud = entry_id_salud.get()
    id_user = entry_id_user.get()
    altura = entry_altura.get()
    peso = entry_peso.get()
    presion = entry_presion.get()

    datos = DatosSalud(None, id_salud=id_salud, id_user=id_user, altura=altura, peso=peso, presion=presion)
    datos.insertar_datosSalud()
    mostrar_tabla()

# Interfaz gráfica
root = tk.Tk()
root.title("Gestión de Datos de Salud")

# Entrada de datos para agregar registro de salud
tk.Label(root, text="ID Salud").grid(row=0, column=0)
tk.Label(root, text="ID Usuario").grid(row=1, column=0)
tk.Label(root, text="Altura").grid(row=2, column=0)
tk.Label(root, text="Peso").grid(row=3, column=0)
tk.Label(root, text="Presión").grid(row=4, column=0)

entry_id_salud = tk.Entry(root)
entry_id_salud.grid(row=0, column=1)

entry_id_user = tk.Entry(root)
entry_id_user.grid(row=1, column=1)

entry_altura = tk.Entry(root)
entry_altura.grid(row=2, column=1)

entry_peso = tk.Entry(root)
entry_peso.grid(row=3, column=1)

entry_presion = tk.Entry(root)
entry_presion.grid(row=4, column=1)

tk.Button(root, text="Agregar Datos de Salud", command=agregar).grid(row=5, column=1)

# Frame para la tabla
frame_tabla = tk.Frame(root)
frame_tabla.grid(row=6, column=0, columnspan=2)

# Mostrar la tabla de datos de salud
mostrar_tabla()

root.mainloop()
