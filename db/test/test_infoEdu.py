import unittest
from db.conexion import Conexion
from db.tables.infoEdu import InfoEdu

class TestInfoEdu(unittest.TestCase):

    def setUp(self):
        # Usamos la db de memoria para las pruebas
        self.db = Conexion(":memory:")  # Db en memoria
        self.db.crear_tablas()  # Creamos todas las tablas necesarias
    
        # Insertamos un usuario para la fk
        self.db.cursor.execute("INSERT INTO usuarios (id_user, nombre, apellido, fecha_nac, sexo, mail, contraseña) VALUES (1, 'Carlos', 'González', '1990-05-15', 'M', 'carlos.gonzalez@example.com', '123456')")
    
    def tearDown(self):
        # Cerrar la conexión después de cada prueba
        self.db.cerrar_conexion()

    def test_insertar(self):
        # Creamos un contenido educativo "falso" para la prueba
        infoedu = InfoEdu(self.db.cursor, id_info=1, titulo="Salud Mental", contenido="Importancia de la salud mental", creditos="Dr. Roberto Paez", id_user=1)
        infoedu.insertar_infoedu()

        # Verificamos que el contenido educativo fue insertado correctamente
        self.db.cursor.execute("SELECT * FROM infoedu WHERE id_info=1")
        resultado = self.db.cursor.fetchone()
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado[1], "Salud Mental")
        self.assertEqual(resultado[2], "Importancia de la salud mental")
        self.assertEqual(resultado[3], "Dr. Roberto Paez")
        self.assertEqual(resultado[4], 1)

    def test_editar(self):
        # Insertamos un contenido educativo "falso" para editar después
        infoedu = InfoEdu(self.db.cursor, id_info=2, titulo="Nutrición", contenido="Alimentos saludables", creditos="Dra. Camila Lopez", id_user=1)
        infoedu.insertar_infoedu()

        # Editamos el contenido educativo
        infoedu.titulo = "Nutrición Balanceada"
        infoedu.contenido = "Alimentos saludables y equilibrados"
        infoedu.creditos = "Dra. Diana Herrera"
        infoedu.editar_infoedu()

        # Verificamos que el cambio se haya realizado correctamente
        self.db.cursor.execute("SELECT * FROM infoedu WHERE id_info=2")
        resultado = self.db.cursor.fetchone()
        self.assertEqual(resultado[1], "Nutrición Balanceada")
        self.assertEqual(resultado[2], "Alimentos saludables y equilibrados")
        self.assertEqual(resultado[3], "Dra. Diana Herrera")

    def test_eliminar(self):
        # Insertamos un contenido educativo "falso" para eliminarlo
        infoedu = InfoEdu(self.db.cursor, id_info=3, titulo="Ejercicio Físico", contenido="Beneficios del ejercicio", creditos="Dra. Diana Herrera", id_user=2)
        infoedu.insertar_infoedu()

        # Eliminamos el contenido educativo
        infoedu.eliminar_infoedu()

        # Verificamos que el contenido educativo fue eliminado
        self.db.cursor.execute("SELECT * FROM infoedu WHERE id_info=3")
        resultado = self.db.cursor.fetchone()
        self.assertIsNone(resultado)

    def test_mostrar(self):
        # Insertamos algunos contenidos educativos "falsos" para verificar que se muestren correctamente
        infoedu1 = InfoEdu(self.db.cursor, id_info=4, titulo="Hidratación", contenido="Importancia del agua", creditos="Dra. Diana Herrera", id_user=1)
        infoedu1.insertar_infoedu()

        infoedu2 = InfoEdu(self.db.cursor, id_info=5, titulo="Sueño", contenido="Beneficios de un buen descanso", creditos="Dr. Roberto Paez", id_user=1)
        infoedu2.insertar_infoedu()

        # Obtenemos todos los contenidos educativos y verificamos que se muestren correctamente
        infoedu = infoedu1.mostrar_infoedu()
        self.assertEqual(len(infoedu), 2)
        self.assertEqual(infoedu[0][1], "Hidratación")
        self.assertEqual(infoedu[1][1], "Sueño")

if __name__ == "__main__":
    unittest.main()
