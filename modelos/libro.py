class Libro:
    def __init__(self, isbn, titulo, autor, genero, anio=None, disponible=True):
        """El atributo ISBN se utilizará como identificador único del libro."""
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.genero = genero
        self.disponible = disponible

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"ISBN: {self.isbn}\nTITULO: {self.titulo}\nAUTOR: {self.autor}\nAÑO: {self.anio}\nGENERO: {self.genero}\nDISPONIBLE: {estado}"

    def __eq__(self, libro_nuevo):
        return self.isbn == libro_nuevo.isbn

