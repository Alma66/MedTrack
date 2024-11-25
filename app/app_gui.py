import sys
import os
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import PhotoImage
from gui_helpers import abrir_registro, abrir_inicio_sesion

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Bienvenido a MedTrack")
        # Tamaño de la ventana como celular estándar
        self.root.geometry("360x640")
        
        # Ruta de la fuente eterna
        self.font_path = "fonts/JunigardenSwash_PERSONAL_USE_ONLY.otf"
        
        # Registrar la fuente 
        self.registrar_fuente()

        # Fondo negro
        self.root.config(bg="black")
        
        # Agregar el icono
        self.icono = PhotoImage(file="app/images/logoMedtrack.png")  
        self.root.iconphoto(True, self.icono)
        
        # Crear la página de inicio
        self.crear_pagina_inicio()

    def registrar_fuente(self):
        """Registra la fuente personalizada en Tkinter."""
        # Se usa "tk.call" para registrar la fuente en Tkinter
        self.root.tk.call("font", "create", "Junigarden", "-family", "JunigardenSwash_PERSONAL_USE_ONLY", "-size", 14)
        
    def crear_pagina_inicio(self):
        # Se "limpia" ventana
        for widget in self.root.winfo_children():
            widget.destroy()

        titulo = tk.Label(self.root, text="¡Bienvenido a MedTrack!", font=("Junigarden", 16, "bold"), fg="white", bg="black")
        titulo.pack(pady=30)

        # Logo 
        logo = PhotoImage(file="app/images/logoMedtrack.png")  
        logo_label = tk.Label(self.root, image=logo, bg="black")
        logo_label.image = logo 
        logo_label.pack(pady=20)

        # Con "tk.frame" ponemos los botones uno al lado del otro
        frame_botones = tk.Frame(self.root, bg="black")
        frame_botones.pack(pady=20)

        # Botón para iniciar sesión
        btn_inicio_sesion = ttk.Button(frame_botones, text="Iniciar sesión", command=abrir_inicio_sesion)
        btn_inicio_sesion.grid(row=0, column=0, padx=10)

        # Botón para registrarse
        btn_registro = ttk.Button(frame_botones, text="Registrarse", command=abrir_registro)
        btn_registro.grid(row=0, column=1, padx=10)

if __name__ == "__main__":
    root = tk.Tk()  # Crear la ventana principal
    app = App(root)  
    root.mainloop()  # Ejecutar el bucle principal de Tkinter
