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