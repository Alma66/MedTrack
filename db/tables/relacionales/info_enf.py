class InfoEnf:
    def __init__(self, id_infoenf=None, id_enf=None, id_info=None):
        self.id_infoenf = id_infoenf
        self.id_enf = id_enf
        self.id_info = id_info

    @staticmethod
    def crear_tabla(cursor):
        """Crea la tabla info_enf si no existe."""
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS info_enf (
            id_infoenf INTEGER PRIMARY KEY AUTOINCREMENT,
            id_enf INTEGER NOT NULL,
            id_info INTEGER NOT NULL,
            FOREIGN KEY (id_enf) REFERENCES enfermedad(id_enfermedad),
            FOREIGN KEY (id_info) REFERENCES infoEdu(id_info)
        );
        """)

    def insertar(self, cursor):
        """Inserta un nuevo registro en la tabla info_enf."""
        cursor.execute("""
        INSERT INTO info_enf (id_enf, id_info)
        VALUES (?, ?);
        """, (self.id_enf, self.id_info))

    @staticmethod
    def obtener_todos(cursor):
        """Obtiene todos los registros de la tabla info_enf."""
        cursor.execute("SELECT * FROM info_enf;")
        return cursor.fetchall()

    @staticmethod
    def obtener_por_id(cursor, id_infoenf):
        """Obtiene un registro por su id_infoenf."""
        cursor.execute("SELECT * FROM info_enf WHERE id_infoenf = ?;", (id_infoenf,))
        return cursor.fetchone()

    def actualizar(self, cursor):
        """Actualiza un registro existente en la tabla info_enf."""
        cursor.execute("""
        UPDATE info_enf
        SET id_enf = ?, id_info = ?
        WHERE id_infoenf = ?;
        """, (self.id_enf, self.id_info, self.id_infoenf))

    @staticmethod
    def eliminar(cursor, id_infoenf):
        """Elimina un registro de la tabla info_enf."""
        cursor.execute("DELETE FROM info_enf WHERE id_infoenf = ?;", (id_infoenf,))
