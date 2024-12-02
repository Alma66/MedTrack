import unittest
import sqlite3
from db.conexion import Conexion
from db.tables.relacionales.enf_datos import EnfDatos

class TestEnfDatos(unittest.TestCase):

    def setUp(self):
        """Configura una base de datos en memoria para pruebas."""
        self.conexion = Conexion(":memory:")
        self.cursor = self.conexion.cursor

        # Crear tablas necesarias
        self.cursor.execute("""
        CREATE TABLE datosSalud (
            id_salud INTEGER PRIMARY KEY AUTOINCREMENT
        );
        """)
        self.cursor.execute("""
        CREATE TABLE enfermedad (
            id_enfermedad INTEGER PRIMARY KEY AUTOINCREMENT
        );
        """)
        EnfDatos.crear_tabla(self.cursor)

        # Insertar datos relacionados
        self.cursor.execute("INSERT INTO datosSalud DEFAULT VALUES;")  # id_salud = 1
        self.cursor.execute("INSERT INTO enfermedad DEFAULT VALUES;")  # id_enfermedad = 1
        self.conexion.commit()

    def tearDown(self):
        """Cierra la conexión después de cada prueba."""
        self.conexion.cerrar_conexion()

    def test_insertar_enf_datos(self):
        """Prueba la inserción de un registro en enf_datos."""
        enf_datos = EnfDatos(id_salud=1, id_enf=1)
        enf_datos.insertar(self.cursor)
        self.conexion.commit()

        self.cursor.execute("SELECT * FROM enf_datos;")
        registros = self.cursor.fetchall()
        self.assertEqual(len(registros), 1)
        self.assertEqual(registros[0][1], 1)  # id_salud
        self.assertEqual(registros[0][2], 1)  # id_enf

    def test_obtener_por_id(self):
        """Prueba la obtención de un registro por su ID."""
        enf_datos = EnfDatos(id_salud=1, id_enf=1)
        enf_datos.insertar(self.cursor)
        self.conexion.commit()

        registro = EnfDatos.obtener_por_id(self.cursor, 1)
        self.assertIsNotNone(registro)
        self.assertEqual(registro[1], 1)  # id_salud
        self.assertEqual(registro[2], 1)  # id_enf

    def test_obtener_todos(self):
        """Prueba la obtención de todos los registros."""
        enf_datos_1 = EnfDatos(id_salud=1, id_enf=1)
        enf_datos_2 = EnfDatos(id_salud=1, id_enf=1)
        enf_datos_1.insertar(self.cursor)
        enf_datos_2.insertar(self.cursor)
        self.conexion.commit()

        registros = EnfDatos.obtener_todos(self.cursor)
        self.assertEqual(len(registros), 2)

    def test_actualizar_enf_datos(self):
        """Prueba la actualización de un registro."""
        enf_datos = EnfDatos(id_salud=1, id_enf=1)
        enf_datos.insertar(self.cursor)
        self.conexion.commit()

        # Actualizar registro
        enf_datos_actualizado = EnfDatos(id_enfdatos=1, id_salud=2, id_enf=1)
        enf_datos_actualizado.actualizar(self.cursor)
        self.conexion.commit()

        registro = EnfDatos.obtener_por_id(self.cursor, 1)
        self.assertEqual(registro[1], 2)  # id_salud actualizado

    def test_eliminar_enf_datos(self):
        """Prueba la eliminación de un registro."""
        enf_datos = EnfDatos(id_salud=1, id_enf=1)
        enf_datos.insertar(self.cursor)
        self.conexion.commit()

        # Eliminar registro
        EnfDatos.eliminar(self.cursor, 1)
        self.conexion.commit()

        registros = EnfDatos.obtener_todos(self.cursor)
        self.assertEqual(len(registros), 0)

if __name__ == "__main__":
    unittest.main()
    