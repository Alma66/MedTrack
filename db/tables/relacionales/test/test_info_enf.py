import unittest
import sqlite3
from db.conexion import Conexion
from db.tables.relacionales.info_enf import InfoEnf

class TestInfoEnf(unittest.TestCase):

    def setUp(self):
        """Configura una base de datos en memoria para pruebas."""
        self.conexion = Conexion(":memory:")
        self.cursor = self.conexion.cursor

        # Crear tablas necesarias
        self.cursor.execute("""
        CREATE TABLE enfermedad (
            id_enfermedad INTEGER PRIMARY KEY AUTOINCREMENT
        );
        """)
        self.cursor.execute("""
        CREATE TABLE infoEdu (
            id_info INTEGER PRIMARY KEY AUTOINCREMENT
        );
        """)
        InfoEnf.crear_tabla(self.cursor)

        # Insertar datos relacionados
        self.cursor.execute("INSERT INTO enfermedad DEFAULT VALUES;")  # id_enfermedad = 1
        self.cursor.execute("INSERT INTO infoEdu DEFAULT VALUES;")  # id_info = 1
        self.conexion.commit()

    def tearDown(self):
        """Cierra la conexión después de cada prueba."""
        self.conexion.cerrar_conexion()

    def test_insertar_info_enf(self):
        """Prueba la inserción de un registro en info_enf."""
        info_enf = InfoEnf(id_enf=1, id_info=1)
        info_enf.insertar(self.cursor)
        self.conexion.commit()

        self.cursor.execute("SELECT * FROM info_enf;")
        registros = self.cursor.fetchall()
        self.assertEqual(len(registros), 1)
        self.assertEqual(registros[0][1], 1)  # id_enf
        self.assertEqual(registros[0][2], 1)  # id_info

    def test_obtener_por_id(self):
        """Prueba la obtención de un registro por su ID."""
        info_enf = InfoEnf(id_enf=1, id_info=1)
        info_enf.insertar(self.cursor)
        self.conexion.commit()

        registro = InfoEnf.obtener_por_id(self.cursor, 1)
        self.assertIsNotNone(registro)
        self.assertEqual(registro[1], 1)  # id_enf
        self.assertEqual(registro[2], 1)  # id_info

    def test_obtener_todos(self):
        """Prueba la obtención de todos los registros."""
        info_enf_1 = InfoEnf(id_enf=1, id_info=1)
        info_enf_2 = InfoEnf(id_enf=1, id_info=1)
        info_enf_1.insertar(self.cursor)
        info_enf_2.insertar(self.cursor)
        self.conexion.commit()

        registros = InfoEnf.obtener_todos(self.cursor)
        self.assertEqual(len(registros), 2)

    def test_actualizar_info_enf(self):
        """Prueba la actualización de un registro."""
        info_enf = InfoEnf(id_enf=1, id_info=1)
        info_enf.insertar(self.cursor)
        self.conexion.commit()

        # Actualizar registro
        info_enf_actualizado = InfoEnf(id_infoenf=1, id_enf=1, id_info=2)
        info_enf_actualizado.actualizar(self.cursor)
        self.conexion.commit()

        registro = InfoEnf.obtener_por_id(self.cursor, 1)
        self.assertEqual(registro[2], 2)  # id_info actualizado

    def test_eliminar_info_enf(self):
        """Prueba la eliminación de un registro."""
        info_enf = InfoEnf(id_enf=1, id_info=1)
        info_enf.insertar(self.cursor)
        self.conexion.commit()

        # Eliminar registro
        InfoEnf.eliminar(self.cursor, 1)
        self.conexion.commit()

        registros = InfoEnf.obtener_todos(self.cursor)
        self.assertEqual(len(registros), 0)

if __name__ == "__main__":
    unittest.main()