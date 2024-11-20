import unittest
from db.conexion import Conexion
from db.tables.recordatorio import Recordatorio

class TestRecordatorio(unittest.TestCase):

    def setUp(self):
        # Usamos la db de memoria para las pruebas
        self.db = Conexion(":memory:")  # Db en memoria
        self.db.crear_tablas()  # Creamos todas las tablas necesarias

        # Insertamos un usuario y un medicamento para las fk
        self.db.cursor.execute("INSERT INTO usuarios (id_user, nombre, apellido, fecha_nac, sexo, mail, contraseña) VALUES (1, 'Carlos', 'González', '1990-05-15', 'M', 'carlos.gonzalez@example.com', '123456')")
        self.db.cursor.execute("INSERT INTO medicamento (id_med, nombre, detalles, efec_secun) VALUES (1, 'Paracetamol', 'Analgésico', 'Tos')")

    def tearDown(self):
        # Cerrar la conexión después de cada prueba
        self.db.cerrar_conexion()

    def test_insertar(self):
        # Creamos un recordatorio "falso" para la prueba
        recordatorio = Recordatorio(self.db.cursor, id_rec=1, hora="08:00", dosis="500mg", estado="activo", frecuencia="diario", id_user=1, id_med=1)
        recordatorio.insertar_recordatorio()

        # Verificamos que el recordatorio fue insertado correctamente
        self.db.cursor.execute("SELECT * FROM recordatorio WHERE id_rec=1")
        resultado = self.db.cursor.fetchone()
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado[1], "08:00")
        self.assertEqual(resultado[2], "500mg")
        self.assertEqual(resultado[3], "activo")

    def test_editar(self):
        # Insertamos un recordatorio "falso" para editarlo después
        recordatorio = Recordatorio(self.db.cursor, id_rec=2, hora="12:00", dosis="1g", estado="pendiente", frecuencia="semanal", id_user=1, id_med=1)
        recordatorio.insertar_recordatorio()

        # Editamos el recordatorio
        recordatorio.hora = "14:00"
        recordatorio.estado = "completado"
        recordatorio.editar_recordatorio()

        # Verificamos que el cambio se haya realizado correctamente
        self.db.cursor.execute("SELECT * FROM recordatorio WHERE id_rec=2")
        resultado = self.db.cursor.fetchone()
        self.assertEqual(resultado[1], "14:00")
        self.assertEqual(resultado[3], "completado")

    def test_eliminar(self):
        # Insertamos un recordatorio "falso" para eliminarlo
        recordatorio = Recordatorio(self.db.cursor, id_rec=3, hora="18:00", dosis="200mg", estado="pendiente", frecuencia="mensual", id_user=1, id_med=1)
        recordatorio.insertar_recordatorio()

        # Eliminamos el recordatorio
        recordatorio.eliminar_recordatorio()

        # Verificamos que el recordatorio fue eliminado
        self.db.cursor.execute("SELECT * FROM recordatorio WHERE id_rec=3")
        resultado = self.db.cursor.fetchone()
        self.assertIsNone(resultado)

    def test_mostrar(self):
        # Insertamos algunos recordatorios "falsos" para verificar que se muestren correctamente
        recordatorio1 = Recordatorio(self.db.cursor, id_rec=4, hora="07:00", dosis="100mg", estado="activo", frecuencia="diario", id_user=1, id_med=1)
        recordatorio1.insertar_recordatorio()

        recordatorio2 = Recordatorio(self.db.cursor, id_rec=5, hora="22:00", dosis="250mg", estado="pendiente", frecuencia="semanal", id_user=1, id_med=1)
        recordatorio2.insertar_recordatorio()

        # Obtenemos todos los recordatorios y verificamos que se muestren correctamente
        recordatorios = recordatorio1.mostrar_recordatorios()
        self.assertEqual(len(recordatorios), 2)
        self.assertEqual(recordatorios[0][1], "07:00")
        self.assertEqual(recordatorios[1][1], "22:00")

if __name__ == "__main__":
    unittest.main()
