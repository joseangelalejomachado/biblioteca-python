from datetime import date

class Prestamo:
    def __init__(self, usuario, libro, fecha_prestamo=None, fecha_devolucion=None):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = (fecha_prestamo if fecha_prestamo is not None else date.today())
        self.fecha_devolucion = fecha_devolucion
    
    @property
    def activo(self):   # El préstamo estará activo cuando no hay fecha de devolución pero sí fecha de prestamo
        return self.fecha_devolucion is None and self.fecha_prestamo is not None
    
    def __str__(self):
        estado = "Activo" if self.activo else f"Devuelto: {self.fecha_devolucion}"
        return f"Usuario: {self.usuario}\nLibro: {self.libro}\nFecha del prestamo: {self.fecha_prestamo}\nFecha de devolucion: {estado}"

    def to_dict(self):
        return {
            "usuario": self.usuario.id,
            "libro": self.libro.isbn,
            "fecha_prestamo": self.fecha_prestamo.isoformat(),
            "fecha_devolucion": date.isoformat(self.fecha_devolucion) if self.fecha_devolucion else None
        }