class Biblioteca:
    def __init__(self):
        self.usuarios = []
        self.libros = []
        self.prestamos = []
    # MÉTODOS PARA LIBROS
    def registrar_libro(self, libro):
        """Este método realiza una comprobación por ISBN llamando al método de busqueda por isbn.
        Si el libro existe devuelve False. Si no existe, se registra y devuelve True"""
        if self.buscar_libro_por_isbn(libro.isbn) is not None:
            return False
        self.libros.append(libro)
        return True
    # Métodos de búsqueda de libros
    def buscar_libro_por_isbn(self, isbn):
        """Busqueda de libro por ISBN por coincidencia exacta"""
        if not isbn:    # Protección por si el ISBN recibido es una cadena vacía
            return None
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None
    def buscar_libros_por_titulo(self, titulo):
        """Búsqueda de libros por título por coincidencia parcial (case insensitive)"""
        if not titulo:  # Protección para título vacío.
            return []
        resultados = []
        for libro in self.libros:
            if titulo.casefold() in libro.titulo.casefold():
                resultados.append(libro)
        return resultados
    def buscar_libros_por_autor(self, autor):
        """Búsqueda de libros por autor con coincidencia parcial (case insensitive)"""
        if not autor:   # Protección para autor vacío.
            return []
        resultados = []
        for libro in self.libros:
            if autor.casefold() in libro.autor.casefold():
                resultados.append(libro)
        return resultados
    def listar_libros(self):
        """Método para listar los libros registrados en la biblioteca.
        Devuelve una lista vacía si no hay libros registrados.
        La lista vacía equivale a None en el contexto de la función que llama este método.
        Equivale también a False."""
        return self.libros
    # Métodos para USUARIOS
    def buscar_usuario(self, id_usuario):
        """Devuelve el objeto usuario si lo encuentra. Devuelve None si no lo encuentra.
        La búsqueda será por coincidencia exacta del identificador"""
        for usuario in self.usuarios:
            if usuario.id == id_usuario:
                return usuario
        return None
    def registrar_usuario(self, usuario):   # Si el usuario existe devuelve False. Si no existe, se registra y devuelve True
        if self.buscar_usuario(usuario.id) is not None:
            return False
        self.usuarios.append(usuario)
        return True
    