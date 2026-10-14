class Biblioteca:
    def __init__(self):
        self.usuarios = []
        self.libros = []
        self.prestamos = []

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
    # Métodos para USUARIOS
    def buscar_usuario(self, id_usuario): # Busqueda de usuario SOLO por identificador
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        return None
    def registrar_usuario(self, usuario):   # Si el usuario existe devuelve False. Si no existe, se registra y devuelve True
        if self.buscar_usuario(usuario.id_usuario) is not None:
            return False
        self.usuarios.append(usuario)
        return True