class Usuario:
    def __init__(self, cursor, id_user=None, nombre=None, apellido=None, fecha_nac=None, sexo=None, mail=None, contraseña=None):
        self.cursor = cursor
        self.id_user = id_user
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nac = fecha_nac
        self.sexo = sexo
        self.mail = mail
        self.contraseña = contraseña

    @staticmethod
    def crear_tabla_usuario(cursor):
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id_user INTEGER PRIMARY KEY,
            nombre TEXT,
            apellido TEXT,
            fecha_nac DATE,
            sexo TEXT,
            mail TEXT,
            contraseña TEXT
        )
        """)

    def insertar_usuario(self):
        self.cursor.execute("""
        INSERT INTO usuarios (id_user, nombre, apellido, fecha_nac, sexo, mail, contraseña)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            self.id_user, 
            self.nombre, 
            self.apellido, 
            self.fecha_nac if isinstance(self.fecha_nac, str) else self.fecha_nac.strftime("%Y-%m-%d"), 
            self.sexo, 
            self.mail, 
            self.contraseña
        ))
        self.cursor.connection.commit()


    def editar_usuario(self):
        self.cursor.execute("""
        UPDATE usuarios
        SET nombre=?, apellido=?, fecha_nac=?, sexo=?, mail=?, contraseña=?
        WHERE id_user=?
        """, (self.nombre, self.apellido, self.fecha_nac, self.sexo, self.mail, self.contraseña, self.id_user))
        self.cursor.connection.commit()

    def mostrar_usuarios(self):
        self.cursor.execute("SELECT * FROM usuarios")
        return self.cursor.fetchall()

    def eliminar_usuario(self):
        self.cursor.execute("DELETE FROM usuarios WHERE id_user=?", (self.id_user,))
        self.cursor.connection.commit()