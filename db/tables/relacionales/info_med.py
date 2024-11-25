class InfoMed:
    def __init__(self, id_infomed=None, id_med=None, id_info=None):
        self.id_infomed = id_infomed
        self.id_med = id_med
        self.id_info = id_info

    @staticmethod
    def crear_tabla(cursor):
        """Crea la tabla info_med si no existe."""
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS info_med (
            id_infomed INTEGER PRIMARY KEY AUTOINCREMENT,
            id_med INTEGER NOT NULL,
            id_info INTEGER NOT NULL,
            FOREIGN KEY (id_med) REFERENCES medicamentos(id_medicamento),
            FOREIGN KEY (id_info) REFERENCES infoEdu(id_info)
        );
        """)

    def insertar(self, cursor):
        """Inserta un nuevo registro en la tabla info_med."""
        cursor.execute("""
        INSERT INTO info_med (id_med, id_info)
        VALUES (?, ?);
        """, (self.id_med, self.id_info))

    @staticmethod
    def obtener_todos(cursor):
        """Obtiene todos los registros de la tabla info_med."""
        cursor.execute("SELECT * FROM info_med;")
        return cursor.fetchall()

    @staticmethod
    def obtener_por_id(cursor, id_infomed):
        """Obtiene un registro por su id_infomed."""
        cursor.execute("SELECT * FROM info_med WHERE id_infomed = ?;", (id_infomed,))
        return cursor.fetchone()

    def actualizar(self, cursor):
        """Actualiza un registro existente en la tabla info_med."""
        cursor.execute("""
        UPDATE info_med
        SET id_med = ?, id_info = ?
        WHERE id_infomed = ?;
        """, (self.id_med, self.id_info, self.id_infomed))

    @staticmethod
    def eliminar(cursor, id_infomed):
        """Elimina un registro de la tabla info_med."""
        cursor.execute("DELETE FROM info_med WHERE id_infomed = ?;", (id_infomed,))
