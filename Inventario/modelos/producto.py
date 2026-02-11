class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Atributos del producto
        self._id = id_producto      # ID único del producto
        self._nombre = nombre       # Nombre del producto
        self._cantidad = cantidad   # Cantidad disponible
        self._precio = precio       # Precio del producto

    # GETTERS

    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # SETTERS

    def set_id(self, id_producto):
        # Setter del ID (incluido para cumplir el enunciado)
        self._id = id_producto

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    # Representación en texto del producto
    def __str__(self):
        return (
            f"ID: {self._id} | "
            f"Nombre: {self._nombre} | "
            f"Cantidad: {self._cantidad} | "
            f"Precio: ${self._precio:.2f}"
        )
