from modelos.prestamo import Prestamo
from datetime import date

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
    # MÉTODOS PARA USUARIOS
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
    # MÉTODOS PARA PRESTAMOS
    def buscar_prestamo_activo(self, isbn):
        """Método auxiliar para buscar préstamos activos de un libro por ISBN
        Tiene en cuenta que el préstamo esté activo y que el ISBN coincida exactamente."""
        for prestamo in self.prestamos:
            if prestamo.libro.isbn == isbn and prestamo.activo:
                return prestamo
        return None
    def realizar_prestamo(self, usuario, libro):

        if usuario is None or libro is None:
            return False

        usuario_registrado = self.buscar_usuario(usuario.id)
        libro_registrado = self.buscar_libro_por_isbn(libro.isbn)

        if usuario_registrado is None or libro_registrado is None:
            return False

        if not libro_registrado.disponible:
            return False

        if self.buscar_prestamo_activo(libro_registrado.isbn) is not None:
            return False

        prestamo = Prestamo(usuario_registrado, libro_registrado)
        self.prestamos.append(prestamo)
        libro_registrado.disponible = False

        return True

    def registrar_devolucion(self, isbn):
        prestamo = self.buscar_prestamo_activo(isbn)
    
        if prestamo is None:
            return False
    
        prestamo.fecha_devolucion = date.today()
        prestamo.libro.disponible = True
        return True