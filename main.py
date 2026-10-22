from modelos.libro import Libro
from modelos.usuario import Usuario
from servicios.biblioteca import Biblioteca
from servicios.guarda import guardar_datos
from servicios.guarda import cargar_datos

# ENTRADA Y VALIDACIÓN
def pedir_texto_obligatorio(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Este campo no puede estar vacío.")

def pedir_anio():
    while True:
        texto = input("Año de publicación: ").strip()

        try:
            anio = int(texto)
            if anio > 0:
                return anio
            print("El año debe ser positivo.")
        except ValueError:
            print("El año debe ser un número entero.")

def pedir_email():
    while True:
        email = pedir_texto_obligatorio("Ingrese el email: ")

        partes = email.split("@")

        if len(partes) == 2 and partes[0] and "." in partes[1]:
            return email

        print("Introduzca un email válido.")

def menu():
    print(f"\n=================================")
    print(f"    GESTION DE BIBLIOTECA   ")
    print(f"=================================\n")
    print(f"    1. Registrar libro")
    print(f"    2. Registrar usuario")
    print(f"    3. Buscar libro")
    print(f"    4. Listar libros")
    print(f"    5. Realizar préstamo")
    print(f"    6. Registrar devolución")
    print(f"    7. Mostrar préstamos activos")
    print(f"    8. Mostrar préstamos de un usuario")
    print(f"    9. Guardar datos")
    print(f"    10. Mostrar estadisticas")
    print(f"    0. Salir")
    while True:
        try:
            opcion = int(input("\nSeleccione una opción: "))
            if 0 <= opcion <= 10:
                return opcion
            print("Opción inválida. Introduzca un número del 0 al 10.")
        except ValueError:
            print("Opción inválida. Introduzca un número del 0 al 10.")

# LIBROS
def registrar_libro(biblioteca):
    isbn = pedir_texto_obligatorio("Ingrese el ISBN del libro: ")
    titulo = pedir_texto_obligatorio("Ingrese el título del libro: ")
    autor = pedir_texto_obligatorio("Ingrese el autor del libro: ")
    genero = pedir_texto_obligatorio("Ingrese el género del libro: ")
    anio = pedir_anio()

    libro = Libro(isbn, titulo, autor, genero, anio)
    registrado = biblioteca.registrar_libro(libro)
    if registrado:
        print(f"\nLibro registrado exitosamente:\n{libro}")
    else:
        print(f"Ya existe un libro con el ISBN {isbn}.")

def registrar_usuario(biblioteca):
    id_usuario = pedir_texto_obligatorio("Ingrese el ID del usuario: ")
    nombre = pedir_texto_obligatorio("Ingrese el nombre: ")
    apellidos = pedir_texto_obligatorio("Ingrese los apellidos: ")
    email = pedir_email()

    usuario = Usuario(id_usuario, nombre, apellidos, email)
    registrado = biblioteca.registrar_usuario(usuario)
    if registrado:
        print(f"\nUsuario registrado exitosamente:\n{usuario}")
    else:
        print("---------")
        print(f"Ya existe un usuario con el ID {id_usuario}.")

def listar_usuarios(biblioteca):
    usuarios = biblioteca.listar_usuarios()

    if not usuarios:
        print("No hay usuarios registrados.")
        return

    print("\nUSUARIOS REGISTRADOS:")
    for usuario in usuarios:
        print(usuario)
        print("---------")

def gestionar_usuarios(biblioteca):
    while True:
        print("\n1. Registrar usuario")
        print("2. Listar usuarios")
        print("0. Volver")
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            registrar_usuario(biblioteca)
        elif opcion == "2":
            listar_usuarios(biblioteca)
        elif opcion == "0":
            break
        else:
            print("Opción no válida.")

def listar_libros(biblioteca):
    while True:
        print("\nLISTAR LIBROS")
        print("1. Mostrar todos")
        print("2. Mostrar disponibles")
        print("3. Mostrar prestados")
        print("0. Volver")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            libros = biblioteca.listar_libros()
        elif opcion == "2":
            libros = biblioteca.listar_libros_disponibles()
        elif opcion == "3":
            libros = biblioteca.listar_libros_prestados()
        elif opcion == "0":
            break
        else:
            print("Opción no válida.")
            continue

        mostrar_resultados(libros)

def buscar_libro(biblioteca):
    while True:
        print("1. Buscar por ISBN")
        print("2. Buscar por título")
        print("3. Buscar por autor")
        print("0. Volver al menú principal")
        opcion = input("Selecciona el tipo de búsqueda: ").strip()
        if opcion == "1":
            isbn = input("Ingrese el ISBN: ").strip()
            if not isbn:
                print("El ISBN no puede estar vacío.")
            else:
                libro = biblioteca.buscar_libro_por_isbn(isbn)
                if libro:
                    print(f"\nLibro encontrado:\n{libro}")
                else:
                    print(f"No se encontró un libro con el ISBN {isbn}.")
        elif opcion == "2":
            titulo = input("Ingrese el título: ").strip()
            if not titulo:
                print("El título no puede estar vacío.")
            else:
                libros = biblioteca.buscar_libros_por_titulo(titulo)
                mostrar_resultados(libros)
        elif opcion == "3":
            autor = input("Ingrese el autor: ").strip()
            if not autor:
                print("El autor no puede estar vacío.")
            else:
                libros = biblioteca.buscar_libros_por_autor(autor)
                mostrar_resultados(libros)
        elif opcion == "0":
            print("Volviendo al menú principal...")
            break
        else:
            print("Tipo de búsqueda no válida. Intentalo de nuevo.")

def mostrar_resultados(libros):
    """Función auxiliar para mostrar resultados de búsquedas en 'buscar_libro(biblioteca)'"""
    if libros:
        for libro in libros:
            print(f"\n{libro}")
    else:
        print("No se encontraron libros.")

# PRÉSTAMOS
def realizar_prestamo(biblioteca):
    id_usuario = pedir_texto_obligatorio("ID del usuario: ")
    isbn = pedir_texto_obligatorio("ISBN del libro: ")

    usuario = biblioteca.buscar_usuario(id_usuario)
    libro = biblioteca.buscar_libro_por_isbn(isbn)

    if usuario is None:
        print("El usuario no existe.")
        return

    if libro is None:
        print("El libro no existe.")
        return

    if biblioteca.realizar_prestamo(usuario, libro):
        print("Préstamo realizado correctamente.")
    else:
        print("No se puede realizar el préstamo.")

def registrar_devolucion(biblioteca):
    isbn = pedir_texto_obligatorio("ISBN del libro: ")

    libro = biblioteca.buscar_libro_por_isbn(isbn)

    if libro is None:
        print("El libro no existe.")
    elif libro.disponible:
        print("El libro no tiene un préstamo activo.")
    elif biblioteca.registrar_devolucion(isbn):
        print("Devolución registrada correctamente.")
    else:
        print("No se pudo registrar la devolución.")

def mostrar_prestamos_activos(biblioteca):
    prestamos = biblioteca.listar_prestamos_activos()

    if not prestamos:
        print("No hay préstamos activos.")
        return

    print("\nPRÉSTAMOS ACTIVOS:")
    for prestamo in prestamos:
        print(prestamo)
        print("---------")

def mostrar_prestamos_de_usuario(biblioteca):
    id_usuario = pedir_texto_obligatorio("ID del usuario: ")

    usuario = biblioteca.buscar_usuario(id_usuario)

    if usuario is None:
        print("El usuario no existe.")
        return

    prestamos = biblioteca.listar_prestamos_de_usuario(id_usuario)

    if not prestamos:
        print("El usuario no tiene préstamos.")
        return

    print(f"\nPRÉSTAMOS DE {usuario.nombre} {usuario.apellidos}:")
    for prestamo in prestamos:
        print(prestamo)
        print("---------")

def mostrar_estadisticas(biblioteca):
    biblioteca.mostrar_estadisticas()

# PROGRAMA PRINCIPAL
def main():
    biblioteca = Biblioteca()

    cargar_datos(biblioteca)
    while True:
        opcion = menu()

        if opcion == 1:
            print("\n1. Registrar libro ---")
            registrar_libro(biblioteca)
        elif opcion == 2:
            gestionar_usuarios(biblioteca)
        elif opcion == 3:
            print(f"\n3. Buscar libro")
            buscar_libro(biblioteca)
        elif opcion == 4:
            print(f"\n4. Listar libros")
            listar_libros(biblioteca)
        elif opcion == 5:
            print(f"\n5. Realizar préstamo")
            realizar_prestamo(biblioteca)
        elif opcion == 6:
            print(f"\n6. Registrar devolución")
            registrar_devolucion(biblioteca)
        elif opcion == 7:
            print("\n7. Mostrando préstamos activos...")
            mostrar_prestamos_activos(biblioteca)
        elif opcion == 8:
            print("\n8. Mostrando préstamos de un usuario...")
            mostrar_prestamos_de_usuario(biblioteca)
        elif opcion == 9:
            print("Guardando datos...")
            guardar_datos(biblioteca)
        elif opcion == 10:
            print("Mostrando estadísticas: ")
            mostrar_estadisticas(biblioteca)
        elif opcion == 0:
            print("Saliendo del programa...")
            #biblioteca.guardar_usuarios()
            guardar_datos(biblioteca)
            break
        else:
            print("Opción inválida. Intente nuevamente.")
        


if __name__ == "__main__":
    main()