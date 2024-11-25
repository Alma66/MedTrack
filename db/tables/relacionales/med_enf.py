class MedEnf:
    def __init__(self, id_enfmed=None, id_med=None, id_enf=None):
        self.id_enfmed = id_enfmed
        self.id_med = id_med
        self.id_enf = id_enf

    @staticmethod
    def crear_tabla(cursor):
        """Crea la tabla enf_med si no existe."""
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS enf_med (
            id_enfmed INTEGER PRIMARY KEY AUTOINCREMENT,
            id_med INTEGER NOT NULL,
            id_enf INTEGER NOT NULL,
            FOREIGN KEY (id_med) REFERENCES medicamentos(id_medicamento),
            FOREIGN KEY (id_enf) REFERENCES enfermedad(id_enfermedad)
        );
        """)

    def insertar(self, cursor):
        """Inserta un nuevo registro en la tabla enf_med."""
        cursor.execute("""
        INSERT INTO enf_med (id_med, id_enf)
        VALUES (?, ?);
        """, (self.id_med, self.id_enf))

    @staticmethod
    def obtener_todos(cursor):
        """Obtiene todos los registros de la tabla enf_med."""
        cursor.execute("SELECT * FROM enf_med;")
        return cursor.fetchall()

    @staticmethod
    def obtener_por_id(cursor, id_enfmed):
        """Obtiene un registro por su id_enfmed."""
        cursor.execute("SELECT * FROM enf_med WHERE id_enfmed = ?;", (id_enfmed,))
        return cursor.fetchone()

    def actualizar(self, cursor):
        """Actualiza un registro existente en la tabla enf_med."""
        cursor.execute("""
        UPDATE enf_med
        SET id_med = ?, id_enf = ?
        WHERE id_enfmed = ?;
        """, (self.id_med, self.id_enf, self.id_enfmed))

    @staticmethod
    def eliminar(cursor, id_enfmed):
        """Elimina un registro de la tabla enf_med."""
        cursor.execute("DELETE FROM enf_med WHERE id_enfmed = ?;", (id_enfmed,))
