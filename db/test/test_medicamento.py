import unittest
from db.conexion import Conexion
from db.tables.medicamento import Medicamento

class TestMedicamento(unittest.TestCase):

    def setUp(self):
        # Usamos la db de memoria para las pruebas
        self.db = Conexion(":memory:")  # Db en memoria
        self.db.crear_tablas()  # Creamos todas las tablas necesarias

    def tearDown(self):
        # Cerrar la conexión después de cada prueba
        self.db.cerrar_conexion()

    def test_insertar(self):
        # Creamos un medicamento "falso" para la prueba
        medicamento = Medicamento(self.db.cursor, id_med=1, nombre="Paracetamol", detalles="Analgésico y antipirético", efec_secun="Náuseas")
        medicamento.insertar_medicamento()

        # Verificamos que el medicamento fue insertado correctamente
        self.db.cursor.execute("SELECT * FROM medicamento WHERE id_med=1")
        resultado = self.db.cursor.fetchone()
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado[1], "Paracetamol")
        self.assertEqual(resultado[2], "Analgésico y antipirético")
        self.assertEqual(resultado[3], "Náuseas")

    def test_editar(self):
        # Insertamos un medicamento "falso" para editarlo después
        medicamento = Medicamento(self.db.cursor, id_med=2, nombre="Ibuprofeno", detalles="Analgésico", efec_secun="Dolor de estómago")
        medicamento.insertar_medicamento()

        # Editamos el medicamento
        medicamento.nombre = "Ibuprofeno 400mg"
        medicamento.detalles = "Analgésico y antiinflamatorio"
        medicamento.editar_medicamento()

        # Verificamos que el cambio se haya realizado correctamente
        self.db.cursor.execute("SELECT * FROM medicamento WHERE id_med=2")
        resultado = self.db.cursor.fetchone()
        self.assertEqual(resultado[1], "Ibuprofeno 400mg")
        self.assertEqual(resultado[2], "Analgésico y antiinflamatorio")

    def test_eliminar(self):
        # Insertamos un medicamento "falso" para eliminarlo
        medicamento = Medicamento(self.db.cursor, id_med=3, nombre="Amoxicilina", detalles="Antibiótico", efec_secun="Reacciones alérgicas")
        medicamento.insertar_medicamento()

        # Eliminamos el medicamento
        medicamento.eliminar_medicamento()

        # Verificamos que el medicamento fue eliminado
        self.db.cursor.execute("SELECT * FROM medicamento WHERE id_med=3")
        resultado = self.db.cursor.fetchone()
        self.assertIsNone(resultado)

    def test_mostrar(self):
        # Insertamos algunos medicamentos "falsos" para verificar que se muestren correctamente
        medicamento1 = Medicamento(self.db.cursor, id_med=4, nombre="Omeprazol", detalles="Protector gástrico", efec_secun="Dolor de cabeza")
        medicamento1.insertar_medicamento()

        medicamento2 = Medicamento(self.db.cursor, id_med=5, nombre="Loratadina", detalles="Antihistamínico", efec_secun="Somnolencia")
        medicamento2.insertar_medicamento()

        # Obtenemos todos los medicamentos y verificamos que se muestren correctamente
        medicamentos = medicamento1.mostrar_medicamentos()
        self.assertEqual(len(medicamentos), 2)
        self.assertEqual(medicamentos[0][1], "Omeprazol")
        self.assertEqual(medicamentos[1][1], "Loratadina")

if __name__ == "__main__":
    unittest.main()
