import unittest
from db.conexion import Conexion
from db.tables.sintoma import Sintoma

class TestSintoma(unittest.TestCase):

    def setUp(self):
        # Usamos la db de memoria para las pruebas
        self.db = Conexion(":memory:")  # Db en memoria
        self.db.crear_tablas()  # Creamos todas las tablas necesarias

    def tearDown(self):
        # Cerrar la conexión después de cada prueba
        self.db.cerrar_conexion()

    def test_insertar(self):
        # Creamos un síntoma "falso" para la prueba
        sintoma = Sintoma(self.db.cursor, id_sintoma=1, nombre="Fiebre", descripcion="Aumento de la temperatura corporal")
        sintoma.insertar_sintoma()

        # Verificamos que el síntoma fue insertado correctamente
        self.db.cursor.execute("SELECT * FROM sintoma WHERE id_sintoma=1")
        resultado = self.db.cursor.fetchone()
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado[1], "Fiebre")
        self.assertEqual(resultado[2], "Aumento de la temperatura corporal")

    def test_editar(self):
        # Insertamos un síntoma "falso" para editarlo después
        sintoma = Sintoma(self.db.cursor, id_sintoma=2, nombre="Dolor de cabeza", descripcion="Malestar general en la cabeza")
        sintoma.insertar_sintoma()

        # Editamos el síntoma
        sintoma.nombre = "Migraña"
        sintoma.descripcion = "Dolor intenso en la cabeza"
        sintoma.editar_sintoma()

        # Verificamos que el cambio se haya realizado correctamente
        self.db.cursor.execute("SELECT * FROM sintoma WHERE id_sintoma=2")
        resultado = self.db.cursor.fetchone()
        self.assertEqual(resultado[1], "Migraña")
        self.assertEqual(resultado[2], "Dolor intenso en la cabeza")

    def test_eliminar(self):
        # Insertamos un síntoma "falso" para eliminarlo
        sintoma = Sintoma(self.db.cursor, id_sintoma=3, nombre="Tos", descripcion="Expulsión repentina de aire desde los pulmones")
        sintoma.insertar_sintoma()

        # Eliminamos el síntoma
        sintoma.eliminar_sintoma()

        # Verificamos que el síntoma fue eliminado
        self.db.cursor.execute("SELECT * FROM sintoma WHERE id_sintoma=3")
        resultado = self.db.cursor.fetchone()
        self.assertIsNone(resultado)

    def test_mostrar(self):
        # Insertamos algunos síntomas "falsos" para verificar que se muestren correctamente
        sintoma1 = Sintoma(self.db.cursor, id_sintoma=4, nombre="Fatiga", descripcion="Cansancio extremo")
        sintoma1.insertar_sintoma()

        sintoma2 = Sintoma(self.db.cursor, id_sintoma=5, nombre="Escalofríos", descripcion="Sensación de frío acompañada de temblores")
        sintoma2.insertar_sintoma()

        # Obtenemos todos los síntomas y verificamos que se muestren correctamente
        sintomas = sintoma1.mostrar_sintomas()
        self.assertEqual(len(sintomas), 2)
        self.assertEqual(sintomas[0][1], "Fatiga")
        self.assertEqual(sintomas[1][1], "Escalofríos")

if __name__ == "__main__":
    unittest.main()
