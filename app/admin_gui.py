import sys
import os
import tkinter as tk
from tkinter import messagebox
import subprocess

# Agregar la carpeta raíz al path para importar correctamente módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db.conexion import Conexion

class AdminGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Panel de Administración")
        self.master.geometry("400x300")
        
        # Inicializa la conexión a la base de datos
        try:
            self.conexion = Conexion("medtrack.db")
            self.cursor = self.conexion.cursor
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo establecer conexión con la base de datos.\n{e}")
            self.master.destroy()
            return
        
        self.create_table_list()

    # Diccionario para mapear nombres de tablas con sus módulos correspondientes
    TABLE_MODULES = {
        "Usuarios": "db.tables.usuario",
        "Medicamentos": "db.tables.medicamento",
        "Enfermedades": "db.tables.enfermedad",
        "Sintomas": "db.tables.sintoma",
        "InfoEducacional": "db.tables.infoedu",
        "Datos de Salud": "db.tables.datosSalud",
        "User_Med": "db.tables.relacionales.user_med",
        "User_Enf": "db.tables.relacionales.user_enf",
        "Enf_Med": "db.tables.relacionales.med_enf",
        "Enf_Sintoma": "db.tables.relacionales.enf_sintoma",
        "Enf_Datos": "db.tables.relacionales.enf_datos",
        "Info_Med": "db.tables.relacionales.info_med",
        "Info_Datos": "db.tables.relacionales.info_datos",
        "Info_Enf": "db.tables.relacionales.info_enf",
    }

    # Diccionario para mapear las tablas con las vistas GUI
    TABLE_VIEWS = {
        "Usuarios": "app/tables/table_usuario_gui.py",
        "Medicamentos": "tables/medicamentos_gui.py",
        "Enfermedades": "tables/enfermedad_gui.py",
        "Sintomas": "app/tables/sintoma_gui.py",
        "InfoEducacional": "app/tables/infoedu_gui.py",
        "Datos de Salud": "app/tables/datosSalud_gui.py",
        "User_Med": "app/tables/relacionales/user_med_gui.py",
        "User_Enf": "app/tables/relacionales/user_enf_gui.py",
        "Enf_Med": "app/tables/relacionales/med_enf_gui.py",
        "Enf_Sintoma": "app/tables/relacionales/enf_sintoma_gui.py",
        "Enf_Datos": "app/tables/relacionales/enf_datos_gui.py",
        "Info_Med": "app/tables/relacionales/info_med_gui.py",
        "Info_Datos": "app/tables/relacionales/info_datos_gui.py",
        "Info_Enf": "app/tables/relacionales/info_enf_gui.py",
    }

    def create_table_list(self):
        """Crea la lista de tablas en la GUI con la opción de hacer clic en ellas."""
        tablas = list(self.TABLE_MODULES.keys())
        
        tabla_label = tk.Label(self.master, text="Selecciona una tabla para gestionar:")
        tabla_label.pack(pady=10)
        
        self.lista_tablas = tk.Listbox(self.master, height=10)
        for tabla in tablas:
            self.lista_tablas.insert(tk.END, tabla)
        
        self.lista_tablas.pack(pady=10)
        
        # Botón para gestionar la tabla seleccionada
        gestionar_button = tk.Button(self.master, text="Gestionar Tabla", command=self.gestionar_tabla)
        gestionar_button.pack(pady=10)

    def gestionar_tabla(self):
        """Gestiona la tabla seleccionada y ejecuta la vista correspondiente."""
        seleccion = self.lista_tablas.curselection()
        
        if seleccion:
            tabla_seleccionada = self.lista_tablas.get(seleccion)
            vista = self.TABLE_VIEWS.get(tabla_seleccionada)
            
            if vista:
                ruta_vista = os.path.abspath(vista)
                
                if os.path.exists(ruta_vista):
                    try:
                        subprocess.run(["python", ruta_vista])
                    except Exception as e:
                        messagebox.showerror("Error", f"No se pudo ejecutar la vista para '{tabla_seleccionada}'.\n{e}")
                else:
                    messagebox.showerror("Error", f"No se encontró el archivo: {ruta_vista}")
            else:
                messagebox.showinfo("Info", f"No hay vista definida para la tabla: {tabla_seleccionada}")
        else:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tabla.")

def main():
    root = tk.Tk()
    app = AdminGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
