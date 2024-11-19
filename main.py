# Llamamos a las clases desde la carpeta Methods
from methods.usuario import Usuario
from methods.sintoma import Sintoma
from methods.recordatorio import Recordatorio
from methods.medicamento import Medicamento
from methods.infoEdu import InfoEdu
from methods.grafico import Graficos
from methods.enfermedad import Enfermedad
from methods.datosSalud import DatosSalud
from db.conexion import Conexion  

def main():
    conexion = Conexion("db/database.db")

    # Creamos las instancias de las clases
    usuario1 = Usuario(id_user=1, nombre="Juan", apellido="Pérez", fecha_nac="1990-01-01", sexo="M", mail="juan@example.com", contraseña="password123")
    sintoma1 = Sintoma(id_sintoma=1, nombre="Fiebre", descripcion="Temperatura alta")
    medicamento1 = Medicamento(id_med=1, nombre="Paracetamol", detalles="Para fiebre y dolor", efec_secun="Náuseas")
    recordatorio1 = Recordatorio(id_rec=1, hora="08:00", dosis="1 pastilla", estado="Activo", frecuencia="Diaria", id_user=1, id_med=1)
    infoedu1 = InfoEdu(id_info=1, titulo="Cómo tomar medicamentos", contenido="Instrucciones para tomar medicamentos correctamente", creditos="Dr. Enrique", id_user=1)
    enfermedad1 = Enfermedad(id_enf=1, nombre="Gripe", descripcion="Enfermedad viral común")
    datos_salud1 = DatosSalud(id_salud=1, id_user=1, altura=180, peso=75.5, presion=120.80)
    grafico1 = Graficos(id_graf=1, titulo="Progreso de Salud", id_user=1, id_rec=1, id_med=1, id_salud=1)

    # Creamos las tablas
    conexion.crear_tablas()

    # Insertamos los datos de los objetos en las tablas
    conexion.insertar_usuario(usuario1)
    conexion.insertar_sintoma(sintoma1)
    conexion.insertar_medicamento(medicamento1)
    conexion.insertar_recordatorio(recordatorio1)
    conexion.insertar_infoedu(infoedu1)
    conexion.insertar_enfermedad(enfermedad1)
    conexion.insertar_datosSalud(datos_salud1)
    conexion.insertar_grafico(grafico1)

    # Mostramos los datos de las tablas
    print("Usuarios:", conexion.mostrar_usuarios())
    print("Síntomas:", conexion.mostrar_sintomas())
    print("Recordatorios:", conexion.mostrar_recordatorios())
    print("Medicamentos:", conexion.mostrar_medicamentos())
    print("Información Educacional:", conexion.mostrar_infoedu())
    print("Gráficos:", conexion.mostrar_graficos())
    print("Enfermedades:", conexion.mostrar_enfermedades())
    print("Datos de Salud:", conexion.mostrar_datosSalud())

    # Editamos algunos datos
    # Usuario
    usuario1.nombre = "Nacho"
    usuario1.apellido = "Pérez"
    usuario1.fecha_nac = "1991-02-02"
    usuario1.sexo = "M"
    usuario1.mail = "nacho@example.com"
    usuario1.contraseña = "newpassword123"
    conexion.editar_usuario(usuario1)

    # Síntoma
    sintoma1.nombre = "Náuseas"
    sintoma1.descripcion = "Sensación de mareo y/o asco"
    conexion.editar_sintoma(sintoma1)

    # Recordatorio
    recordatorio1.hora = "07:00"
    recordatorio1.dosis = "4gm"
    recordatorio1.estado = "Activo"
    recordatorio1.frecuencia = "Cada 6 hrs"
    conexion.editar_recordatorio(recordatorio1)

    # Medicamento
    medicamento1.nombre = "Ibuprofeno"
    medicamento1.detalles = "Para fiebre y dolor"
    medicamento1.efec_secun = "Dolor de pansa"
    conexion.editar_medicamento(medicamento1)

    # Información Educacional
    infoedu1.titulo = "Intoxicación por ibuprofeno"
    infoedu1.contenido = "Protección contra la intoxicación"
    infoedu1.creditos = "Dra. Martina"
    conexion.editar_infoedu(infoedu1)

    # Gráfico
    grafico1.titulo = "Progreso en el Peso"
    conexion.editar_grafico(grafico1)

    # Enfermedad
    enfermedad1.nombre = "Hipertensión"
    enfermedad1.descripcion = "Presión Alta"
    conexion.editar_enfermedad(enfermedad1)

    # Datos de Salud
    datos_salud1.altura = 170
    datos_salud1.peso = 60.5
    datos_salud1.presion = 100.90
    conexion.editar_datosSalud(datos_salud1)

    # Mostramos los datos después de la edición
    print("\nDatos actualizados:")
    print("Usuarios:", conexion.mostrar_usuarios())
    print("Síntomas:", conexion.mostrar_sintomas())
    print("Recordatorios:", conexion.mostrar_recordatorios())
    print("Medicamentos:", conexion.mostrar_medicamentos())
    print("Información Educacional:", conexion.mostrar_infoedu())
    print("Gráficos:", conexion.mostrar_graficos())
    print("Enfermedades:", conexion.mostrar_enfermedades())
    print("Datos de Salud:", conexion.mostrar_datosSalud())

    # Eliminamos algunos datos
    conexion.eliminar_usuario(id_user=1)
    conexion.eliminar_sintoma(id_sintoma=1)
    conexion.eliminar_recordatorio(id_rec=1)
    conexion.eliminar_medicamento(id_med=1)
    conexion.eliminar_infoedu(id_info=1)
    conexion.eliminar_grafico(id_graf=1)
    conexion.eliminar_enfermedad(id_enf=1)
    conexion.eliminar_datosSalud(id_salud=1)

    # Mostramos los datos después de eliminar
    print("\nDespués de eliminar:")
    print("Usuarios:", conexion.mostrar_usuarios())
    print("Síntomas:", conexion.mostrar_sintomas())
    print("Recordatorios:", conexion.mostrar_recordatorios())
    print("Medicamentos:", conexion.mostrar_medicamentos())
    print("Información Educacional:", conexion.mostrar_infoedu())
    print("Gráficos:", conexion.mostrar_graficos())
    print("Enfermedades:", conexion.mostrar_enfermedades())
    print("Datos de Salud:", conexion.mostrar_datosSalud())

    # Cerramos la conexión
    conexion.cerrar_conexion()

if __name__ == "__main__":
    main()
