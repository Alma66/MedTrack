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

    # Creamos metodo para editar y actualizar los datos del dato de salud
    def editar_dato_salud(self, id_salud, id_user=None, altura=None, peso=None, presion=None):
        # Buscamos el dato de salud que se va a editar
        for datosSalud in DatosSalud.lista_datos_salud:
            if datosSalud.id_salud == id_salud:
                # Actualizamos los atributos solo si se proporcionan nuevos valores
                # is not None = para verificar si que un valor no este vacio ni sea nulo
                if id_user is not None:
                    datosSalud.id_user = id_user
                if altura is not None:
                    datosSalud.altura = altura
                if peso is not None:
                    datosSalud.peso = peso
                if presion is not None:
                    datosSalud.presion = presion
                
                print("El dato de salud se actualizó correctamente.")
                return
        
        # Si no se encuentra el dato de salud
        print("El dato de salud no se encuentra en la lista.")