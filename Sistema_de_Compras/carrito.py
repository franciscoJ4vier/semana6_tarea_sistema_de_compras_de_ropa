class CarritoCompras:
    def __init__(self):
        # Diccionario para almacenar productos y cantidades en el carrito
        self._items = {}

    def agregar_item(self, producto, cantidad):
        # Verifica si hay stock suficiente antes de añadir al carrito
        if producto.verificar_stock(cantidad):
            producto.disminuir_stock(cantidad)  # Disminuye el stock del producto en el inventario
            if producto in self._items:
                self._items[producto] += cantidad  # Suma cantidad si el producto ya está en el carrito
            else:
                self._items[producto] = cantidad  # Añade el producto al carrito si no está
            print(f"\nProducto añadido: {producto._nombre} x {cantidad}.")
        else:
            print(f"Stock insuficiente para {producto._nombre}. Disponibles: {producto._stock} unidades.")

    def calcular_total(self):
        # Calcula el precio total sumando el costo de cada producto en el carrito
        total = sum(item.obtener_precio() * cantidad for item, cantidad in self._items.items())
        return total

    def obtener_resumen(self):
        # Genera un resumen de la compra mostrando cada producto y cantidad
        resumen = "Resumen del carrito:\n"
        for producto, cantidad in self._items.items():
            resumen += (f"- {producto.info()} || Cantidad: {cantidad}\n")
        resumen += f"Total a pagar: ${int(self.calcular_total())}"
        return resumen

