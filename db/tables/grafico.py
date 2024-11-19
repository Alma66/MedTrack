class Graficos:
    def __init__(self, cursor, id_graf=None, titulo=None, id_user=None, id_rec=None, id_med=None, id_salud=None):
        self.cursor = cursor
        self.id_graf = id_graf
        self.titulo = titulo
        self.id_user = id_user
        self.id_rec = id_rec
        self.id_med = id_med
        self.id_salud = id_salud

    @staticmethod
    def crear_tabla_grafico(cursor):
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS graficos (
            id_graf INTEGER PRIMARY KEY,
            titulo TEXT,
            id_user INTEGER,
            id_rec INTEGER,
            id_med INTEGER,
            id_salud INTEGER,
            FOREIGN KEY (id_user) REFERENCES usuarios(id_user),
            FOREIGN KEY (id_rec) REFERENCES recordatorio(id_rec),
            FOREIGN KEY (id_med) REFERENCES medicamento(id_med),
            FOREIGN KEY (id_salud) REFERENCES datos_salud(id_salud)
        )
        """)

    def insertar_grafico(self):
        self.cursor.execute("""
        INSERT INTO graficos (id_graf, titulo, id_user, id_rec, id_med, id_salud)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (self.id_graf, self.titulo, self.id_user, self.id_rec, self.id_med, self.id_salud))
        self.cursor.connection.commit()

    def editar_grafico(self):
        self.cursor.execute("""
        UPDATE graficos
        SET titulo=?, id_user=?, id_rec=?, id_med=?, id_salud=?
        WHERE id_graf=?
        """, (self.titulo, self.id_user, self.id_rec, self.id_med, self.id_salud, self.id_graf))
        self.cursor.connection.commit()

    def mostrar_graficos(self):
        self.cursor.execute("SELECT * FROM graficos")
        return self.cursor.fetchall()

    def eliminar_grafico(self):
        self.cursor.execute("DELETE FROM graficos WHERE id_graf=?", (self.id_graf,))
        self.cursor.connection.commit()
