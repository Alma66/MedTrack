class InfoEdu:
    # Creamos lista de la información educativa
    lista_info_edu = []

    # Inicializamos la información educativa
    def __init__(self, id_info, titulo, contenido, creditos, id_user):
        self.id_info = id_info
        self.titulo = titulo
        self.contenido = contenido
        self.creditos = creditos
        self.id_user = id_user

    # Creamos metodo para agregar información educativa
    def agregar_info(self, id_info, titulo, contenido, creditos, id_user):
        # Verificar que la información educativa no exista
        for info in InfoEdu.lista_info_edu:
            if info.id_info == id_info:
                print("La información educativa ya está registrada.")
                return
        
        # Si no existe, crea una nueva información educativa
        nueva_info = InfoEdu(id_info, titulo, contenido, creditos, id_user)
        InfoEdu.lista_info_edu.append(nueva_info)
        print("La información educativa se agregó correctamente.")

    # Mostramos cada información educativa y sus datos
    def __str__(self):
        return (f"Informacion Educacional(id_info={self.id_info}, titulo={self.titulo}, "
                f"contenido={self.contenido}, creditos={self.creditos}, "
                f"id_user={self.id_user})")

    # Creamos metodo para eliminar información educativa
    def eliminar_info(self, id_info):
        # Buscar y eliminar la información educativa
        for info in InfoEdu.lista_info_edu:
            if info.id_info == id_info:
                InfoEdu.lista_info_edu.remove(info)
                print("La información educativa se eliminó correctamente.")
                return
        
        # Si no se encuentra la información
        print("La información educativa no se encuentra en la lista.")

    # Creamos metodo para editar y actualizar los datos de la información educativa
    def editar_info(self, id_info, titulo=None, contenido=None, creditos=None, id_user=None):
        # Buscamos la información educativa que se va a editar
        for info in InfoEdu.lista_info_edu:
            if info.id_info == id_info:  # Acceder al atributo de instancia
                # Actualizamos los atributos solo si se proporcionan nuevos valores
                if titulo is not None:
                    info.titulo = titulo
                if contenido is not None:
                    info.contenido = contenido
                if creditos is not None:
                    info.creditos = creditos
                if id_user is not None:
                    info.id_user = id_user
                
                print("La información educativa se actualizó correctamente.")
                return
        
        # Si no se encuentra la información educativa
        print("La información educativa no se encuentra en la lista.")
