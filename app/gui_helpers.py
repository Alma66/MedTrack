import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import ttk
from db.conexion import Conexion

def abrir_registro():
    from registro_gui import Registro
    Registro.abrir_registro()

def abrir_inicio_sesion():
    from inicio_sesion_gui import InicioSesion
    ventana_inicio = tk.Toplevel()
    app_inicio = InicioSesion(ventana_inicio)

def abrir_inicio():
    from inicio_gui import InicioGUI
    ventana_inicio = tk.Toplevel()
    app_inicio = InicioGUI(ventana_inicio)

def abrir_main():
    from main import main  
    ventana_main = tk.Toplevel()
    main(ventana_main) 
