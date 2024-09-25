class Sintoma:
     # Creamos lista de sintomas
    lista_sintomas = []

    # Inicializamos el sintoma
    def __init__(self, id_sintoma, nombre, descripcion):
        self.id_sintoma = id_sintoma
        self.nombre = nombre
        self.descripcion = descripcion

    # Creamos metodo para agregar sintomas
    def agregar_sintoma(self, id_sintoma, nombre, descripcion):
        # Verificar que el síntoma no exista
        for sintoma in Sintoma.lista_sintomas:
            if sintoma.id_sintoma == id_sintoma:
                print("El síntoma ya está registrado.")
                return
        
        # Si no existe, crea un nuevo síntoma
        nuevo_sintoma = Sintoma(id_sintoma, nombre, descripcion)
        Sintoma.lista_sintomas.append(nuevo_sintoma)
        print("El síntoma se agregó correctamente.")

    # Mostramos cada sintoma y sus datos
    def __str__(self):
        return (f"Sintoma(id_sintoma={self.id_sintoma}, nombre={self.nombre}, descripcion={self.descripcion})")

    # Creamos metodo para eliminar sintomas
    def eliminar_sintoma(self, id_sintoma):
            # Buscar y eliminar el síntoma
            for sintoma in Sintoma.lista_sintomas:
                if sintoma.id_sintoma == id_sintoma:
                    Sintoma.lista_sintomas.remove(sintoma)
                    print("El síntoma se eliminó correctamente.")
                    return
        
            # Si no se encuentra el síntoma
            print("El síntoma no se encuentra en la lista.")

              
