class Sintoma:
    def __init__(self, cursor, id_sintoma=None, nombre=None, descripcion=None):
        self.cursor = cursor
        self.id_sintoma = id_sintoma
        self.nombre = nombre
        self.descripcion = descripcion

    @staticmethod
    def crear_tabla_sintoma(cursor):
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS sintoma (
            id_sintoma INTEGER PRIMARY KEY,
            nombre TEXT,
            descripcion TEXT
        )
        """)

    def insertar_sintoma(self):
        self.cursor.execute("""
        INSERT INTO sintoma (id_sintoma, nombre, descripcion)
        VALUES (?, ?, ?)
        """, (self.id_sintoma, self.nombre, self.descripcion))
        self.cursor.connection.commit()

    def editar_sintoma(self):
        self.cursor.execute("""
        UPDATE sintoma
        SET nombre=?, descripcion=?
        WHERE id_sintoma=?
        """, (self.nombre, self.descripcion, self.id_sintoma))
        self.cursor.connection.commit()

    def mostrar_sintomas(self):
        self.cursor.execute("SELECT * FROM sintoma")
        return self.cursor.fetchall()

    def eliminar_sintoma(self):
        self.cursor.execute("DELETE FROM sintoma WHERE id_sintoma=?", (self.id_sintoma,))
        self.cursor.connection.commit()
