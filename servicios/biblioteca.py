class Biblioteca:
    def __init__(self):
        self.usuarios = []
        self.libros = []
        self.prestamos = []
    # Métodos para LIBROS
    def registrar_libro(self, libro):
        if self.buscar_libro(libro) is not None:
            return False
        self.libros.append(libro)
        return True
    
    def buscar_libro(self, libro_nuevo):
        for libro in self.libros:
            if libro.__eq__(libro_nuevo):
                return libro
        return None
    # Método para listar los libros registrados
    def listar_libros(self):
        return self.libros  # Si no hay libros se devuelve vacia ([] equivale a None)
    # Métodos para USUARIOS
    def buscar_usuario(self, id_usuario): # Busqueda de usuario SOLO por identificador
        for usuario in self.usuarios:
            if usuario.id == id_usuario:
                return usuario
        return None
    def registrar_usuario(self, usuario):   # Si el usuario existe devuelve False. Si no existe, se registra y devuelve True
        if self.buscar_usuario(usuario.id) is not None:
            return False
        self.usuarios.append(usuario)
        return True
    