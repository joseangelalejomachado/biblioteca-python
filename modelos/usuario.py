class Usuario:
    def __init__(self, id_usuario, nombre, apellidos, email):
        self.id = id_usuario
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

    def __str__(self):
        return f"ID: {self.id}\nNombre: {self.nombre}\nApellidos: {self.apellidos}\nEmail: {self.email}"

    def __repr__(self):
        return (
            f"Usuario(id={self.id!r}, "
            f"nombre={self.nombre!r}, "
            f"apellidos={self.apellidos!r}, "
            f"email={self.email!r})"
        )

    def to_dict(self):
        return {
            "id_usuario": self.id,
            "nombre": self.nombre,
            "apellidos": self.apellidos,
            "email": self.email
        }