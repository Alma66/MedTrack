class EnfDatos:
    def __init__(self, id_enfdatos=None, id_salud=None, id_enf=None):
        self.id_enfdatos = id_enfdatos
        self.id_salud = id_salud
        self.id_enf = id_enf

    @staticmethod
    def crear_tabla(cursor):
        """Crea la tabla enf_datos si no existe."""
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS enf_datos (
            id_enfdatos INTEGER PRIMARY KEY AUTOINCREMENT,
            id_salud INTEGER NOT NULL,
            id_enf INTEGER NOT NULL,
            FOREIGN KEY (id_salud) REFERENCES datosSalud(id_salud),
            FOREIGN KEY (id_enf) REFERENCES enfermedad(id_enfermedad)
        );
        """)

    def insertar(self, cursor):
        """Inserta un nuevo registro en la tabla enf_datos."""
        cursor.execute("""
        INSERT INTO enf_datos (id_salud, id_enf)
        VALUES (?, ?);
        """, (self.id_salud, self.id_enf))

    @staticmethod
    def obtener_todos(cursor):
        """Obtiene todos los registros de la tabla enf_datos."""
        cursor.execute("SELECT * FROM enf_datos;")
        return cursor.fetchall()

    @staticmethod
    def obtener_por_id(cursor, id_enfdatos):
        """Obtiene un registro por su id_enfdatos."""
        cursor.execute("SELECT * FROM enf_datos WHERE id_enfdatos = ?;", (id_enfdatos,))
        return cursor.fetchone()

    def actualizar(self, cursor):
        """Actualiza un registro existente en la tabla enf_datos."""
        cursor.execute("""
        UPDATE enf_datos
        SET id_salud = ?, id_enf = ?
        WHERE id_enfdatos = ?;
        """, (self.id_salud, self.id_enf, self.id_enfdatos))

    @staticmethod
    def eliminar(cursor, id_enfdatos):
        """Elimina un registro de la tabla enf_datos."""
        cursor.execute("DELETE FROM enf_datos WHERE id_enfdatos = ?;", (id_enfdatos,))
