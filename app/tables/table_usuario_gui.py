import sys
import os
import tkinter as tk
from tkinter import messagebox
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db.tables.usuario import Usuario
 

# Función para obtener todos los usuarios
def obtener_usuarios():
    return Usuario.lista_usuarios

# Función para mostrar la tabla de usuarios en la interfaz gráfica
def mostrar_tabla():
    """Despliega los usuarios en el frame de tabla con botones para editar y eliminar."""
    for widget in frame_tabla.winfo_children():
        widget.destroy()

    usuarios = obtener_usuarios()

    # Encabezados de la tabla
    encabezados = ["ID", "Nombre", "Apellido", "Fecha Nac.", "Sexo", "Mail", "Contraseña", "Acciones"]
    for col, encabezado in enumerate(encabezados):
        tk.Label(frame_tabla, text=encabezado, font=("Arial", 10, "bold")).grid(row=0, column=col, padx=5, pady=5)

    # Contenido de la tabla
    for i, usuario in enumerate(usuarios):
        tk.Label(frame_tabla, text=usuario.id_user).grid(row=i + 1, column=0)
        tk.Label(frame_tabla, text=usuario.nombre).grid(row=i + 1, column=1)
        tk.Label(frame_tabla, text=usuario.apellido).grid(row=i + 1, column=2)
        tk.Label(frame_tabla, text=usuario.fecha_nac).grid(row=i + 1, column=3)
        tk.Label(frame_tabla, text=usuario.sexo).grid(row=i + 1, column=4)
        tk.Label(frame_tabla, text=usuario.mail).grid(row=i + 1, column=5)
        tk.Label(frame_tabla, text=usuario.contraseña).grid(row=i + 1, column=6)

        # Botones para eliminar y editar
        tk.Button(frame_tabla, text="Eliminar", command=lambda id=usuario.id_user: eliminar_usuario(id)).grid(row=i + 1, column=7)
        tk.Button(frame_tabla, text="Editar", command=lambda id=usuario.id_user: abrir_editar_usuario(id)).grid(row=i + 1, column=8)

# Función para eliminar un usuario
def eliminar_usuario(id_user):
    """Elimina un usuario por ID y actualiza la tabla."""
    if messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas eliminar este usuario?"):
        Usuario.eliminar_usuario(id_user)
        mostrar_tabla()

# Función para abrir la ventana de edición
def abrir_editar_usuario(id_user):
    """Abre una ventana emergente para editar los datos del usuario."""
    usuario = next((u for u in Usuario.lista_usuarios if u.id_user == id_user), None)
    if not usuario:
        messagebox.showerror("Error", f"No se encontró el usuario con ID {id_user}.")
        return

    ventana_editar = tk.Toplevel(root)
    ventana_editar.title(f"Editar Usuario {id_user}")

    def guardar_cambios():
        Usuario.editar_usuario(
            id_user,
            entry_nombre.get(),
            entry_apellido.get(),
            entry_fecha_nac.get(),
            entry_sexo.get(),
            entry_mail.get(),
            entry_contraseña.get()
        )
        mostrar_tabla()
        ventana_editar.destroy()

    campos = ["Nombre", "Apellido", "Fecha Nac.", "Sexo", "Mail", "Contraseña"]
    valores = [usuario.nombre, usuario.apellido, usuario.fecha_nac, usuario.sexo, usuario.mail, usuario.contraseña]
    entradas = []

    for i, (campo, valor) in enumerate(zip(campos, valores)):
        tk.Label(ventana_editar, text=campo).grid(row=i, column=0, padx=5, pady=5)
        entry = tk.Entry(ventana_editar)
        entry.insert(0, valor)
        entry.grid(row=i, column=1, padx=5, pady=5)
        entradas.append(entry)

    entry_nombre, entry_apellido, entry_fecha_nac, entry_sexo, entry_mail, entry_contraseña = entradas

    tk.Button(ventana_editar, text="Guardar", command=guardar_cambios).grid(row=len(campos), column=1, pady=10)

# Función para agregar un nuevo usuario
def agregar_usuario():
    """Agrega un nuevo usuario a la lista y actualiza la tabla."""
    try:
        id_user = entry_id_user.get()
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        fecha_nac = entry_fecha_nac.get()
        sexo = entry_sexo.get()
        mail = entry_mail.get()
        contraseña = entry_contraseña.get()
        
        if not all([id_user, nombre, apellido, fecha_nac, sexo, mail, contraseña]):
            raise ValueError("Todos los campos son obligatorios.")
        
        Usuario.agregar_usuario(id_user, nombre, apellido, fecha_nac, sexo, mail, contraseña)
        mostrar_tabla()
        limpiar_campos()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def limpiar_campos():
    """Limpia los campos de entrada después de agregar un usuario."""
    entry_id_user.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_fecha_nac.delete(0, tk.END)
    entry_sexo.delete(0, tk.END)
    entry_mail.delete(0, tk.END)
    entry_contraseña.delete(0, tk.END)

# Interfaz gráfica
root = tk.Tk()
root.title("Gestión de Usuarios")

# Entrada de datos para agregar usuarios
campos = ["ID Usuario", "Nombre", "Apellido", "Fecha Nacimiento", "Sexo", "Mail", "Contraseña"]
entradas = []

for i, campo in enumerate(campos):
    tk.Label(root, text=campo).grid(row=i, column=0, padx=5, pady=5)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entradas.append(entry)

entry_id_user, entry_nombre, entry_apellido, entry_fecha_nac, entry_sexo, entry_mail, entry_contraseña = entradas

tk.Button(root, text="Agregar Usuario", command=agregar_usuario).grid(row=len(campos), column=1, pady=10)

# Frame para la tabla
frame_tabla = tk.Frame(root)
frame_tabla.grid(row=len(campos) + 1, column=0, columnspan=2, pady=10)

# Mostrar la tabla de usuarios
mostrar_tabla()

root.mainloop()
