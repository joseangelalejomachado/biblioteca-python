# Propuesta de JIHuertas
import json
from modelos.libro import Libro
from modelos.usuario import Usuario
from modelos.prestamo import Prestamo
from servicios.biblioteca import Biblioteca
from datetime import date

FICHERO_LIBROS = "datos/libros_prueba.json"
FICHERO_USUARIOS = "datos/usuarios_prueba.json"
FICHERO_PRESTAMOS = "datos/prestamos_prueba.json"

def guarda_json(nombre_fichero, datos):
    with open(nombre_fichero, "w", encoding="utf-8") as fichero:
        json.dump(datos, fichero, ensure_ascii=False, indent=4)

# Guardamos todo lo que hay en biblioteca en tres ficheros.
# Uno para libros, otro para prestamos, otro para usuarios
def guardar_datos(biblioteca):
    libros = [libro.__dict__ for libro in biblioteca.libros]
    # Vamos a usar __dict__ porque libro tiene atributos
    # simples, no contiene diccionarios u otras estructuras que
    # agreguen complejidad
    #for libro in biblioteca.libros:
    #    libros.append(libro.__dict__)

    guarda_json(FICHERO_LIBROS, libros)

    usuarios = []
    for usuario in biblioteca.usuarios:
        usuarios.append(usuario.to_dict())

    guarda_json(FICHERO_USUARIOS, usuarios)

    prestamos = []
    for prestamo in biblioteca.prestamos:
        prestamos.append(prestamo.to_dict())
    guarda_json(FICHERO_PRESTAMOS, prestamos)

def cargar_datos(biblioteca: Biblioteca):
    with open(FICHERO_LIBROS, "r", encoding="utf-8") as fichero:
        libros = json.load(fichero)

    for libro in libros:
        libro_obj = Libro(libro["isbn"], libro["titulo"], libro["autor"], libro["genero"], libro["anio"], libro["disponible"])
        biblioteca.libros.append(libro_obj)

    with open(FICHERO_USUARIOS, "r", encoding="utf-8") as fichero:
        usuarios = json.load(fichero)

    for usuario in usuarios:
        usuario_obj= Usuario(usuario["id_usuario"], usuario["nombre"], usuario["apellidos"], usuario["email"])
        biblioteca.usuarios.append(usuario_obj)

    with open(FICHERO_PRESTAMOS, "r", encoding="utf-8") as fichero:
        prestamos = json.load(fichero)

    for prestamo in prestamos:
        usuario_obj = biblioteca.buscar_usuario(prestamo["usuario"])
        if usuario_obj is None:
            raise ValueError(f"Usuario con ID {prestamo['usuario']} no encontrado.")
            return
        libro_obj = biblioteca.buscar_libro_por_isbn(prestamo["libro"])
        if libro_obj is None:
            raise ValueError(f"Lbro con ISBN {prestamo['libro']} no encontrado.")
            return
        fecha_prestamo = date.fromisoformat(prestamo["fecha_prestamo"])
        fecha_devolucion = date.fromisoformat(prestamo["fecha_devolucion"]) if prestamo["fecha_devolucion"] is not None else None
        prestamo_obj = Prestamo(usuario_obj, libro_obj, fecha_prestamo, fecha_devolucion)
        biblioteca.prestamos.append(prestamo_obj)


