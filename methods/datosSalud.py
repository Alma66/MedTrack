class DatosSalud:
    # Creamos lista de los datos de salud
    lista_datos_salud = []
 
    # Inicializamos los datos de salud
    def __init__(self, id_salud, id_user, altura, peso, presion):
        self.id_salud = id_salud
        self.id_user = id_user
        self.altura = altura
        self.peso = peso
        self.presion = presion

    # Creamos metodo para agregar datos de salud
    def agregar_dato_salud(self, id_salud, id_user, altura, peso, presion):
        # Verificar que los datos de salud no existan
        for dato in DatosSalud.lista_datos_salud:
            if dato.id_salud == id_salud:
                print("Los datos de salud ya están registrados.")
                return
        
        # Si no existen, crea un nuevo dato de salud
        nuevo_dato_salud = DatosSalud(id_salud, id_user, altura, peso, presion)
        DatosSalud.lista_datos_salud.append(nuevo_dato_salud)
        print("Los datos de salud se agregaron correctamente.")

    # Mostramos cada datos de salud y sus datos
    def __str__(self):
        return (f"Datos Salud(id_salud={self.id_salud}, id_user={self.id_user}, altura={self.altura}, "
                f"peso={self.peso}, presion={self.presion})")

     # Creamos metodo para eliminar datos de salud
    def eliminar_dato_salud(self, id_salud):
        # Buscar y eliminar los datos de salud
        for dato in DatosSalud.lista_datos_salud:
            if dato.id_salud == id_salud:
                DatosSalud.lista_datos_salud.remove(dato)
                print("Los datos de salud se eliminaron correctamente.")
                return
        
        # Si no se encuentran los datos
        print("Los datos de salud no se encuentran en la lista.")