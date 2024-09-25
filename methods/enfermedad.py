class Enfermedad:
    # Creamos lista de enfermedades
    lista_enfermedades = []
 
    # Inicializamos la enfermedad
    def __init__(self, id_enf, nombre, descripcion):
        self.id_enf = id_enf
        self.nombre = nombre
        self.descripcion = descripcion

    # Creamos metodo para agregar enfermedades
    def agregar_enfermedad(self, id_enf, nombre, descripcion):
        # Verificar que la enfermedad no exista
        for enfermedad in Enfermedad.lista_enfermedades:
            if enfermedad.id_enf == id_enf:
                print("La enfermedad ya está registrada.")
                return
        
        # Si no existe, crea una nueva enfermedad
        nueva_enfermedad = Enfermedad(id_enf, nombre, descripcion)
        Enfermedad.lista_enfermedades.append(nueva_enfermedad)
        print("La enfermedad se agregó correctamente.")

    # Mostramos cada enfermedad y sus datos
    def __str__(self):
        return (f"Enfermedad(id_enf={self.id_enf}, nombre={self.nombre}, descripcion={self.descripcion})")


    # Creamos metodo para eliminar enfermedades
    def eliminar_enfermedad(self, id_enf):
        # Buscar y eliminar la enfermedad
        for enfermedad in Enfermedad.lista_enfermedades:
            if enfermedad.id_enf == id_enf:
                Enfermedad.lista_enfermedades.remove(enfermedad)
                print("La enfermedad se eliminó correctamente.")
                return
        
        # Si no se encuentra la enfermedad
        print("La enfermedad no se encuentra en la lista.")