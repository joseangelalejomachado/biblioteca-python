import json
from pathlib import Path


RUTA_USUARIOS = Path("../datos/usuarios.json")
RUTA_PRESTAMOS = Path("../datos/prestamos.json")
RUTA_LIBROS = Path("../datos/libros.json")

# Crear métodos de conversión a diccionario para cada clase (Usuario, Libro, Prestamo)

# Creamos un guardar_biblioteca que llame a método guardar_json tres veces,
# para cada tipo de objeto (usuarios, libros y préstamos)
# Dentro de cada guardar_json se llama al método de conversión

def guardar_usuarios(objeto_usuario):
    if not RUTA_USUARIOS.exists():
        return []
    with RUTA_USUARIOS.open("w", encoding="utf-8") as fichero_usuario:
        json.dump(objeto_usuario, fichero_usuario, ensure_ascii=False, indent=4)

def guardar_prestamos(objeto_prestamo):
    if not RUTA_PRESTAMOS.exists():
        return []
    with RUTA_PRESTAMOS.open("w", encoding="utf-8") as fichero_prestamo:
        json.dump(objeto_prestamo, fichero_prestamo, ensure_ascii=False, indent=4)

def guardar_libros(objeto_libro):
    if not RUTA_LIBROS:
        return []
    with RUTA_LIBROS.open("w", encoding="utf-8") as fichero_libro:
        json.dump(objeto_libro, fichero_libro, ensure_ascii=False, indent=4)

def cargar_usuarios():
    pass
    # if not RUTA_USUARIOS.exists():
        # return []
    # with RUTA_USUARIOS(encoding="utf-8") as fichero_usuario:
        # return json.load(fichero_usuario)