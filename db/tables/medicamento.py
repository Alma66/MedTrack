class Medicamento:
    def __init__(self, cursor, id_med=None, nombre=None, detalles=None, efec_secun=None):
        self.cursor = cursor
        self.id_med = id_med
        self.nombre = nombre
        self.detalles = detalles
        self.efec_secun = efec_secun

    @staticmethod
    def crear_tabla_medicamento(cursor):
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS medicamento (
            id_med INTEGER PRIMARY KEY,
            nombre TEXT,
            detalles TEXT,
            efec_secun TEXT
        )
        """)

    def insertar_medicamento(self):
        self.cursor.execute("""
        INSERT INTO medicamento (id_med, nombre, detalles, efec_secun)
        VALUES (?, ?, ?, ?)
        """, (self.id_med, self.nombre, self.detalles, self.efec_secun))
        self.cursor.connection.commit()

    def editar_medicamento(self):
        self.cursor.execute("""
        UPDATE medicamento
        SET nombre=?, detalles=?, efec_secun=?
        WHERE id_med=?
        """, (self.nombre, self.detalles, self.efec_secun, self.id_med))
        self.cursor.connection.commit()

    def mostrar_medicamentos(self):
        self.cursor.execute("SELECT * FROM medicamento")
        return self.cursor.fetchall()

    def eliminar_medicamento(self):
        self.cursor.execute("DELETE FROM medicamento WHERE id_med=?", (self.id_med,))
        self.cursor.connection.commit()
