# Lista de "TODOS"

## Para día 15/10/2026

- TODO: En main hasta la opción 6
- DONE: Se ha modificado comprobación a método de registro de libro para considerar cuando no se ingrese nada.
  - Al ejecutar `main.py` en opción 1 se genera un error `ValueError: invalid literal for int() with base 10: ''` al ingresar un año vacío, está intentando convertir un string vacío a entero.
  
```gitbash
=================================
    GESTION DE BIBLIOTECA   
=================================

    1. Registrar libro
    2. Registrar usuario
    3. Buscar libro
    4. Listar libros
    5. Realizar préstamo
    6. Registrar devolución
    7. Mostrar préstamos activos
    8. Mostrar préstamos de un usuario
    9. Guardar datos
    10. Salir

Seleccione una opción: 1

1 --- Registrar libro ---
Ingrese el ISBN del libro: libro1
Ingrese el título del libro: titulo1
Ingrese el autor del libro: autor1
Ingrese el género del libro: genero1
Ingrese el año de publicación del libro (opcional): 
Traceback (most recent call last):
  File "C:\Users\José Ángel\gitrepositories\DAW\biblioteca-python\main.py", line 69, in <module>
    main()
    ~~~~^^
  File "C:\Users\José Ángel\gitrepositories\DAW\biblioteca-python\main.py", line 43, in main
    registrar_libro(biblioteca)
    ~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\José Ángel\gitrepositories\DAW\biblioteca-python\main.py", line 29, in registrar_libro
    anio = int(anio_texto) if anio_texto is not None else None
           ~~~^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: ''
```
