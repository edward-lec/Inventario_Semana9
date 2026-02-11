# Informe del Programa de Gestión de Inventario

## Introducción

El presente informe describe el desarrollo y funcionamiento de un programa de gestión de inventario implementado en el lenguaje de programación Python. El sistema fue diseñado con el objetivo de permitir la administración básica de productos, incluyendo el registro, actualización, búsqueda y visualización de los mismos, a través de una interfaz de usuario en consola.

Para su desarrollo se aplicaron principios de Programación Orientada a Objetos (POO) y una organización modular del código, separando claramente las responsabilidades en distintos archivos y carpetas. Esta estructura mejora la legibilidad del programa, facilita su mantenimiento y permite una correcta escalabilidad del sistema.

---

## Desarrollo

El programa se encuentra organizado en tres componentes principales: el modelo `Producto`, el servicio `Inventario` y el archivo principal `main.py`, cada uno con una función específica dentro del sistema.

### Clase Producto

La clase `Producto` representa la entidad principal del sistema. Cada producto cuenta con los siguientes atributos: identificador (ID), nombre, cantidad y precio. Estos atributos se encuentran encapsulados mediante el uso de getters y setters, lo que permite un acceso controlado a la información y refuerza el uso de la Programación Orientada a Objetos.

Además, la clase incluye el método especial `__str__`, el cual permite mostrar la información del producto de manera clara y legible cuando se imprime en pantalla, facilitando la interacción con el usuario.

### Clase Inventario

La clase `Inventario` es la encargada de la gestión de los productos registrados. Internamente utiliza una lista como estructura principal de almacenamiento. Entre las funcionalidades implementadas se encuentran:

* Agregar nuevos productos al inventario, validando que el ID no se repita.
* Eliminar productos mediante su identificador.
* Actualizar la cantidad y/o el precio de un producto existente.
* Buscar productos por ID, retornando un único resultado.
* Buscar productos por nombre, permitiendo coincidencias parciales y sin distinguir entre mayúsculas y minúsculas.
* Listar todos los productos registrados en el inventario.

Estas operaciones garantizan un manejo correcto y organizado de la información, cumpliendo con los requisitos funcionales del sistema.

### Archivo Principal (main.py)

El archivo `main.py` actúa como punto de entrada del programa y se encarga de la interacción con el usuario mediante un menú en consola. A través de este menú, el usuario puede ejecutar todas las operaciones disponibles del sistema, como añadir, eliminar, actualizar, buscar y listar productos.

En este módulo se implementa la validación de entradas del usuario, controlando datos obligatorios y tipos numéricos, con el fin de evitar errores de ejecución. Asimismo, se integran los métodos de la clase `Inventario`, asegurando un flujo correcto del programa y una experiencia de uso clara.

Durante el desarrollo se realizaron pruebas y correcciones para garantizar que el sistema funcione correctamente en su totalidad, verificando cada una de las opciones del menú.

---

## Conclusión

El programa de gestión de inventario desarrollado cumple con los objetivos planteados y con los criterios de evaluación establecidos. Se logró implementar un sistema funcional, organizado y fácil de entender, aplicando adecuadamente los conceptos de Programación Orientada a Objetos y una estructura modular del proyecto.

Las validaciones implementadas y la verificación del funcionamiento del programa permitieron corregir errores iniciales y asegurar una ejecución estable. Además, la organización del código facilita futuras mejoras o ampliaciones del sistema.

En conclusión, el proyecto representa una solución correcta y bien estructurada para la gestión básica de inventarios, cumpliendo con los requerimientos técnicos y académicos solicitados.
