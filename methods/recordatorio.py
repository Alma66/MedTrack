class Recordatorio:
    # Creamos lista de recordatorios
    lista_recordatorios = []

    # Inicializamos el recordatorio
    def __init__(self, id_rec, hora, dosis, estado, frecuencia, id_user, id_med):
        self.id_rec = id_rec
        self.hora = hora
        self.dosis = dosis
        self.estado = estado
        self.frecuencia = frecuencia
        self.id_user = id_user
        self.id_med = id_med

    # Creamos metodo para agregar recordatorios
    def agregar_recordatorio(self, id_rec, hora, dosis, estado, frecuencia, id_user, id_med):
        # Verificar que el recordatorio no exista
        for recordatorio in Recordatorio.lista_recordatorios:
            if recordatorio.id_rec == id_rec:
                print("El recordatorio ya está registrado.")
                return
        
        # Si no existe, crea un nuevo recordatorio
        nuevo_recordatorio = Recordatorio(id_rec, hora, dosis, estado, frecuencia, id_user, id_med)
        Recordatorio.lista_recordatorios.append(nuevo_recordatorio)
        print("El recordatorio se agregó correctamente.")

    # Mostramos cada recordatorio y sus datos
    def __str__(self):
        return (f"Recordatorio(id_rec={self.id_rec}, hora={self.hora}, dosis={self.dosis}, "
                f"estado={self.estado}, frecuencia={self.frecuencia}, id_user={self.id_user}, "
                f"id_med={self.id_med})")

    # Creamos metodo para eliminar recordatorios
    def eliminar_recordatorio(self, id_rec):
            # Buscar y eliminar el recordatorio
            for recordatorio in Recordatorio.lista_recordatorios:
                if recordatorio.id_rec == id_rec:
                    Recordatorio.lista_recordatorios.remove(recordatorio)
                    print("El recordatorio se eliminó correctamente.")
                    return
            
            # Si no se encuentra el recordatorio
            print("El recordatorio no se encuentra en la lista.")

     # Creamos metodo para editar y actualizar los datos del recordatorio
    def editar_recordatorio(self, id_rec, hora=None, dosis=None, estado=None, frecuencia=None, id_user=None, id_med=None):
        for recordatorio in Recordatorio.lista_recordatorios:
            if recordatorio.id_rec == id_rec:
                if hora is not None:
                    recordatorio.hora = hora
                if dosis is not None:
                    recordatorio.dosis = dosis
                if estado is not None:
                    recordatorio.estado = estado
                if frecuencia is not None:
                    recordatorio.frecuencia = frecuencia
                if id_user is not None:
                    recordatorio.id_user = id_user
                if id_med is not None:
                    recordatorio.id_med = id_med
                print("El recordatorio se actualizó correctamente.")
                return
        print("El recordatorio no se encuentra en la lista.")