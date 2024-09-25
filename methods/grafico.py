class Graficos:
    # Creamos lista de graficos
    lista_graficos = []
 
    # Inicializamos el grafico
    def __init__(self, id_graf, titulo, id_user, id_rec, id_med, id_salud):
        self.id_graf = id_graf
        self.titulo = titulo
        self.id_user = id_user
        self.id_rec = id_rec
        self.id_med = id_med
        self.id_salud = id_salud

    # Creamos metodo para agregar enfermedades
    def agregar_grafico(self, id_graf, titulo, id_user, id_rec, id_med, id_salud):
        # Verificar que el gráfico no exista
        for grafico in Graficos.lista_graficos:
            if grafico.id_graf == id_graf:
                print("El gráfico ya está registrado.")
                return
        
        # Si no existe, crea un nuevo gráfico
        nuevo_grafico = Graficos(id_graf, titulo, id_user, id_rec, id_med, id_salud)
        Graficos.lista_graficos.append(nuevo_grafico)
        print("El gráfico se agregó correctamente.")

     # Mostramos cada gráfico y sus datos
    def __str__(self):
        return (f"Grafico(id_graf={self.id_graf}, titulo={self.titulo}, id_user={self.id_user}, "
                f"id_rec={self.id_rec}, id_med={self.id_med}, id_salud={self.id_salud})")

    # Creamos metodo para eliminar gráficos
    def eliminar_grafico(self, id_graf):
        # Buscar y eliminar el gráfico
        for grafico in Graficos.lista_graficos:
            if grafico.id_graf == id_graf:
                Graficos.lista_graficos.remove(grafico)
                print("El gráfico se eliminó correctamente.")
                return
        
        # Si no se encuentra el gráfico
        print("El gráfico no se encuentra en la lista.")