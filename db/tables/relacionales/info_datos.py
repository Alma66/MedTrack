import sqlite3

class InfoDatos:
    def __init__(self, id_info_datos=None, id_salud=None, id_info=None):
        self.id_info_datos = id_info_datos
        self.id_salud = id_salud
        self.id_info = id_info

    @staticmethod
    def crear_tabla(cursor):
        """Crea la tabla info_datos en la base de datos."""
        query = """
        CREATE TABLE IF NOT EXISTS info_datos (
            id_info_datos INTEGER PRIMARY KEY AUTOINCREMENT,
            id_salud INTEGER NOT NULL,
            id_info INTEGER NOT NULL,
            FOREIGN KEY (id_salud) REFERENCES datosSalud(id_datos_salud) ON DELETE CASCADE,
            FOREIGN KEY (id_info) REFERENCES infoEdu(id_info) ON DELETE CASCADE
        );
        """
        cursor.execute(query)

    def insertar(self, cursor):
        """Inserta un nuevo registro en la tabla info_datos."""
        query = """
        INSERT INTO info_datos (id_salud, id_info)
        VALUES (?, ?);
        """
        cursor.execute(query, (self.id_salud, self.id_info))

    @staticmethod
    def obtener_por_id(cursor, id_info_datos):
        """Obtiene un registro por su ID."""
        query = "SELECT * FROM info_datos WHERE id_info_datos = ?;"
        cursor.execute(query, (id_info_datos,))
        return cursor.fetchone()

    @staticmethod
    def obtener_todos(cursor):
        """Obtiene todos los registros de la tabla."""
        query = "SELECT * FROM info_datos;"
        cursor.execute(query)
        return cursor.fetchall()

    def actualizar(self, cursor):
        """Actualiza un registro existente."""
        if not self.id_info_datos:
            raise ValueError("El ID principal es necesario para actualizar.")
        query = """
        UPDATE info_datos
        SET id_salud = ?, id_info = ?
        WHERE id_info_datos = ?;
        """
        cursor.execute(query, (self.id_salud, self.id_info, self.id_info_datos))

    @staticmethod
    def eliminar(cursor, id_info_datos):
        """Elimina un registro por su ID."""
        query = "DELETE FROM info_datos WHERE id_info_datos = ?;"
        cursor.execute(query, (id_info_datos,))
