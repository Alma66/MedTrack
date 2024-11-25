import unittest
import sqlite3
from db.conexion import Conexion
from db.tables.relacionales.info_med import InfoMed

class TestInfoMed(unittest.TestCase):

    def setUp(self):
        """Configura una base de datos en memoria para pruebas."""
        self.conexion = Conexion(":memory:")
        self.cursor = self.conexion.cursor

        # Crear tablas necesarias
        self.cursor.execute("""
        CREATE TABLE medicamentos (
            id_medicamento INTEGER PRIMARY KEY AUTOINCREMENT
        );
        """)
        self.cursor.execute("""
        CREATE TABLE infoEdu (
            id_info INTEGER PRIMARY KEY AUTOINCREMENT
        );
        """)
        InfoMed.crear_tabla(self.cursor)

        # Insertar datos relacionados
        self.cursor.execute("INSERT INTO medicamentos DEFAULT VALUES;")  # id_medicamento = 1
        self.cursor.execute("INSERT INTO infoEdu DEFAULT VALUES;")  # id_info = 1
        self.conexion.commit()

    def tearDown(self):
        """Cierra la conexión después de cada prueba."""
        self.conexion.cerrar_conexion()

    def test_insertar_info_med(self):
        """Prueba la inserción de un registro en info_med."""
        info_med = InfoMed(id_med=1, id_info=1)
        info_med.insertar(self.cursor)
        self.conexion.commit()

        self.cursor.execute("SELECT * FROM info_med;")
        registros = self.cursor.fetchall()
        self.assertEqual(len(registros), 1)
        self.assertEqual(registros[0][1], 1)  # id_med
        self.assertEqual(registros[0][2], 1)  # id_info

    def test_obtener_por_id(self):
        """Prueba la obtención de un registro por su ID."""
        info_med = InfoMed(id_med=1, id_info=1)
        info_med.insertar(self.cursor)
        self.conexion.commit()

        registro = InfoMed.obtener_por_id(self.cursor, 1)
        self.assertIsNotNone(registro)
        self.assertEqual(registro[1], 1)  # id_med
        self.assertEqual(registro[2], 1)  # id_info

    def test_obtener_todos(self):
        """Prueba la obtención de todos los registros."""
        info_med_1 = InfoMed(id_med=1, id_info=1)
        info_med_2 = InfoMed(id_med=1, id_info=1)
        info_med_1.insertar(self.cursor)
        info_med_2.insertar(self.cursor)
        self.conexion.commit()

        registros = InfoMed.obtener_todos(self.cursor)
        self.assertEqual(len(registros), 2)

    def test_actualizar_info_med(self):
        """Prueba la actualización de un registro."""
        info_med = InfoMed(id_med=1, id_info=1)
        info_med.insertar(self.cursor)
        self.conexion.commit()

        # Actualizar registro
        info_med_actualizado = InfoMed(id_infomed=1, id_med=1, id_info=2)
        info_med_actualizado.actualizar(self.cursor)
        self.conexion.commit()

        registro = InfoMed.obtener_por_id(self.cursor, 1)
        self.assertEqual(registro[2], 2)  # id_info actualizado

    def test_eliminar_info_med(self):
        """Prueba la eliminación de un registro."""
        info_med = InfoMed(id_med=1, id_info=1)
        info_med.insertar(self.cursor)
        self.conexion.commit()

        # Eliminar registro
        InfoMed.eliminar(self.cursor, 1)
        self.conexion.commit()

        registros = InfoMed.obtener_todos(self.cursor)
        self.assertEqual(len(registros), 0)

if __name__ == "__main__":
    unittest.main()
