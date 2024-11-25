class UserMed:
    def __init__(self, id_usermed=None, id_user=None, id_med=None):
        self.id_usermed = id_usermed
        self.id_user = id_user
        self.id_med = id_med

    @staticmethod
    def crear_tabla(cursor):
        """Crea la tabla user_med si no existe."""
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_med (
            id_usermed INTEGER PRIMARY KEY AUTOINCREMENT,
            id_user INTEGER NOT NULL,
            id_med INTEGER NOT NULL,
            FOREIGN KEY (id_user) REFERENCES usuarios(id_usuario),
            FOREIGN KEY (id_med) REFERENCES medicamentos(id_medicamento)
        );
        """)

    def insertar(self, cursor):
        """Inserta un nuevo registro en la tabla user_med."""
        cursor.execute("""
        INSERT INTO user_med (id_user, id_med)
        VALUES (?, ?);
        """, (self.id_user, self.id_med))

    @staticmethod
    def obtener_todos(cursor):
        """Obtiene todos los registros de la tabla user_med."""
        cursor.execute("SELECT * FROM user_med;")
        return cursor.fetchall()

    @staticmethod
    def obtener_por_id(cursor, id_usermed):
        """Obtiene un registro por su id_usermed."""
        cursor.execute("SELECT * FROM user_med WHERE id_usermed = ?;", (id_usermed,))
        return cursor.fetchone()

    def actualizar(self, cursor):
        """Actualiza un registro existente en la tabla user_med."""
        cursor.execute("""
        UPDATE user_med
        SET id_user = ?, id_med = ?
        WHERE id_usermed = ?;
        """, (self.id_user, self.id_med, self.id_usermed))

    @staticmethod
    def eliminar(cursor, id_usermed):
        """Elimina un registro de la tabla user_med."""
        cursor.execute("DELETE FROM user_med WHERE id_usermed = ?;", (id_usermed,))
