# Gestor de usuarios


## Descripción
El proyecto permite realizar acciones como ser:
- Agregar usuario.
- Eliminar usuario.
- Ver usuarios.
- Ver todos los usuarios.


## Requisitos Previos

- Python 3.11 o superior


## Instalación y Configuración
```sh
git clone https://github.com/tu-usuario/nombre-del-repositorio.git
cd nombre-del-repositorio
```

## Uso
python main.py


## Observaciones de Uso
La version final del proyecto fue programada para que imprima un ejemplo al momento de ejecutar `main.py`, si se desea utilizar el programa de una forma mas dinamica es conveniente agregar un menu de opciones en dicho archivo.



## Principios SOLID
- **Single Responsibility Principle (SRP)**: Cada una de las siguientes clases tiene una sola responsabilidad.

    * Usuario (en modelos/usuario.py) gestiona los datos del usuario.
    * DaoUsuario (en capa_datos/dao_usuario.py) gestiona la persistencia.
    * ServicioUsuario (en capa_negocio/servicio_usuario.py) gestiona la lógica de negocio.
    * ControladorUsuario (en capa_presentacion/controlador_usuario.py) gestiona la presentación."


- **Open/Closed Principle (OCP)**: Las clases están abiertas para extensión pero cerradas para modificación.

    * Podemos extender la clase DaoUsuario para añadir nuevas funcionalidades sin modificar la clase existente.

- **Liskov Substitution Principle (LSP)**:

    * El principio LSP está implícitamente respetado ya que nuestras clases están diseñadas de manera que cualquier instancia de Usuario puede ser utilizada sin alterar el comportamiento esperado.

- **Interface Segregation Principle (ISP)**:

    * Nuestras interfaces están definidas de manera que las clases no están obligadas a implementar métodos que no utilizan. Por ejemplo, DaoUsuario solo implementa métodos relevantes para la persistencia de usuarios.

- **Dependency Inversion Principle (DIP)**: Las dependencias se manejan a través de la inyección de dependencias.

    * ControladorUsuario depende de ServicioUsuario y ServicioUsuario depende de DaoUsuario, y estas dependencias se inyectan a través de los constructores.



## Patrones de Diseño
- **Patrón Creacional(Factory Method)**: Implementado en `servicio_usuario.py`, el método agregar_usuario en ServicioUsuario actúa como un Factory Method, creando instancias de Usuario.

- **Patrón Estructural: (Dependency Injection)**: Las dependencias se inyectan a través de los constructores, permitiendo que las clases dependan de abstracciones en lugar de concretas. Por ejemplo, ServicioUsuario inyecta DaoUsuario.

- **Patrón de Comportamiento: (Command)**: Cada operación en ControladorUsuario (como agregar_usuario, ver_usuario) puede considerarse como un comando que se ejecuta para manipular los datos.



## Arquitectura del Proyecto

- **Capa de Presentacion**: Gestiona la interacción con el usuario. Se encuentra en `capa_presentacion/controlador_usuario.py`
    
    - *Responsabilidades*:
        * Agregar Usuario: Recoge los datos del usuario desde la entrada y llama al servicio de negocio para agregar un nuevo usuario.
        * Ver Usuario: Solicita información de un usuario específico al servicio de negocio y muestra los detalles al usuario.
        * Ver Todos los Usuarios: Solicita todos los usuarios al servicio de negocio y los muestra al usuario.



- **Capa de Negocio**: Contiene la lógica de negocio. Se encuentra en `capa_negocio/servicio_usuario.py`

    - *Responsabilidades*:
        * Agregar Usuario: Crea una instancia del usuario y la pasa al DAO (Data Access Object) para guardarla.
        * Obtener Usuario: Solicita al DAO la información de un usuario específico.
        * Obtener Todos los Usuarios: Solicita al DAO la lista de todos los usuarios.



- **Capa de Datos**: Gestiona el almacenamiento y recuperación de datos. Se encuentra en `capa_datos/dao_usuario.py`
    
    - *Responsabilidades*:
        * Agregar Usuario: Crea una instancia del usuario y la pasa al DAO (Data Access Object) para guardarla.
        * Obtener Usuario: Solicita al DAO la información de un usuario específico.
        * Obtener Todos los Usuarios: Solicita al DAO la lista de todos los usuarios.