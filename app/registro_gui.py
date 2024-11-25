import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
from db.conexion import Conexion
from db.tables.usuario import Usuario
from db.tables.datosSalud import DatosSalud


class Registro:
    @staticmethod
    def abrir_registro():
        # Crear ventana de registro
        root = tk.Tk()
        root.title("Registro")
        root.geometry("360x640")
        root.config(bg="black")  
        
        # Ingresar la fecha de nacimiento
        tk.Label(root, text="Fecha de nacimiento (YYYY-MM-DD):", fg="white", bg="black").pack(pady=10)
        fecha_nac_entry = tk.Entry(root)
        fecha_nac_entry.pack(pady=10)

        def verificar_edad():
            # Obtener la fecha de nacimiento
            fecha_nac = fecha_nac_entry.get()
            try:
                # Validar la fecha de nacimiento (Que sea mayor a 16 años)
                fecha_nac = datetime.strptime(fecha_nac, "%Y-%m-%d")
                edad = Registro.calcular_edad(fecha_nac)
                if edad < 16:
                    messagebox.showerror("Edad no válida", "No puedes registrarte en la app si eres menor de 16 años.")
                else:
                    # Preguntar datos del usuario
                    Registro.preguntar_datos_usuario(root, fecha_nac)
            except ValueError:
                messagebox.showerror("Fecha inválida", "Por favor, ingresa una fecha válida en formato YYYY-MM-DD.")

        # Botón para verificar la edad
        btn_verificar = ttk.Button(root, text="Verificar Edad", command=verificar_edad)
        btn_verificar.pack(pady=20)

        root.mainloop()

    @staticmethod
    def calcular_edad(fecha_nac):
        # Calcular la edad segun la fecha de nacimiento
        hoy = datetime.today()
        edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
        return edad

    @staticmethod
    def preguntar_datos_usuario(root, fecha_nac):
        for widget in root.winfo_children():
            widget.destroy()

        # Preguntar los datos del usuario
        tk.Label(root, text="Nombre:", fg="white", bg="black").pack(pady=10)
        nombre_entry = tk.Entry(root)
        nombre_entry.pack(pady=10)

        tk.Label(root, text="Apellido:", fg="white", bg="black").pack(pady=10)
        apellido_entry = tk.Entry(root)
        apellido_entry.pack(pady=10)

        tk.Label(root, text="Sexo:", fg="white", bg="black").pack(pady=10)
        sexo_entry = ttk.Combobox(root, values=["M", "F"])
        sexo_entry.pack(pady=10)

        tk.Label(root, text="Correo Electrónico:", fg="white", bg="black").pack(pady=10)
        mail_entry = tk.Entry(root)
        mail_entry.pack(pady=10)

        tk.Label(root, text="Contraseña:", fg="white", bg="black").pack(pady=10)
        password_entry = tk.Entry(root, show="*")
        password_entry.pack(pady=10)

        def guardar_usuario():
            # Recuperar los datos del usuario
            nombre = nombre_entry.get()
            apellido = apellido_entry.get()
            sexo = sexo_entry.get()
            mail = mail_entry.get()
            password = password_entry.get()

            # Revisar que los campos no estén vacíos
            if not nombre or not apellido or not sexo or not mail or not password:
                messagebox.showerror("Campos Vacíos", "Por favor, completa todos los campos.")
                return
            
             # Revisar que el sexo sea una opción válida
            if sexo not in ["M", "F"]:
                messagebox.showerror("Error", "Por favor, selecciona un sexo válido ('M' o 'F').")
                return

            # Crear un Usuario
            usuario = Usuario(
            None,  # id_user None 
            nombre=nombre,
            apellido=apellido,
            fecha_nac=fecha_nac.strftime("%Y-%m-%d"),  # Para que se tome la fecha correctamente
            sexo=sexo,
            mail=mail,
            contraseña=password
        )


            # Insertar el usuario en la db
            try:
                conexion = Conexion("db/database.db")
                id_user = conexion.insertar_usuario(usuario)  
                conexion.cerrar_conexion()

                # Mensaje de éxito
                messagebox.showinfo("Registro Exitoso", "¡Registro exitoso! Ahora puedes llenar tus datos de salud.")
                root.quit()  # Cerrar la ventana actual
                Registro.abrir_datos_salud(id_user)  # Abrir la ventana de "datos_salud"
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error al registrar al usuario: {str(e)}")

        # Botón para guardar los datos del usuario
        btn_guardar = ttk.Button(root, text="Guardar", command=guardar_usuario)
        btn_guardar.pack(pady=20)


    @staticmethod
    def abrir_datos_salud(id_user):
        # Crear ventana para ingresar los datos de salud
        root = tk.Tk()
        root.title("Datos de Salud")
        root.geometry("400x400")
        root.config(bg="black")  

        # Ingresar los datos de salud
        tk.Label(root, text="Altura (cm):", fg="white", bg="black").pack(pady=10)
        altura_entry = tk.Entry(root)
        altura_entry.pack(pady=10)

        tk.Label(root, text="Peso (kg):", fg="white", bg="black").pack(pady=10)
        peso_entry = tk.Entry(root)
        peso_entry.pack(pady=10)

        tk.Label(root, text="Presión Arterial (sistólica/diastólica):", fg="white", bg="black").pack(pady=10)
        presion_entry = tk.Entry(root)
        presion_entry.pack(pady=10)

        def guardar_datos_salud():
            
            # Obtener los datos de salud
            altura = altura_entry.get()
            peso = peso_entry.get()
            presion = presion_entry.get()

            if not altura or not peso or not presion:
                messagebox.showerror("Campos Vacíos", "Por favor, completa todos los campos.")
                return

            # Crear objeto DatosSalud
            datos_salud = DatosSalud(
                id_user=id_user,
                altura=float(altura),  # Convertir a float 
                peso=float(peso),  
                presion=presion
            )

            # Guardar los datos en la dv
            try:
                conexion = Conexion("db/database.db")
                datos_salud.insertar_datosSalud(conexion.cursor)
                
                # Cerrar la conexión
                conexion.cerrar_conexion()

                messagebox.showinfo("Datos Guardados", "¡Tus datos de salud han sido guardados exitosamente!")
                root.quit()
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error al guardar los datos de salud: {str(e)}")




        # Botón para guardar los datos de salud
        btn_guardar_salud = ttk.Button(root, text="Guardar Datos de Salud", command=guardar_datos_salud)
        btn_guardar_salud.pack(pady=20)

        root.mainloop()
