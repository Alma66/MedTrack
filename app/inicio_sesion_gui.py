import sys
import os
import subprocess 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import ttk, messagebox
from db.conexion import Conexion
from db.tables.datosSalud import DatosSalud

class InicioSesion:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de Sesión")
        self.root.geometry("360x640")  
        self.root.configure(bg="black")

        # Título
        titulo = tk.Label(self.root, text="Iniciar Sesión", font=("Arial", 14, "bold"), fg="white", bg="black")
        titulo.pack(pady=10)

        # Formulario
        lbl_email = tk.Label(self.root, text="Email:", fg="white", bg="black")
        lbl_email.pack(pady=5)
        self.entry_email = ttk.Entry(self.root)
        self.entry_email.pack(pady=5)

        lbl_password = tk.Label(self.root, text="Contraseña:", fg="white", bg="black")
        lbl_password.pack(pady=5)
        self.entry_password = ttk.Entry(self.root, show="*")
        self.entry_password.pack(pady=5)

        # Botón para iniciar sesión
        btn_iniciar = ttk.Button(self.root, text="Iniciar Sesión", command=self.iniciar_sesion)
        btn_iniciar.pack(pady=20)

        btn_iniciar.configure(style="TButton")

    def iniciar_sesion(self):
        email = self.entry_email.get()
        password = self.entry_password.get()
        print(f"Inicio de sesión: {email}")
        
        self.root.withdraw()  # Ocultar la ventana principal
        
        # Llamar a la ventana de opciones
        self.mostrar_opciones()

    def mostrar_opciones(self):
        # Ventana mostrar las opciones
        ventana_opciones = tk.Toplevel(self.root)
        ventana_opciones.title("Opciones de Salud")
        ventana_opciones.geometry("360x640") 
        ventana_opciones.configure(bg="black")

        # Crear las opciones
        tk.Label(ventana_opciones, text="Seleccione una opción", font=("Arial", 12, "bold"), fg="white", bg="black").pack(pady=10)

        # Opción 1: Registrar presión
        btn_presion = ttk.Button(ventana_opciones, text="Registrar presión actual", command=self.registrar_presion)
        btn_presion.pack(pady=10)

        # Opción 2: Registrar peso
        btn_peso = ttk.Button(ventana_opciones, text="Registrar peso actual", command=self.registrar_peso)
        btn_peso.pack(pady=10)

        # Opción 3: Ninguna
        btn_ninguna = ttk.Button(ventana_opciones, text="Ninguna", command=self.salir)
        btn_ninguna.pack(pady=10)

    def registrar_presion(self):
        # Ventana para registrar presión
        ventana_presion = tk.Toplevel(self.root)
        ventana_presion.title("Registrar Presión")
        ventana_presion.geometry("300x200")
        ventana_presion.configure(bg="black")

        # Registrar la presión
        tk.Label(ventana_presion, text="Presión Arterial:", font=("Arial", 10), fg="white", bg="black").pack(pady=10)
        presion_entry = ttk.Entry(ventana_presion)
        presion_entry.pack(pady=10)

        # Botón para guardar la presión
        def guardar_presion():
            presion = presion_entry.get()
            if not presion:
                messagebox.showerror("Error", "Por favor ingrese la presión.")
                return

            # Ver que ID de usuario este disponible y es correcto
            id_user = 1  

            # Actualizar datos de salud en la db
            try:
                conexion = Conexion("db/database.db")
                cursor = conexion.cursor
                datos_salud = DatosSalud(id_user=id_user, presion=presion)
                datos_salud.editar_datosSalud(cursor)
                conexion.cerrar_conexion()

                messagebox.showinfo("Éxito", "Presión registrada correctamente.")
                ventana_presion.destroy()

                # Mostrar siguiente opción
                self.mostrar_opciones()
            except Exception as e:
                messagebox.showerror("Error", f"Error al registrar la presión: {e}")

        # Botón para guardar
        ttk.Button(ventana_presion, text="Guardar", command=guardar_presion).pack(pady=10)

    def registrar_peso(self):
        # Crear ventana para registrar peso
        ventana_peso = tk.Toplevel(self.root)
        ventana_peso.title("Registrar Peso")
        ventana_peso.geometry("300x200")
        ventana_peso.configure(bg="black")

        # Registrar el peso
        tk.Label(ventana_peso, text="Peso Actual:", font=("Arial", 10), fg="white", bg="black").pack(pady=10)
        peso_entry = ttk.Entry(ventana_peso)
        peso_entry.pack(pady=10)

        # Botón para guardar el peso
        def guardar_peso():
            peso = peso_entry.get()
            if not peso:
                messagebox.showerror("Error", "Por favor ingrese el peso.")
                return
            
            id_user = 1  

            # Actualizar datos de salud en la db
            try:
                conexion = Conexion("db/database.db")
                cursor = conexion.cursor
                datos_salud = DatosSalud(id_user=id_user, peso=peso)
                datos_salud.editar_datosSalud(cursor)
                conexion.cerrar_conexion()

                messagebox.showinfo("Éxito", "Peso registrado correctamente.")
                ventana_peso.destroy()

                # Mostrar siguiente opción
                self.mostrar_opciones()
            except Exception as e:
                messagebox.showerror("Error", f"Error al registrar el peso: {e}")

        # Botón para guardar
        ttk.Button(ventana_peso, text="Guardar", command=guardar_peso).pack(pady=10)

    def salir(self):
        # Cerrar la ventana de opciones y e ir a inicio_gui.py
        self.root.quit()
        self.root.destroy()  # Cierra la ventana actual
        subprocess.run(["python", "app/inicio_gui.py"]) 

