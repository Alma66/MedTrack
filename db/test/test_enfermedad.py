import unittest
from db.conexion import Conexion
from db.tables.enfermedad import Enfermedad

class TestEnfermedad(unittest.TestCase):

    def setUp(self):
        # Usamos la db de memoria para las pruebas
        self.db = Conexion(":memory:")  # Db en memoria
        self.db.crear_tablas()  # Creamos todas las tablas necesarias

    def tearDown(self):
        # Cerrar la conexión después de cada prueba
        self.db.cerrar_conexion()

    def test_insertar_enfermedad_correcto(self):
        # Creamos una enfermedad "falsa" para la prueba
        enfermedad = Enfermedad(self.db.cursor, id_enf=1, nombre="Gripe", descripcion="Infección respiratoria viral")
        enfermedad.insertar_enfermedad()

        # Verificamos que la enfermedad fue insertada correctamente
        self.db.cursor.execute("SELECT * FROM enfermedad WHERE id_enf=1")
        resultado = self.db.cursor.fetchone()
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado[1], "Gripe")
        self.assertEqual(resultado[2], "Infección respiratoria viral")

    def test_editar_enfermedad(self):
        # Insertamos una enfermedad "falsa" para editarla después
        enfermedad = Enfermedad(self.db.cursor, id_enf=2, nombre="Resfriado", descripcion="Infección viral leve")
        enfermedad.insertar_enfermedad()

        # Editamos la enfermedad
        enfermedad.nombre = "Neumonía"
        enfermedad.descripcion = "Infección pulmonar grave"
        enfermedad.editar_enfermedad()

        # Verificamos que el cambio se haya realizado correctamente
        self.db.cursor.execute("SELECT * FROM enfermedad WHERE id_enf=2")
        resultado = self.db.cursor.fetchone()
        self.assertEqual(resultado[1], "Neumonía")
        self.assertEqual(resultado[2], "Infección pulmonar grave")

    def test_eliminar_enfermedad(self):
        # Insertamos una enfermedad "falsa" para eliminarla
        enfermedad = Enfermedad(self.db.cursor, id_enf=3, nombre="Covid-19", descripcion="Enfermedad respiratoria grave")
        enfermedad.insertar_enfermedad()

        # Eliminamos la enfermedad
        enfermedad.eliminar_enfermedad()

        # Verificamos que la enfermedad fue eliminada
        self.db.cursor.execute("SELECT * FROM enfermedad WHERE id_enf=3")
        resultado = self.db.cursor.fetchone()
        self.assertIsNone(resultado)

    def test_mostrar_enfermedades(self):
        # Insertamos algunas enfermedades "falsas" para verificar que se muestren correctamente
        enfermedad1 = Enfermedad(self.db.cursor, id_enf=4, nombre="Diabetes", descripcion="Trastorno metabólico")
        enfermedad1.insertar_enfermedad()

        enfermedad2 = Enfermedad(self.db.cursor, id_enf=5, nombre="Hipertensión", descripcion="Presión arterial alta")
        enfermedad2.insertar_enfermedad()

        # Obtenemos todas las enfermedades y verificamos que se muestren correctamente
        enfermedades = enfermedad1.mostrar_enfermedades()
        self.assertEqual(len(enfermedades), 2)
        self.assertEqual(enfermedades[0][1], "Diabetes")
        self.assertEqual(enfermedades[1][1], "Hipertensión")

if __name__ == "__main__":
    unittest.main()
