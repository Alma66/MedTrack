import unittest
from db.conexion import Conexion
from db.tables.datosSalud import DatosSalud

class TestDatosSalud(unittest.TestCase):

    def setUp(self):
        # Usamos la db de memoria para las pruebas
        self.db = Conexion(":memory:")  # Db en memoria
        self.db.crear_tablas()  # Crear todas las tablas necesarias

    #Insertamos un usuario para la fk
        self.db.cursor.execute("INSERT INTO usuarios (id_user, nombre, apellido, fecha_nac, sexo, mail, contraseña) VALUES (1, 'Carlos', 'González', '1990-05-15', 'M', 'carlos.gonzalez@example.com', '123456')")

    def tearDown(self):
        # Cerrar la conexión después de cada prueba
        self.db.cerrar_conexion()

    def test_insertar_datosSalud_correcto(self):
        # Creamos un objeto DatosSalud "falso" para la prueba
        datos_salud = DatosSalud(self.db.cursor, id_salud=1, id_user=1, altura=1.75, peso=70.5, presion="120/80")
        datos_salud.insertar_datosSalud()

        # Verificamos que los datos de salud fueron insertados correctamente
        self.db.cursor.execute("SELECT * FROM datos_salud WHERE id_salud=1")
        resultado = self.db.cursor.fetchone()
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado[2], 1.75)
        self.assertEqual(resultado[3], 70.5)
        self.assertEqual(resultado[4], "120/80")

    def test_editar_datosSalud(self):
        # Insertamos un objeto DatosSalud "falso" para editarlo después
        datos_salud = DatosSalud(self.db.cursor, id_salud=2, id_user=2, altura=1.80, peso=80.0, presion="130/85")
        datos_salud.insertar_datosSalud()

        # Editamos los datos de salud
        datos_salud.altura = 1.85
        datos_salud.peso = 85.0
        datos_salud.presion = "125/80"
        datos_salud.editar_datosSalud()

        # Verificamos que los cambios se hayan realizado correctamente
        self.db.cursor.execute("SELECT * FROM datos_salud WHERE id_salud=2")
        resultado = self.db.cursor.fetchone()
        self.assertEqual(resultado[2], 1.85)
        self.assertEqual(resultado[3], 85.0)
        self.assertEqual(resultado[4], "125/80")

    def test_eliminar_datosSalud(self):
        # Insertamos un objeto DatosSalud "falso" para eliminarlo
        datos_salud = DatosSalud(self.db.cursor, id_salud=3, id_user=3, altura=1.70, peso=65.0, presion="118/76")
        datos_salud.insertar_datosSalud()

        # Eliminamos los datos de salud
        datos_salud.eliminar_datosSalud()

        # Verificamos que los datos de salud fueron eliminados
        self.db.cursor.execute("SELECT * FROM datos_salud WHERE id_salud=3")
        resultado = self.db.cursor.fetchone()
        self.assertIsNone(resultado)

    def test_mostrar_datosSalud(self):
        # Insertamos algunos objetos DatosSalud "falsos" para verificar que se muestren correctamente
        datos_salud1 = DatosSalud(self.db.cursor, id_salud=4, id_user=4, altura=1.65, peso=55.5, presion="110/70")
        datos_salud1.insertar_datosSalud()

        datos_salud2 = DatosSalud(self.db.cursor, id_salud=5, id_user=5, altura=1.90, peso=95.0, presion="140/90")
        datos_salud2.insertar_datosSalud()

        # Obtenemos todos los datos de salud y verificamos que se muestren correctamente
        datos = datos_salud1.mostrar_datosSalud()
        self.assertEqual(len(datos), 2)
        self.assertEqual(datos[0][2], 1.65)
        self.assertEqual(datos[1][2], 1.90)

if __name__ == "__main__":
    unittest.main()
