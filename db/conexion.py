import sqlite3

class Conexion:
    def __init__(self, database):
        self.nombre_bd = database
        self.conexion = sqlite3.connect(database)
        self.cursor = self.conexion.cursor()

    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()
 
    # Llamamos a los métodos para crear las tablas
    def crear_tablas(self):
        from db.tables.usuario import Usuario
        from db.tables.sintoma import Sintoma
        from db.tables.recordatorio import Recordatorio
        from db.tables.medicamento import Medicamento
        from db.tables.infoEdu import InfoEdu
        from db.tables.grafico import Graficos
        from db.tables.enfermedad import Enfermedad
        from db.tables.datosSalud import DatosSalud

        Usuario.crear_tabla_usuario(self.cursor)
        Sintoma.crear_tabla_sintoma(self.cursor)
        Medicamento.crear_tabla_medicamento(self.cursor)
        Recordatorio.crear_tabla_recordatorio(self.cursor)
        InfoEdu.crear_tabla_infoedu(self.cursor)
        Enfermedad.crear_tabla_enfermedad(self.cursor)
        DatosSalud.crear_tabla_datosSalud(self.cursor)
        Graficos.crear_tabla_grafico(self.cursor)

    # Métodos de inserción, deben recibir objetos para insertar los datos
    def insertar_usuario(self, usuario):
        from db.tables.usuario import Usuario
        usuario.id_user = None 
        Usuario(self.cursor, usuario.id_user, usuario.nombre, usuario.apellido, usuario.fecha_nac, usuario.sexo, usuario.mail, usuario.contraseña).insertar_usuario()

    def insertar_sintoma(self, sintoma):
        from db.tables.sintoma import Sintoma
        Sintoma(self.cursor, sintoma.id_sintoma, sintoma.descripcion).insertar_sintoma()

    def insertar_medicamento(self, medicamento):
        from db.tables.medicamento import Medicamento
        Medicamento(self.cursor, medicamento.id_med, medicamento.nombre, medicamento.detalles, medicamento.efec_secun).insertar_medicamento()

    def insertar_recordatorio(self, recordatorio):
        from db.tables.recordatorio import Recordatorio
        Recordatorio(self.cursor, recordatorio.id_rec, recordatorio.hora, recordatorio.dosis, recordatorio.estado, recordatorio.frecuencia, recordatorio.id_user, recordatorio.id_med).insertar_recordatorio()

    def insertar_infoedu(self, infoedu):
        from db.tables.infoEdu import InfoEdu
        InfoEdu(self.cursor, infoedu.id_info, infoedu.titulo, infoedu.contenido, infoedu.creditos, infoedu.id_user).insertar_infoedu()

    def insertar_enfermedad(self, enfermedad):
        from db.tables.enfermedad import Enfermedad
        Enfermedad(self.cursor, enfermedad.id_enf, enfermedad.nombre).insertar_enfermedad()

    def insertar_datosSalud(self, datos_salud):
        from db.tables.datosSalud import DatosSalud
        DatosSalud(self.cursor, datos_salud.id_salud, datos_salud.id_user, datos_salud.altura, datos_salud.peso, datos_salud.presion).insertar_datosSalud()

    def insertar_grafico(self, grafico):
        from db.tables.grafico import Graficos
        Graficos(self.cursor, grafico.id_graf, grafico.titulo, grafico.id_user, grafico.id_rec, grafico.id_med, grafico.id_salud).insertar_grafico()
        
    # Métodos de eliminación, deben recibir el identificador para eliminar
    def eliminar_usuario(self, id_user):
        from db.tables.usuario import Usuario
        Usuario(self.cursor, id_user).eliminar_usuario()

    def eliminar_sintoma(self, id_sintoma):
        from db.tables.sintoma import Sintoma
        Sintoma(self.cursor, id_sintoma).eliminar_sintoma()

    def eliminar_recordatorio(self, id_rec):
        from db.tables.recordatorio import Recordatorio
        Recordatorio(self.cursor, id_rec).eliminar_recordatorio()

    def eliminar_medicamento(self, id_med):
        from db.tables.medicamento import Medicamento
        Medicamento(self.cursor, id_med).eliminar_medicamento()

    def eliminar_infoedu(self, id_info):
        from db.tables.infoEdu import InfoEdu
        InfoEdu(self.cursor, id_info).eliminar_infoedu()

    def eliminar_grafico(self, id_graf):
        from db.tables.grafico import Graficos
        Graficos(self.cursor, id_graf).eliminar_grafico()

    def eliminar_enfermedad(self, id_enf):
        from db.tables.enfermedad import Enfermedad
        Enfermedad(self.cursor, id_enf).eliminar_enfermedad()

    def eliminar_datosSalud(self, id_salud):
        from db.tables.datosSalud import DatosSalud
        DatosSalud(self.cursor, id_salud).eliminar_datosSalud()

    # Métodos de edición, deben recibir objetos para editar los datos
    def editar_usuario(self, usuario):
        from db.tables.usuario import Usuario
        Usuario(self.cursor, usuario.id_user, usuario.nombre, usuario.apellido, usuario.fecha_nac, usuario.sexo, usuario.mail, usuario.contraseña).editar_usuario()

    def editar_sintoma(self, sintoma):
        from db.tables.sintoma import Sintoma
        Sintoma(self.cursor, sintoma.id_sintoma, sintoma.descripcion).editar_sintoma()

    def editar_recordatorio(self, recordatorio):
        from db.tables.recordatorio import Recordatorio
        Recordatorio(self.cursor, recordatorio.id_rec, recordatorio.hora, recordatorio.dosis, recordatorio.estado, recordatorio.frecuencia, recordatorio.id_user, recordatorio.id_med).editar_recordatorio()

    def editar_medicamento(self, medicamento):
        from db.tables.medicamento import Medicamento
        Medicamento(self.cursor, medicamento.id_med, medicamento.nombre, medicamento.detalles, medicamento.efec_secun).editar_medicamento()

    def editar_infoedu(self, infoedu):
        from db.tables.infoEdu import InfoEdu
        InfoEdu(self.cursor, infoedu.id_info, infoedu.titulo, infoedu.contenido, infoedu.creditos, infoedu.id_user).editar_infoedu()

    def editar_grafico(self, grafico):
        from db.tables.grafico import Graficos
        Graficos(self.cursor, grafico.id_graf, grafico.titulo, grafico.id_user, grafico.id_rec, grafico.id_med, grafico.id_salud).editar_grafico()

    def editar_enfermedad(self, enfermedad):
        from db.tables.enfermedad import Enfermedad
        Enfermedad(self.cursor, enfermedad.id_enf, enfermedad.nombre).editar_enfermedad()

    def editar_datosSalud(self, datos_salud):
        from db.tables.datosSalud import DatosSalud
        DatosSalud(self.cursor, datos_salud.id_salud, datos_salud.id_user, datos_salud.altura, datos_salud.peso, datos_salud.presion).editar_datosSalud()

    # Métodos para mostrar las tablas, ahora retornan los resultados
    def mostrar_usuarios(self):
        from db.tables.usuario import Usuario
        return Usuario(self.cursor).mostrar_usuarios()

    def mostrar_sintomas(self):
        from db.tables.sintoma import Sintoma
        return Sintoma(self.cursor).mostrar_sintomas()

    def mostrar_recordatorios(self):
        from db.tables.recordatorio import Recordatorio
        return Recordatorio(self.cursor).mostrar_recordatorios()

    def mostrar_medicamentos(self):
        from db.tables.medicamento import Medicamento
        return Medicamento(self.cursor).mostrar_medicamentos()

    def mostrar_infoedu(self):
        from db.tables.infoEdu import InfoEdu
        return InfoEdu(self.cursor).mostrar_infoedu()

    def mostrar_graficos(self):
        from db.tables.grafico import Graficos
        return Graficos(self.cursor).mostrar_graficos()

    def mostrar_enfermedades(self):
        from db.tables.enfermedad import Enfermedad
        return Enfermedad(self.cursor).mostrar_enfermedades()

    def mostrar_datosSalud(self):
        from db.tables.datosSalud import DatosSalud
        return DatosSalud(self.cursor).mostrar_datosSalud()