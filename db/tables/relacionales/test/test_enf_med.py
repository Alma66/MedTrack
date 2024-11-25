import unittest
import sqlite3
from db.conexion import Conexion
from db.tables.relacionales.med_enf import EnfMed

class TestMedEnf(unittest.TestCase):

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
        CREATE TABLE enfermedad (
            id_enfermedad INTEGER PRIMARY KEY AUTOINCREMENT
        );
        """)
        EnfMed.crear_tabla(self.cursor)

        # Insertar datos relacionados
        self.cursor.execute("INSERT INTO medicamentos DEFAULT VALUES;")  # id_medicamento = 1
        self.cursor.execute("INSERT INTO enfermedad DEFAULT VALUES;")  # id_enfermedad = 1
        self.conexion.commit()

    def tearDown(self):
        """Cierra la conexión después de cada prueba."""
        self.conexion.cerrar_conexion()

    def test_insertar_enf_med(self):
        """Prueba la inserción de un registro en enf_med."""
        enf_med = EnfMed(id_med=1, id_enf=1)
        enf_med.insertar(self.cursor)
        self.conexion.commit()

        self.cursor.execute("SELECT * FROM enf_med;")
        registros = self.cursor.fetchall()
        self.assertEqual(len(registros), 1)
        self.assertEqual(registros[0][1], 1)  # id_med
        self.assertEqual(registros[0][2], 1)  # id_enf

    def test_obtener_por_id(self):
        """Prueba la obtención de un registro por su ID."""
        enf_med = EnfMed(id_med=1, id_enf=1)
        enf_med.insertar(self.cursor)
        self.conexion.commit()

        registro = EnfMed.obtener_por_id(self.cursor, 1)
        self.assertIsNotNone(registro)
        self.assertEqual(registro[1], 1)  # id_med
        self.assertEqual(registro[2], 1)  # id_enf

    def test_obtener_todos(self):
        """Prueba la obtención de todos los registros."""
        enf_med_1 = EnfMed(id_med=1, id_enf=1)
        enf_med_2 = EnfMed(id_med=1, id_enf=1)
        enf_med_1.insertar(self.cursor)
        enf_med_2.insertar(self.cursor)
        self.conexion.commit()

        registros = EnfMed.obtener_todos(self.cursor)
        self.assertEqual(len(registros), 2)

    def test_actualizar_enf_med(self):
        """Prueba la actualización de un registro."""
        enf_med = EnfMed(id_med=1, id_enf=1)
        enf_med.insertar(self.cursor)
        self.conexion.commit()

        # Actualizar registro
        enf_med_actualizado = EnfMed(id_enfmed=1, id_med=2, id_enf=1)
        enf_med_actualizado.actualizar(self.cursor)
        self.conexion.commit()

        registro = EnfMed.obtener_por_id(self.cursor, 1)
        self.assertEqual(registro[1], 2)  # id_med actualizado

    def test_eliminar_enf_med(self):
        """Prueba la eliminación de un registro."""
        enf_med = EnfMed(id_med=1, id_enf=1)
        enf_med.insertar(self.cursor)
        self.conexion.commit()

        # Eliminar registro
        EnfMed.eliminar(self.cursor, 1)
        self.conexion.commit()

        registros = EnfMed.obtener_todos(self.cursor)
        self.assertEqual(len(registros), 0)

if __name__ == "__main__":
    unittest.main()
