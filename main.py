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
    anio_texto = input("Ingrese el año de publicación del libro (opcional): ").strip()
    anio = int(anio_texto) if anio_texto is not None else None 

    libro = Libro(isbn, titulo, autor, genero, anio)
    biblioteca.registrar_libro(libro)
    print(f"\nLibro registrado exitosamente:\n{libro}")

def main():
    biblioteca = Biblioteca()

    while True:
        opcion = menu()

        if opcion == 1:
            print("\n1 --- Registrar libro ---")
            registrar_libro(biblioteca)
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
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