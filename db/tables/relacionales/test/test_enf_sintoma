import unittest
import sqlite3
from db.conexion import Conexion
from db.tables.relacionales.enf_sintoma import EnfSintoma

class TestEnfSintoma(unittest.TestCase):

    def setUp(self):
        """Configura una base de datos en memoria para pruebas."""
        self.conexion = Conexion(":memory:")
        self.cursor = self.conexion.cursor

        # Crear tablas necesarias
        self.cursor.execute("""
        CREATE TABLE sintoma (
            id_sintoma INTEGER PRIMARY KEY AUTOINCREMENT
        );
        """)
        self.cursor.execute("""
        CREATE TABLE enfermedad (
            id_enfermedad INTEGER PRIMARY KEY AUTOINCREMENT
        );
        """)
        EnfSintoma.crear_tabla(self.cursor)

        # Insertar datos relacionados
        self.cursor.execute("INSERT INTO sintoma DEFAULT VALUES;")  # id_sintoma = 1
        self.cursor.execute("INSERT INTO enfermedad DEFAULT VALUES;")  # id_enfermedad = 1
        self.conexion.commit()

    def tearDown(self):
        """Cierra la conexión después de cada prueba."""
        self.conexion.cerrar_conexion()

    def test_insertar_enf_sintoma(self):
        """Prueba la inserción de un registro en enf_sintoma."""
        enf_sintoma = EnfSintoma(id_sintoma=1, id_enf=1)
        enf_sintoma.insertar(self.cursor)
        self.conexion.commit()

        self.cursor.execute("SELECT * FROM enf_sintoma;")
        registros = self.cursor.fetchall()
        self.assertEqual(len(registros), 1)
        self.assertEqual(registros[0][1], 1)  # id_sintoma
        self.assertEqual(registros[0][2], 1)  # id_enf

    def test_obtener_por_id(self):
        """Prueba la obtención de un registro por su ID."""
        enf_sintoma = EnfSintoma(id_sintoma=1, id_enf=1)
        enf_sintoma.insertar(self.cursor)
        self.conexion.commit()

        registro = EnfSintoma.obtener_por_id(self.cursor, 1)
        self.assertIsNotNone(registro)
        self.assertEqual(registro[1], 1)  # id_sintoma
        self.assertEqual(registro[2], 1)  # id_enf

    def test_obtener_todos(self):
        """Prueba la obtención de todos los registros."""
        enf_sintoma_1 = EnfSintoma(id_sintoma=1, id_enf=1)
        enf_sintoma_2 = EnfSintoma(id_sintoma=1, id_enf=1)
        enf_sintoma_1.insertar(self.cursor)
        enf_sintoma_2.insertar(self.cursor)
        self.conexion.commit()

        registros = EnfSintoma.obtener_todos(self.cursor)
        self.assertEqual(len(registros), 2)

    def test_actualizar_enf_sintoma(self):
        """Prueba la actualización de un registro."""
        enf_sintoma = EnfSintoma(id_sintoma=1, id_enf=1)
        enf_sintoma.insertar(self.cursor)
        self.conexion.commit()

        # Actualizar registro
        enf_sintoma_actualizado = EnfSintoma(id_enfsintoma=1, id_sintoma=2, id_enf=1)
        enf_sintoma_actualizado.actualizar(self.cursor)
        self.conexion.commit()

        registro = EnfSintoma.obtener_por_id(self.cursor, 1)
        self.assertEqual(registro[1], 2)  # id_sintoma actualizado

    def test_eliminar_enf_sintoma(self):
        """Prueba la eliminación de un registro."""
        enf_sintoma = EnfSintoma(id_sintoma=1, id_enf=1)
        enf_sintoma.insertar(self.cursor)
        self.conexion.commit()

        # Eliminar registro
        EnfSintoma.eliminar(self.cursor, 1)
        self.conexion.commit()

        registros = EnfSintoma.obtener_todos(self.cursor)
        self.assertEqual(len(registros), 0)

if __name__ == "__main__":
    unittest.main()
