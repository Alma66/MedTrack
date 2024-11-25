class EnfSintoma:
    def __init__(self, id_enfsintoma=None, id_sintoma=None, id_enf=None):
        self.id_enfsintoma = id_enfsintoma
        self.id_sintoma = id_sintoma
        self.id_enf = id_enf

    @staticmethod
    def crear_tabla(cursor):
        """Crea la tabla enf_sintoma si no existe."""
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS enf_sintoma (
            id_enfsintoma INTEGER PRIMARY KEY AUTOINCREMENT,
            id_sintoma INTEGER NOT NULL,
            id_enf INTEGER NOT NULL,
            FOREIGN KEY (id_sintoma) REFERENCES sintoma(id_sintoma),
            FOREIGN KEY (id_enf) REFERENCES enfermedad(id_enfermedad)
        );
        """)

    def insertar(self, cursor):
        """Inserta un nuevo registro en la tabla enf_sintoma."""
        cursor.execute("""
        INSERT INTO enf_sintoma (id_sintoma, id_enf)
        VALUES (?, ?);
        """, (self.id_sintoma, self.id_enf))

    @staticmethod
    def obtener_todos(cursor):
        """Obtiene todos los registros de la tabla enf_sintoma."""
        cursor.execute("SELECT * FROM enf_sintoma;")
        return cursor.fetchall()

    @staticmethod
    def obtener_por_id(cursor, id_enfsintoma):
        """Obtiene un registro por su id_enfsintoma."""
        cursor.execute("SELECT * FROM enf_sintoma WHERE id_enfsintoma = ?;", (id_enfsintoma,))
        return cursor.fetchone()

    def actualizar(self, cursor):
        """Actualiza un registro existente en la tabla enf_sintoma."""
        cursor.execute("""
        UPDATE enf_sintoma
        SET id_sintoma = ?, id_enf = ?
        WHERE id_enfsintoma = ?;
        """, (self.id_sintoma, self.id_enf, self.id_enfsintoma))

    @staticmethod
    def eliminar(cursor, id_enfsintoma):
        """Elimina un registro de la tabla enf_sintoma."""
        cursor.execute("DELETE FROM enf_sintoma WHERE id_enfsintoma = ?;", (id_enfsintoma,))
