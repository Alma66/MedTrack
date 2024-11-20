class InfoEdu:
    def __init__(self, cursor, id_info=None, titulo=None, contenido=None, creditos=None, id_user=None):
        self.cursor = cursor
        self.id_info = id_info
        self.titulo = titulo
        self.contenido = contenido
        self.creditos = creditos
        self.id_user = id_user

    @staticmethod
    def crear_tabla_infoedu(cursor):
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS infoedu (
            id_info INTEGER PRIMARY KEY,
            titulo TEXT,
            contenido TEXT,
            creditos TEXT,
            id_user INTEGER,
            FOREIGN KEY (id_user) REFERENCES usuarios(id_user)
        )
        """)

    def insertar_infoedu(self):
        self.cursor.execute("""
        INSERT INTO infoedu (id_info, titulo, contenido, creditos, id_user)
        VALUES (?, ?, ?, ?, ?)
        """, (self.id_info, self.titulo, self.contenido, self.creditos, self.id_user))
        self.cursor.connection.commit()

    def editar_infoedu(self):
        self.cursor.execute("""
        UPDATE infoedu
        SET titulo=?, contenido=?, creditos=?, id_user=?
        WHERE id_info=?
        """, (self.titulo, self.contenido, self.creditos, self.id_user, self.id_info))
        self.cursor.connection.commit()

    def mostrar_infoedu(self):
        self.cursor.execute("SELECT * FROM infoedu")
        return self.cursor.fetchall()

    def eliminar_infoedu(self):
        self.cursor.execute("DELETE FROM infoedu WHERE id_info=?", (self.id_info,))
        self.cursor.connection.commit()
