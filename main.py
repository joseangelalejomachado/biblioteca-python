from modelos.libro import Libro
from modelos.prestamo import Prestamo
from modelos.usuario import Usuario
from servicios.biblioteca import Biblioteca

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
    print(f"    0. Salir")
    opcion = int(input("\nSeleccione una opción: "))
    return opcion

def registrar_libro(biblioteca):
    isbn = input("Ingrese el ISBN del libro: ").strip()
    titulo = input("Ingrese el título del libro: ").strip()
    autor = input("Ingrese el autor del libro: ").strip()
    genero = input("Ingrese el género del libro: ").strip()
    anio_texto = input("Ingrese el año de publicación del libro como numero (opcional): ").strip()
    
    anio = int(anio_texto) if anio_texto != "" else None 

    libro = Libro(isbn, titulo, autor, genero, anio)
    registrado = biblioteca.registrar_libro(libro)
    if registrado:
        print(f"\nLibro registrado exitosamente:\n{libro}")
    else:
        print(f"Ya existe un libro con el ISBN {isbn}.")

def registrar_usuario(biblioteca):
    id_usuario = input("Ingrese el ID del usuario: ").strip()
    nombre = input("Ingrese el nombre: ").strip()
    apellidos = input("Ingrese los apellidos: ").strip()
    email = input("Ingrese el email: ").strip()

    usuario = Usuario(id_usuario, nombre, apellidos, email)
    registrado = biblioteca.registrar_usuario(usuario)
    if registrado:
        print(f"\nUsuario registrado exitosamente:\n{usuario}")
    else:
        print("---------")
        print(f"Ya existe un usuario con el ID {id_usuario}.")

def listar_libros(biblioteca):
    libros = biblioteca.listar_libros()
    if libros:
        print("\nLIBROS REGISTRADOS:")
        for libro in libros:
            print(libro)
            print("---------")
    else:
        print("No hay libros registrados.")

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

def realizar_prestamo(biblioteca):
    id_usuario = input("Ingrese el ID del usuario: ").strip()
    isbn = input("Ingrese el ISBN del libro: ").strip()

    if not id_usuario or not isbn:
        print("El ID del usuario y el ISBN son obligatorios.")
        return

    usuario = biblioteca.buscar_usuario(id_usuario)
    if usuario is None:
        print("El usuario no existe.")
        return

    libro = biblioteca.buscar_libro_por_isbn(isbn)
    if libro is None:
        print("El libro no existe.")
        return

    if not libro.disponible:
        print("El libro no está disponible.")
        return

    realizado = biblioteca.realizar_prestamo(usuario, libro)

    if realizado:
        print("Préstamo realizado correctamente.")
    else:
        print("No se pudo realizar el préstamo.")

def main():
    biblioteca = Biblioteca()

    while True:
        opcion = menu()

        if opcion == 1:
            print("\n1. Registrar libro ---")
            registrar_libro(biblioteca)
        elif opcion == 2:
            print(f"\n2. Registrar usuario")
            registrar_usuario(biblioteca)
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
        elif opcion == 7:
            pass
        elif opcion == 8:
            pass
        elif opcion == 9:
            pass
        elif opcion == 0:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
        


if __name__ == "__main__":
    main()