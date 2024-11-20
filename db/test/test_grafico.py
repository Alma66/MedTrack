import unittest
from db.conexion import Conexion 
from db.tables.grafico import Graficos

class TestGraficos(unittest.TestCase):

    def setUp(self):
        # Usamos la db de memoria para las pruebas
        self.db = Conexion(":memory:")  # Db en memoria
        self.db.crear_tablas()  # Creamos todas las tablas necesarias

    #Insertamos un usuario, un recordatorio, medicamento y dato de salud para las fk
        self.db.cursor.execute("INSERT INTO usuarios (id_user, nombre, apellido, fecha_nac, sexo, mail, contraseña) VALUES (1, 'Carlos', 'González', '1990-05-15', 'M', 'carlos.gonzalez@example.com', '123456')")
        self.db.cursor.execute("INSERT INTO recordatorio (id_rec, hora, dosis, estado, frecuencia, id_user, id_med) VALUES (1, '08:00', '1 pastilla', 'Activo', 'Diaria', 1, 1)")
        self.db.cursor.execute("INSERT INTO medicamento (id_med, nombre, detalles, efec_secun) VALUES (1, 'Paracetamol', 'Para fiebre y dolor', 'Náuseas')")
        self.db.cursor.execute("INSERT INTO datos_salud (id_salud, id_user, altura, peso, presion) VALUES (1, 1, 180, 75.5, 120.80)")
                               
    def tearDown(self):
        # Cerrar la conexión después de cada prueba
        self.db.cerrar_conexion()

    def test_insertar_grafico_correcto(self):
        # Creamos un gráfico "falso" para la prueba
        grafico = Graficos(self.db.cursor, id_graf=1, titulo="Progreso Semanal", id_user=1, id_rec=1, id_med=1, id_salud=1)
        grafico.insertar_grafico()

        # Verificamos que el gráfico fue insertado correctamente
        self.db.cursor.execute("SELECT * FROM graficos WHERE id_graf=1")
        resultado = self.db.cursor.fetchone()
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado[1], "Progreso Semanal")
        self.assertEqual(resultado[2], 1)
        self.assertEqual(resultado[3], 1)
        self.assertEqual(resultado[4], 1)
        self.assertEqual(resultado[5], 1)

    def test_editar_grafico(self):
        # Insertamos un gráfico "falso" para editarlo después
        grafico = Graficos(self.db.cursor, id_graf=2, titulo="Gráfico Mensual", id_user=1, id_rec=1, id_med=1, id_salud=1)
        grafico.insertar_grafico()

        # Editamos el gráfico
        grafico.titulo = "Progreso Mensual"
        grafico.id_user = 2
        grafico.id_rec = 2
        grafico.id_med = 2
        grafico.id_salud = 2
        grafico.editar_grafico()

        # Verificamos que el cambio se haya realizado correctamente
        self.db.cursor.execute("SELECT * FROM graficos WHERE id_graf=2")
        resultado = self.db.cursor.fetchone()
        self.assertEqual(resultado[1], "Progreso Mensual")
        self.assertEqual(resultado[2], 2)
        self.assertEqual(resultado[3], 2)
        self.assertEqual(resultado[4], 2)
        self.assertEqual(resultado[5], 2)

    def test_eliminar_grafico(self):
        # Insertamos un gráfico "falso" para eliminarlo
        grafico = Graficos(self.db.cursor, id_graf=3, titulo="Progreso Anual", id_user=1, id_rec=1, id_med=1, id_salud=1)
        grafico.insertar_grafico()

        # Eliminamos el gráfico
        grafico.eliminar_grafico()

        # Verificamos que el gráfico fue eliminado
        self.db.cursor.execute("SELECT * FROM graficos WHERE id_graf=3")
        resultado = self.db.cursor.fetchone()
        self.assertIsNone(resultado)

    def test_mostrar_graficos(self):
        # Insertamos algunos gráficos "falsos" para verificar que se muestren correctamente
        grafico1 = Graficos(self.db.cursor, id_graf=4, titulo="Progreso Diario", id_user=1, id_rec=1, id_med=1, id_salud=1)
        grafico1.insertar_grafico()

        grafico2 = Graficos(self.db.cursor, id_graf=5, titulo="Progreso Semanal", id_user=2, id_rec=2, id_med=2, id_salud=2)
        grafico2.insertar_grafico()

        # Obtenemos todos los gráficos y verificamos que se muestren correctamente
        graficos = grafico1.mostrar_graficos()
        self.assertEqual(len(graficos), 2)
        self.assertEqual(graficos[0][1], "Progreso Diario")
        self.assertEqual(graficos[1][1], "Progreso Semanal")

if __name__ == "__main__":
    unittest.main()
