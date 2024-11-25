import unittest
import sqlite3
from db.conexion import Conexion
from db.tables.relacionales.user_enf import UserEnf

class TestUserEnf(unittest.TestCase):

    def setUp(self):
        """Configura una base de datos en memoria para pruebas."""
        self.conexion = Conexion(":memory:")
        self.cursor = self.conexion.cursor

        # Crear tablas necesarias
        self.cursor.execute("""
        CREATE TABLE usuarios (
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT
        );
        """)
        self.cursor.execute("""
        CREATE TABLE enfermedad (
            id_enfermedad INTEGER PRIMARY KEY AUTOINCREMENT
        );
        """)
        UserEnf.crear_tabla(self.cursor)

        # Insertar datos relacionados
        self.cursor.execute("INSERT INTO usuarios DEFAULT VALUES;")  # id_user = 1
        self.cursor.execute("INSERT INTO enfermedad DEFAULT VALUES;")  # id_enf = 1
        self.conexion.commit()

    def tearDown(self):
        """Cierra la conexión después de cada prueba."""
        self.conexion.cerrar_conexion()

    def test_insertar_user_enf(self):
        """Prueba la inserción de un registro en user_enf."""
        user_enf = UserEnf(id_user=1, id_enf=1)
        user_enf.insertar(self.cursor)
        self.conexion.commit()

        self.cursor.execute("SELECT * FROM user_enf;")
        registros = self.cursor.fetchall()
        self.assertEqual(len(registros), 1)
        self.assertEqual(registros[0][1], 1)  # id_user
        self.assertEqual(registros[0][2], 1)  # id_enf

    def test_obtener_por_id(self):
        """Prueba la obtención de un registro por su ID."""
        user_enf = UserEnf(id_user=1, id_enf=1)
        user_enf.insertar(self.cursor)
        self.conexion.commit()

        registro = UserEnf.obtener_por_id(self.cursor, 1)
        self.assertIsNotNone(registro)
        self.assertEqual(registro[1], 1)  # id_user
        self.assertEqual(registro[2], 1)  # id_enf

    def test_obtener_todos(self):
        """Prueba la obtención de todos los registros."""
        user_enf_1 = UserEnf(id_user=1, id_enf=1)
        user_enf_2 = UserEnf(id_user=1, id_enf=1)
        user_enf_1.insertar(self.cursor)
        user_enf_2.insertar(self.cursor)
        self.conexion.commit()

        registros = UserEnf.obtener_todos(self.cursor)
        self.assertEqual(len(registros), 2)

    def test_actualizar_user_enf(self):
        """Prueba la actualización de un registro."""
        user_enf = UserEnf(id_user=1, id_enf=1)
        user_enf.insertar(self.cursor)
        self.conexion.commit()

        # Actualizar registro
        user_enf_actualizado = UserEnf(id_userenf=1, id_user=2, id_enf=1)
        user_enf_actualizado.actualizar(self.cursor)
        self.conexion.commit()

        registro = UserEnf.obtener_por_id(self.cursor, 1)
        self.assertEqual(registro[1], 2)  # id_user actualizado

    def test_eliminar_user_enf(self):
        """Prueba la eliminación de un registro."""
        user_enf = UserEnf(id_user=1, id_enf=1)
        user_enf.insertar(self.cursor)
        self.conexion.commit()

        # Eliminar registro
        UserEnf.eliminar(self.cursor, 1)
        self.conexion.commit()

        registros = UserEnf.obtener_todos(self.cursor)
        self.assertEqual(len(registros), 0)

if __name__ == "__main__":
    unittest.main()
