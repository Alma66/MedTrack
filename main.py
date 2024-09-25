# Llamamos a las clases desde la carpeta Methods
from methods.usuario import Usuario
from methods.sintoma import Sintoma
from methods.recordatorio import Recordatorio
from methods.medicamento import Medicamento
from methods.infoEdu import InfoEdu
from methods.grafico import Graficos
from methods.enfermedad import Enfermedad
from methods.datosSalud import DatosSalud

def main():
    # Creamos las instancias de las clases
    usuario1 = Usuario(id_user=1, nombre="Juan", apellido="Pérez", fecha_nac="1990-01-01", sexo="M", mail="juan@example.com", contraseña="password123")
    sintoma1 = Sintoma(id_sintoma=1, nombre="Fiebre", descripcion="Temperatura alta")
    recordatorio1 = Recordatorio(id_rec=1, hora="08:00", dosis="1 pastilla", estado="Activo", frecuencia="Diaria", id_user=1, id_med=1)
    medicamento1 = Medicamento(id_med=1, nombre="Paracetamol", detalles="Para fiebre y dolor", efec_secun="Náuseas")
    infoedu1 = InfoEdu(id_info=1, titulo="Cómo tomar medicamentos", contenido="Instrucciones para tomar medicamentos correctamente", creditos="Dr. Enrique", id_user=1)
    grafico1 = Graficos(id_graf=1, titulo="Progreso de Salud", id_user=1, id_rec=1, id_med=1, id_salud=1)
    enfermedad1 = Enfermedad(id_enf=1, nombre="Gripe", descripcion="Enfermedad viral común")
    datos_salud1 = DatosSalud(id_salud=1, id_user=1, altura=180, peso=75.5, presion=120.80)

    # Agregamos objetos a las listas (con el metodo agregar_nameclass)
    usuario1.agregar_usuario(id_user=1, nombre="Juan", apellido="Pérez", fecha_nac="1990-01-01", sexo="M", mail="juan@example.com", contraseña="password123")
    sintoma1.agregar_sintoma(id_sintoma=1, nombre="Fiebre", descripcion="Temperatura alta")
    recordatorio1.agregar_recordatorio(id_rec=1, hora="08:00", dosis="1 pastilla", estado="Activo", frecuencia="Diaria", id_user=1, id_med=1)
    medicamento1.agregar_medicamento(id_med=1, nombre="Paracetamol", detalles="Para fiebre y dolor", efec_secun="Náuseas")
    infoedu1.agregar_info(id_info=1, titulo="Cómo tomar medicamentos", contenido="Instrucciones para tomar medicamentos correctamente", creditos="Dr. Enrique", id_user=1)
    grafico1.agregar_grafico(id_graf=1, titulo="Progreso de Salud", id_user=1, id_rec=1, id_med=1, id_salud=1)
    enfermedad1.agregar_enfermedad(id_enf=1, nombre="Gripe", descripcion="Enfermedad viral común")
    datos_salud1.agregar_dato_salud(id_salud=1, id_user=1, altura=180, peso=75.5, presion=120.80)

    # Mostramos el contenido de las listas de cada clase
    print("Usuarios:", [str(user) for user in Usuario.lista_usuarios])
    print("Síntomas:", [str(sintoma) for sintoma in Sintoma.lista_sintomas])
    print("Recordatorios:", [str(reco) for reco in  Recordatorio.lista_recordatorios])
    print("Medicamentos:", [str(med) for med in Medicamento.lista_medicamentos])
    print("Información Educacional:", [str(infoEdu) for infoEdu in InfoEdu.lista_info_edu])
    print("Gráficos:", [str(grafico) for grafico in Graficos.lista_graficos])
    print("Enfermedades:", [str(enf) for enf in Enfermedad.lista_enfermedades])
    print("Datos de Salud:", [str(datSalud) for datSalud in DatosSalud.lista_datos_salud])

    usuario1.editar_usuario(id_user=1, nombre="Nacho", apellido="Pérez", fecha_nac="1991-02-02", sexo="M", mail="Nacho@example.com", contraseña="newpassword123")
    sintoma1.editar_sintoma(id_sintoma=1, nombre="Nauseas", descripcion="Sensasion de mareo y/o asco")
    recordatorio1.editar_recordatorio(id_rec=1, hora="07:00", dosis="4gm", estado="Activo", frecuencia="Cada 6 hrs", id_user=1, id_med=1)
    medicamento1.editar_medicamento(id_med=1, nombre="Ibuprofeno", detalles="Para fiebre y dolor", efec_secun="Dolor de pansa")
    infoedu1.editar_info(id_info=1, titulo="Intoxicacion por ibuprofeno", contenido="Proteccion contra la intoxicacion", creditos="Dra. Martina", id_user=1)
    grafico1.editar_grafico(id_graf=1, titulo="Progreso en el Peso", id_user=1, id_rec=1, id_med=1, id_salud=1)
    enfermedad1.editar_enfermedad(id_enf=1, nombre="Hipertension", descripcion="Presion Alta")
    datos_salud1.editar_dato_salud(id_salud=1, id_user=1, altura=170, peso=60.5, presion=100.90)

      # Mostramos el contenido de las listas después de eliminar
    print("\nDatos actualizados:")
    print("Usuarios:", [str(user) for user in Usuario.lista_usuarios])
    print("Síntomas:", [str(sintoma) for sintoma in Sintoma.lista_sintomas])
    print("Recordatorios:", [str(reco) for reco in  Recordatorio.lista_recordatorios])
    print("Medicamentos:", [str(med) for med in Medicamento.lista_medicamentos])
    print("Información Educacional:", [str(infoEdu) for infoEdu in InfoEdu.lista_info_edu])
    print("Gráficos:", [str(grafico) for grafico in Graficos.lista_graficos])
    print("Enfermedades:", [str(enf) for enf in Enfermedad.lista_enfermedades])
    print("Datos de Salud:", [str(datSalud) for datSalud in DatosSalud.lista_datos_salud])

    # Eliminamos objetos de las listas (con el metodo eliminar_nameclass)
    usuario1.eliminar_usuario(id_user=1)
    sintoma1.eliminar_sintoma(id_sintoma=1)
    recordatorio1.eliminar_recordatorio(id_rec=1)
    medicamento1.eliminar_medicamento(id_med=1)
    infoedu1.eliminar_info(id_info=1)
    grafico1.eliminar_grafico(id_graf=1)
    enfermedad1.eliminar_enfermedad(id_enf=1)
    datos_salud1.eliminar_dato_salud(id_salud=1)

    # Mostramos el contenido de las listas después de eliminar
    print("\nDespués de eliminar:")
    print("Usuarios:", [str(user) for user in Usuario.lista_usuarios])
    print("Síntomas:", [str(sintoma) for sintoma in Sintoma.lista_sintomas])
    print("Recordatorios:", [str(reco) for reco in  Recordatorio.lista_recordatorios])
    print("Medicamentos:", [str(med) for med in Medicamento.lista_medicamentos])
    print("Información Educacional:", [str(infoEdu) for infoEdu in InfoEdu.lista_info_edu])
    print("Gráficos:", [str(grafico) for grafico in Graficos.lista_graficos])
    print("Enfermedades:", [str(enf) for enf in Enfermedad.lista_enfermedades])
    print("Datos de Salud:", [str(datSalud) for datSalud in DatosSalud.lista_datos_salud])

if __name__ == "__main__":
    main()
