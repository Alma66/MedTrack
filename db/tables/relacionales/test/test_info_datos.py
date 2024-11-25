import unittest
import sqlite3
from db.conexion import Conexion
from db.tables.relacionales.info_datos import InfoDatos

class TestInfoDatos(unittest.TestCase):

    def setUp(self):
        """Configura una base de datos en memoria para pruebas."""
        self.conexion = Conexion(":memory:")  # Base de datos en memoria
        self.cursor = self.conexion.cursor
        
        # Crear tablas necesarias
        self.cursor.execute("""
        CREATE TABLE datosSalud (
            id_datos_salud INTEGER PRIMARY KEY AUTOINCREMENT
        );
        """)
        self.cursor.execute("""
        CREATE TABLE infoEdu (
            id_info INTEGER PRIMARY KEY AUTOINCREMENT
        );
        """)
        InfoDatos.crear_tabla(self.cursor)

        # Insertar datos relacionados
        self.cursor.execute("INSERT INTO datosSalud DEFAULT VALUES;")  # id_datos_salud = 1
        self.cursor.execute("INSERT INTO infoEdu DEFAULT VALUES;")  # id_info = 1
        self.conexion.commit()

    def tearDown(self):
        """Cierra la conexión después de cada prueba."""
        self.conexion.cerrar_conexion()

    def test_insertar_info_datos(self):
        """Prueba la inserción de un registro en info_datos."""
        info_datos = InfoDatos(id_salud=1, id_info=1)
        info_datos.insertar(self.cursor)
        self.conexion.commit()

        self.cursor.execute("SELECT * FROM info_datos;")
        registros = self.cursor.fetchall()
        self.assertEqual(len(registros), 1)
        self.assertEqual(registros[0][1], 1)  # id_salud
        self.assertEqual(registros[0][2], 1)  # id_info

    def test_obtener_por_id(self):
        """Prueba la obtención de un registro por su ID."""
        info_datos = InfoDatos(id_salud=1, id_info=1)
        info_datos.insertar(self.cursor)
        self.conexion.commit()

        registro = InfoDatos.obtener_por_id(self.cursor, 1)
        self.assertIsNotNone(registro)
        self.assertEqual(registro[1], 1)  # id_salud
        self.assertEqual(registro[2], 1)  # id_info

    def test_obtener_todos(self):
        """Prueba la obtención de todos los registros."""
        info_datos_1 = InfoDatos(id_salud=1, id_info=1)
        info_datos_2 = InfoDatos(id_salud=1, id_info=1)
        info_datos_1.insertar(self.cursor)
        info_datos_2.insertar(self.cursor)
        self.conexion.commit()

        registros = InfoDatos.obtener_todos(self.cursor)
        self.assertEqual(len(registros), 2)

    def test_actualizar_info_datos(self):
        """Prueba la actualización de un registro."""
        info_datos = InfoDatos(id_salud=1, id_info=1)
        info_datos.insertar(self.cursor)
        self.conexion.commit()

        # Actualizar registro
        info_datos_actualizado = InfoDatos(id_info_datos=1, id_salud=1, id_info=2)
        info_datos_actualizado.actualizar(self.cursor)
        self.conexion.commit()

        registro = InfoDatos.obtener_por_id(self.cursor, 1)
        self.assertEqual(registro[2], 2)  # id_info actualizado

    def test_eliminar_info_datos(self):
        """Prueba la eliminación de un registro."""
        info_datos = InfoDatos(id_salud=1, id_info=1)
        info_datos.insertar(self.cursor)
        self.conexion.commit()

        # Eliminar registro
        InfoDatos.eliminar(self.cursor, 1)
        self.conexion.commit()

        registros = InfoDatos.obtener_todos(self.cursor)
        self.assertEqual(len(registros), 0)

if __name__ == "__main__":
    unittest.main()
