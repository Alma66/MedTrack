import unittest
from datetime import datetime
from db.conexion import Conexion
from db.tables.usuario import Usuario

class TestUsuario(unittest.TestCase):

    def setUp(self):
        # Usamos la db de memoria para las pruebas
        self.db = Conexion(":memory:")  # Db en memoria
        self.db.crear_tablas()  # Creamos todas las tablas necesarias

    def tearDown(self):
        # Cerrar la conexión después de cada prueba
        self.db.cerrar_conexion()
    
    def convertir_fecha(self, fecha_str):
        # Convertir fecha de cadena (YYYY-MM-DD) a datetime.date
        return datetime.strptime(fecha_str, "%Y-%m-%d").date()
        
    def test_insertar(self):
        # Creamos un usuario "falso" para la prueba
        fecha_nac = self.convertir_fecha("1990-05-15")
        usuario = Usuario(self.db.cursor, id_user=1, nombre="Carlos", apellido="González", 
                          fecha_nac=fecha_nac, sexo="M", mail="carlos.gonzalez@example.com", 
                          contraseña="123456")
        usuario.insertar_usuario()

        # Verificamos que el usuario fue insertado correctamente
        self.db.cursor.execute("SELECT * FROM usuarios WHERE id_user=1")
        resultado = self.db.cursor.fetchone()
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado[1], "Carlos")
        self.assertEqual(resultado[2], "González")
        self.assertEqual(resultado[6], "123456")

    def test_editar(self):
        # Insertamos otro usuario "falso" para editarlo después
        fecha_nac = self.convertir_fecha("1992-07-25")
        usuario = Usuario(self.db.cursor, id_user=2, nombre="Ana", apellido="Pérez", 
                          fecha_nac=fecha_nac, sexo="F", mail="ana.perez@example.com", 
                          contraseña="password")
        usuario.insertar_usuario()

        # Editamos el usuario
        usuario.nombre = "María"
        usuario.apellido = "González"
        usuario.editar_usuario()

        # Verificamos que el cambio se haya realizado correctamente
        self.db.cursor.execute("SELECT * FROM usuarios WHERE id_user=2")
        resultado = self.db.cursor.fetchone()
        self.assertEqual(resultado[1], "María")
        self.assertEqual(resultado[2], "González")

    def test_eliminar(self):
        # Insertamos otro usuario "falso" usuario para eliminarlo
        fecha_nac = self.convertir_fecha("1985-11-10")
        usuario = Usuario(self.db.cursor, id_user=3, nombre="Juan", apellido="Martínez", 
                          fecha_nac=fecha_nac, sexo="M", mail="juan.martinez@example.com", 
                          contraseña="password123")
        usuario.insertar_usuario()

        # Eliminamos el usuario
        usuario.eliminar_usuario()

        # Verificamos que el usuario fue eliminado
        self.db.cursor.execute("SELECT * FROM usuarios WHERE id_user=3")
        resultado = self.db.cursor.fetchone()
        self.assertIsNone(resultado)

    def test_mostrar(self):
        # Insertamos algunos usuarios "falsos" para verificar que se muestren correctamente
        fecha_nac1 = self.convertir_fecha("1980-12-12")
        usuario1 = Usuario(self.db.cursor, id_user=4, nombre="Luis", apellido="Díaz", 
                           fecha_nac=fecha_nac1, sexo="M", mail="luis.diaz@example.com", 
                           contraseña="password456")
        usuario1.insertar_usuario()

        fecha_nac2 = self.convertir_fecha("1995-09-03")
        usuario2 = Usuario(self.db.cursor, id_user=5, nombre="Marta", apellido="Gómez", 
                           fecha_nac=fecha_nac2, sexo="F", mail="marta.gomez@example.com", 
                           contraseña="mypassword")
        usuario2.insertar_usuario()

        # Obtenemos todos los usuarios y verificamos que se muestren correctamente
        usuarios = self.db.mostrar_usuarios()
        self.assertEqual(len(usuarios), 2)
        self.assertEqual(usuarios[0][1], "Luis")
        self.assertEqual(usuarios[1][1], "Marta")

if __name__ == "__main__":
    unittest.main()
