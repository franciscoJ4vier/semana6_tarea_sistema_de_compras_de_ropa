class Producto:
    def __init__(self, nombre, precio, stock):
        # Inicializa los datos del producto
        self._nombre = nombre
        self._precio = precio
        self._stock = stock

    def obtener_precio(self):
        # Devuelve el precio del producto
        return self._precio

    def info(self):
        # Muestra información breve del producto
        return f"Producto: {self._nombre} || Precio: ${int(self._precio)} || Stock: {self._stock}"

    def verificar_stock(self, cantidad):
        # Confirma si la cantidad deseada está disponible en stock
        return self._stock >= cantidad

    def disminuir_stock(self, cantidad):
        # Resta la cantidad indicada del stock si es posible
        if self.verificar_stock(cantidad):
            self._stock -= cantidad
            return True
        return False


class Ropa(Producto):
    def __init__(self, nombre, precio, talla, material, stock):
        # Llama al constructor de Producto y añade detalles específicos de ropa
        super().__init__(nombre, precio, stock)
        self._talla = talla
        self._material = material

    def info(self):
        # Incluye detalles adicionales de ropa
        return (f"{super().info()} || Talla: {self._talla} || Material: {self._material}")


class Camisa(Ropa):
    def __init__(self, nombre, precio, talla, material, tipo_cuello, stock):
        # Inicializa los atributos para una camisa
        super().__init__(nombre, precio, talla, material, stock)
        self._tipo_cuello = tipo_cuello

    def info(self):
        # Muestra información específica de la camisa
        return (f"{super().info()} || Tipo de Cuello: {self._tipo_cuello}")


class Pantalon(Ropa):
    def __init__(self, nombre, precio, talla, material, largo, stock):
        # Inicializa los atributos para un pantalón
        super().__init__(nombre, precio, talla, material, stock)
        self._largo = largo

    def info(self):
        # Muestra información específica del pantalón
        return (f"{super().info()} || Largo: {self._largo}")


class Zapato(Ropa):
    def __init__(self, nombre, precio, talla, material, stock):
        # Inicializa los atributos para un zapato
        super().__init__(nombre, precio, talla, material, stock)

    def info(self):
        # Muestra información específica del zapato
        return f"{super().info()}"
