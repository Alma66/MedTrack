import unittest
import sqlite3
from db.conexion import Conexion
from db.tables.relacionales.user_med import UserMed

class TestUserMed(unittest.TestCase):

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
        CREATE TABLE medicamentos (
            id_medicamento INTEGER PRIMARY KEY AUTOINCREMENT
        );
        """)
        UserMed.crear_tabla(self.cursor)

        # Insertar datos relacionados
        self.cursor.execute("INSERT INTO usuarios DEFAULT VALUES;")  # id_user = 1
        self.cursor.execute("INSERT INTO medicamentos DEFAULT VALUES;")  # id_med = 1
        self.conexion.commit()

    def tearDown(self):
        """Cierra la conexión después de cada prueba."""
        self.conexion.cerrar_conexion()

    def test_insertar_user_med(self):
        """Prueba la inserción de un registro en user_med."""
        user_med = UserMed(id_user=1, id_med=1)
        user_med.insertar(self.cursor)
        self.conexion.commit()

        self.cursor.execute("SELECT * FROM user_med;")
        registros = self.cursor.fetchall()
        self.assertEqual(len(registros), 1)
        self.assertEqual(registros[0][1], 1)  # id_user
        self.assertEqual(registros[0][2], 1)  # id_med

    def test_obtener_por_id(self):
        """Prueba la obtención de un registro por su ID."""
        user_med = UserMed(id_user=1, id_med=1)
        user_med.insertar(self.cursor)
        self.conexion.commit()

        registro = UserMed.obtener_por_id(self.cursor, 1)
        self.assertIsNotNone(registro)
        self.assertEqual(registro[1], 1)  # id_user
        self.assertEqual(registro[2], 1)  # id_med

    def test_obtener_todos(self):
        """Prueba la obtención de todos los registros."""
        user_med_1 = UserMed(id_user=1, id_med=1)
        user_med_2 = UserMed(id_user=1, id_med=1)
        user_med_1.insertar(self.cursor)
        user_med_2.insertar(self.cursor)
        self.conexion.commit()

        registros = UserMed.obtener_todos(self.cursor)
        self.assertEqual(len(registros), 2)

    def test_actualizar_user_med(self):
        """Prueba la actualización de un registro."""
        user_med = UserMed(id_user=1, id_med=1)
        user_med.insertar(self.cursor)
        self.conexion.commit()

        # Actualizar registro
        user_med_actualizado = UserMed(id_usermed=1, id_user=2, id_med=1)
        user_med_actualizado.actualizar(self.cursor)
        self.conexion.commit()

        registro = UserMed.obtener_por_id(self.cursor, 1)
        self.assertEqual(registro[1], 2)  # id_user actualizado

    def test_eliminar_user_med(self):
        """Prueba la eliminación de un registro."""
        user_med = UserMed(id_user=1, id_med=1)
        user_med.insertar(self.cursor)
        self.conexion.commit()

        # Eliminar registro
        UserMed.eliminar(self.cursor, 1)
        self.conexion.commit()

        registros = UserMed.obtener_todos(self.cursor)
        self.assertEqual(len(registros), 0)

if __name__ == "__main__":
    unittest.main()
