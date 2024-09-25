class Medicamento:
    # Creamos lista de medicamentos
    lista_medicamentos = []

    # Inicializamos el medicamento
    def __init__(self, id_med, nombre, detalles, efec_secun):
        self.id_med = id_med
        self.nombre = nombre
        self.detalles = detalles
        self.efec_secun = efec_secun

    # Creamos metodo para agregar medicamentos
    def agregar_medicamento(self, id_med, nombre, detalles, efec_secun):
        # Verificar que el medicamento no exista
        for medicamento in Medicamento.lista_medicamentos:
            if medicamento.id_med == id_med:
                print("El medicamento ya está registrado.")
                return
        
        # Si no existe, crea un nuevo medicamento
        nuevo_medicamento = Medicamento(id_med, nombre, detalles, efec_secun)
        Medicamento.lista_medicamentos.append(nuevo_medicamento)
        print("El medicamento se agregó correctamente.")

    # Mostramos cada medicamento y sus datos
    def __str__(self):
        return (f"Medicamento(id_med={self.id_med}, nombre={self.nombre}, detalles={self.detalles}, "
                f"efec_secun={self.efec_secun})")

    # Creamos metodo para eliminar medicamentos
    def eliminar_medicamento(self, id_med):
        # Buscar y eliminar el medicamento
        for medicamento in Medicamento.lista_medicamentos:
            if medicamento.id_med == id_med:
                Medicamento.lista_medicamentos.remove(medicamento)
                print("El medicamento se eliminó correctamente.")
                return
        
        # Si no se encuentra el medicamento
        print("El medicamento no se encuentra en la lista.")

    # Creamos metodo para editar y actualizar los datos del medicamento
    def editar_medicamento(self, id_med, nombre=None, detalles=None, efec_secun=None):
        # Buscamos el medicamento que se va a editar
        for medicamento in Medicamento.lista_medicamentos:
            if medicamento.id_med == id_med:  # Acceder al atributo de instancia
                # Actualizamos los atributos solo si se proporcionan nuevos valores
                if nombre is not None:
                    medicamento.nombre = nombre
                if detalles is not None:
                    medicamento.detalles = detalles
                if efec_secun is not None:
                    medicamento.efec_secun = efec_secun
                
                print("El medicamento se actualizó correctamente.")
                return
        
        # Si no se encuentra el medicamento
        print("El medicamento no se encuentra en la lista.")
