class Recordatorio:
    def __init__(self, cursor, id_rec=None, hora=None, dosis=None, estado=None, frecuencia=None, id_user=None, id_med=None):
        self.cursor = cursor
        self.id_rec = id_rec
        self.hora = hora
        self.dosis = dosis
        self.estado = estado
        self.frecuencia = frecuencia
        self.id_user = id_user
        self.id_med = id_med

    @staticmethod
    def crear_tabla_recordatorio(cursor):
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS recordatorio (
            id_rec INTEGER PRIMARY KEY,
            hora TEXT,
            dosis TEXT,
            estado TEXT,
            frecuencia TEXT,
            id_user INTEGER,
            id_med INTEGER,
            FOREIGN KEY (id_med) REFERENCES medicamento(id_med),
            FOREIGN KEY (id_user) REFERENCES usuarios(id_user)
        )
        """)
 
    def insertar_recordatorio(self):
        self.cursor.execute("""
        INSERT INTO recordatorio (id_rec, hora, dosis, estado, frecuencia, id_user, id_med)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (self.id_rec, self.hora, self.dosis, self.estado, self.frecuencia, self.id_user, self.id_med))
        self.cursor.connection.commit()

    def editar_recordatorio(self):
        self.cursor.execute("""
        UPDATE recordatorio
        SET hora=?, dosis=?, estado=?, frecuencia=?, id_user=?, id_med=?
        WHERE id_rec=?
        """, (self.hora, self.dosis, self.estado, self.frecuencia, self.id_user, self.id_med, self.id_rec))
        self.cursor.connection.commit()

    def mostrar_recordatorios(self):
        self.cursor.execute("SELECT * FROM recordatorio")
        return self.cursor.fetchall()

    def eliminar_recordatorio(self):
        self.cursor.execute("DELETE FROM recordatorio WHERE id_rec=?", (self.id_rec,))
        self.cursor.connection.commit()
