import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import messagebox
from db.tables.infoEdu import InfoEdu

# Función para obtener todas las entradas de infoEdu
def obtener_infoedu():
    return InfoEdu.lista_infoedu

# Función para mostrar la tabla de infoEdu en la interfaz gráfica
def mostrar_tabla():
    for widget in frame_tabla.winfo_children():
        widget.destroy()

    infoedu_entries = obtener_infoedu()

    for i, infoedu in enumerate(infoedu_entries):
        tk.Label(frame_tabla, text=infoedu.id_info).grid(row=i+1, column=0)
        tk.Label(frame_tabla, text=infoedu.titulo).grid(row=i+1, column=1)
        tk.Label(frame_tabla, text=infoedu.contenido).grid(row=i+1, column=2)
        tk.Label(frame_tabla, text=infoedu.creditos).grid(row=i+1, column=3)
        tk.Label(frame_tabla, text=infoedu.id_user).grid(row=i+1, column=4)

        # Botones para eliminar y editar
        tk.Button(frame_tabla, text="Eliminar", command=lambda id=infoedu.id_info: eliminar_infoedu(id)).grid(row=i+1, column=5)
        tk.Button(frame_tabla, text="Editar", command=lambda id=infoedu.id_info: abrir_editar_infoedu(id)).grid(row=i+1, column=6)

# Función para eliminar un infoEdu
def eliminar_infoedu(id_info):
    infoedu = InfoEdu(None)  # Se pasa None porque el cursor no es necesario para este caso
    infoedu.eliminar_infoedu()
    mostrar_tabla()

# Función para abrir la ventana de edición
def abrir_editar_infoedu(id_info):
    def editar():
        infoedu = InfoEdu(None, id_info=id_info, titulo=entry_titulo.get(), contenido=entry_contenido.get(),
                          creditos=entry_creditos.get(), id_user=entry_id_user.get())
        infoedu.editar_infoedu()
        mostrar_tabla()
        ventana_editar.destroy()

    ventana_editar = tk.Toplevel(root)
    ventana_editar.title(f"Editar InfoEdu {id_info}")

    # Obtener datos de infoEdu
    infoedu = next((entry for entry in obtener_infoedu() if entry.id_info == id_info), None)

    if infoedu:
        # Campos para editar
        tk.Label(ventana_editar, text="Título").grid(row=0, column=0)
        tk.Label(ventana_editar, text="Contenido").grid(row=1, column=0)
        tk.Label(ventana_editar, text="Créditos").grid(row=2, column=0)
        tk.Label(ventana_editar, text="ID Usuario").grid(row=3, column=0)

        entry_titulo = tk.Entry(ventana_editar)
        entry_titulo.insert(0, infoedu.titulo)
        entry_titulo.grid(row=0, column=1)

        entry_contenido = tk.Entry(ventana_editar)
        entry_contenido.insert(0, infoedu.contenido)
        entry_contenido.grid(row=1, column=1)

        entry_creditos = tk.Entry(ventana_editar)
        entry_creditos.insert(0, infoedu.creditos)
        entry_creditos.grid(row=2, column=1)

        entry_id_user = tk.Entry(ventana_editar)
        entry_id_user.insert(0, infoedu.id_user)
        entry_id_user.grid(row=3, column=1)

        tk.Button(ventana_editar, text="Guardar", command=editar).grid(row=4, column=1)

# Función para agregar un nuevo infoEdu
def agregar():
    id_info = entry_id_info.get()
    titulo = entry_titulo.get()
    contenido = entry_contenido.get()
    creditos = entry_creditos.get()
    id_user = entry_id_user.get()

    infoedu = InfoEdu(None, id_info=id_info, titulo=titulo, contenido=contenido, creditos=creditos, id_user=id_user)
    infoedu.insertar_infoedu()
    mostrar_tabla()

# Interfaz gráfica
root = tk.Tk()
root.title("Gestión de Información Educativa")

# Entrada de datos para agregar infoEdu
tk.Label(root, text="ID InfoEdu").grid(row=0, column=0)
tk.Label(root, text="Título").grid(row=1, column=0)
tk.Label(root, text="Contenido").grid(row=2, column=0)
tk.Label(root, text="Créditos").grid(row=3, column=0)
tk.Label(root, text="ID Usuario").grid(row=4, column=0)

entry_id_info = tk.Entry(root)
entry_id_info.grid(row=0, column=1)

entry_titulo = tk.Entry(root)
entry_titulo.grid(row=1, column=1)

entry_contenido = tk.Entry(root)
entry_contenido.grid(row=2, column=1)

entry_creditos = tk.Entry(root)
entry_creditos.grid(row=3, column=1)

entry_id_user = tk.Entry(root)
entry_id_user.grid(row=4, column=1)

tk.Button(root, text="Agregar InfoEdu", command=agregar).grid(row=5, column=1)

# Frame para la tabla
frame_tabla = tk.Frame(root)
frame_tabla.grid(row=6, column=0, columnspan=2)

# Mostrar la tabla de infoEdu
mostrar_tabla()

root.mainloop()
