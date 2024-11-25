class DatosSalud:
    def __init__(self, id_salud=None, id_user=None, altura=None, peso=None, presion=None):
        self.id_salud = id_salud
        self.id_user = id_user
        self.altura = altura
        self.peso = peso
        self.presion = presion

    @staticmethod
    def crear_tabla_datosSalud(cursor):
        cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS datos_salud (
            id_salud INTEGER PRIMARY KEY,
            id_user INTEGER,
            altura REAL,
            peso REAL,
            presion TEXT,
            FOREIGN KEY (id_user) REFERENCES usuarios(id_user)
        )
        """)

    def insertar_datosSalud(self, cursor):
        cursor.execute("""
        INSERT INTO datos_salud (id_salud, id_user, altura, peso, presion)
        VALUES (?, ?, ?, ?, ?)
        """, (self.id_salud, self.id_user, self.altura, self.peso, self.presion))
        cursor.connection.commit()

    def editar_datosSalud(self, cursor):
        cursor.execute("""
        UPDATE datos_salud
        SET altura=?, peso=?, presion=?
        WHERE id_salud=?
        """, (self.altura, self.peso, self.presion, self.id_salud))
        cursor.connection.commit()

    def mostrar_datosSalud(self, cursor):
        cursor.execute("SELECT * FROM datos_salud")
        return cursor.fetchall()

    def eliminar_datosSalud(self, cursor):
        cursor.execute("DELETE FROM datos_salud WHERE id_salud=?", (self.id_salud,))
        cursor.connection.commit()
