class UserEnf:
    def __init__(self, id_userenf=None, id_user=None, id_enf=None):
        self.id_userenf = id_userenf
        self.id_user = id_user
        self.id_enf = id_enf

    @staticmethod
    def crear_tabla(cursor):
        """Crea la tabla user_enf si no existe."""
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_enf (
            id_userenf INTEGER PRIMARY KEY AUTOINCREMENT,
            id_user INTEGER NOT NULL,
            id_enf INTEGER NOT NULL,
            FOREIGN KEY (id_user) REFERENCES usuarios(id_usuario),
            FOREIGN KEY (id_enf) REFERENCES enfermedad(id_enfermedad)
        );
        """)

    def insertar(self, cursor):
        """Inserta un nuevo registro en la tabla user_enf."""
        cursor.execute("""
        INSERT INTO user_enf (id_user, id_enf)
        VALUES (?, ?);
        """, (self.id_user, self.id_enf))

    @staticmethod
    def obtener_todos(cursor):
        """Obtiene todos los registros de la tabla user_enf."""
        cursor.execute("SELECT * FROM user_enf;")
        return cursor.fetchall()

    @staticmethod
    def obtener_por_id(cursor, id_userenf):
        """Obtiene un registro por su id_userenf."""
        cursor.execute("SELECT * FROM user_enf WHERE id_userenf = ?;", (id_userenf,))
        return cursor.fetchone()

    def actualizar(self, cursor):
        """Actualiza un registro existente en la tabla user_enf."""
        cursor.execute("""
        UPDATE user_enf
        SET id_user = ?, id_enf = ?
        WHERE id_userenf = ?;
        """, (self.id_user, self.id_enf, self.id_userenf))

    @staticmethod
    def eliminar(cursor, id_userenf):
        """Elimina un registro de la tabla user_enf."""
        cursor.execute("DELETE FROM user_enf WHERE id_userenf = ?;", (id_userenf,))
