class Usuario:
    # Creamos lista de usuarios
    lista_usuarios = []

    # Inicializamos el usuario
    def __init__(self, id_user, nombre, apellido, fecha_nac, sexo, mail, contraseña):
        self.id_user = id_user
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nac = fecha_nac
        self.sexo = sexo
        self.mail = mail
        self.contraseña = contraseña

    # Creamos metodo para agregar usuarios
    def agregar_usuario(self, id_user, nombre, apellido, fecha_nac, sexo, mail, contraseña):
        # Verificar que el usuario no exista
        for usuario in Usuario.lista_usuarios:
            if usuario.id_user == id_user:
                print("El usuario ya existe.")
                return
        
        # Si no existe, crea un nuevo usuario
        nuevo_usuario = Usuario(id_user, nombre, apellido, fecha_nac, sexo, mail, contraseña)
        Usuario.lista_usuarios.append(nuevo_usuario)
        print("El usuario se agregó correctamente.")

    # Mostramos cada usuario y sus datos
    def __str__(self):
        return (f"Usuario(id_user={self.id_user}, nombre={self.nombre}, apellido={self.apellido}, "
                f"fecha_nac={self.fecha_nac}, sexo={self.sexo}, mail={self.mail}, "
                f"contraseña={self.contraseña})")

    # Creamos metodo para eliminar usuarios
    def eliminar_usuario(self, id_user):
        # Buscar y eliminar el usuario
        for usuario in Usuario.lista_usuarios:
            if usuario.id_user == id_user:
                Usuario.lista_usuarios.remove(usuario)
                print("El usuario se eliminó correctamente.")
                return
        
        # Si no se encuentra el usuario
        print("El usuario no se encuentra en la lista.")
