# Sistema de gestión de biblioteca

Aplicación de consola desarrollada en Python para gestionar libros, usuarios y préstamos de una biblioteca.

Actualmente los datos se mantienen en memoria mientras el programa está ejecutándose. La persistencia en ficheros JSON queda pendiente para una fase posterior.

## Ejecución

Desde la carpeta del proyecto, ejecutar:

```bash
python main.py
```

El programa muestra un menú de consola con las operaciones disponibles.

## Funcionalidades disponibles

- Registrar libros con ISBN, título, autor, género y año de publicación.
- Evitar libros duplicados mediante el ISBN.
- Registrar usuarios con identificador, nombre, apellidos y email.
- Evitar usuarios duplicados mediante su identificador.
- Buscar libros por ISBN, título o autor.
- Listar todos los libros.
- Listar libros disponibles o prestados.
- Realizar préstamos a usuarios registrados.
- Impedir préstamos de libros no disponibles.
- Registrar devoluciones.
- Mostrar préstamos activos.
- Mostrar los préstamos de un usuario.
- Validar datos básicos introducidos desde el menú.

## Estructura del proyecto

```text
biblioteca-python/
├── main.py
├── modelos/
│   ├── __init__.py
│   ├── libro.py
│   ├── prestamo.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   └── biblioteca.py
├── datos/
├── README.md
├── TODO.md
└── .gitignore
```

## Diseño

### `Libro`

Representa un libro de la biblioteca y contiene su ISBN, título, autor, género, año de publicación y disponibilidad.

### `Usuario`

Representa a una persona registrada en la biblioteca mediante su identificador, nombre, apellidos y email.

### `Prestamo`

Relaciona un usuario con un libro y conserva las fechas del préstamo y de la devolución. La propiedad `activo` indica si todavía no se ha registrado la devolución.

### `Biblioteca`

Gestiona las colecciones de libros, usuarios y préstamos. También aplica las reglas de negocio para registrar, buscar, prestar y devolver libros.

### `main.py`

Es el punto de entrada de la aplicación. Gestiona el menú, solicita datos y muestra los resultados al usuario, delegando la lógica en `Biblioteca`.

## Estado actual

Las opciones 1 a 8 del menú funcionan sin persistencia. La opción 9 está reservada para guardar los datos cuando se implemente el almacenamiento JSON.

## Requisitos

El proyecto utiliza únicamente módulos de la biblioteca estándar de Python, por lo que no sería necesario instalar dependencias externas.
