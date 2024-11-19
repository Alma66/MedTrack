class Enfermedad:
    def __init__(self, cursor, id_enf=None, nombre=None, descripcion=None):
        self.cursor = cursor
        self.id_enf = id_enf
        self.nombre = nombre
        self.descripcion = descripcion

    @staticmethod
    def crear_tabla_enfermedad(cursor):
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS enfermedad (
            id_enf INTEGER PRIMARY KEY,
            nombre TEXT,
            descripcion TEXT
        )
        """)

    def insertar_enfermedad(self):
        self.cursor.execute("""
        INSERT INTO enfermedad (id_enf, nombre, descripcion)
        VALUES (?, ?, ?)
        """, (self.id_enf, self.nombre, self.descripcion))
        self.cursor.connection.commit()

    def editar_enfermedad(self):
        self.cursor.execute("""
        UPDATE enfermedad
        SET nombre=?, descripcion=?
        WHERE id_enf=?
        """, (self.nombre, self.descripcion, self.id_enf))
        self.cursor.connection.commit()

    def mostrar_enfermedades(self):
        self.cursor.execute("SELECT * FROM enfermedad")
        return self.cursor.fetchall()

    def eliminar_enfermedad(self):
        self.cursor.execute("DELETE FROM enfermedad WHERE id_enf=?", (self.id_enf,))
        self.cursor.connection.commit()
