from producto import Camisa, Pantalon, Zapato
from carrito import CarritoCompras

class TiendaVirtual:
    def __init__(self):
        # Crea un catálogo de productos disponibles en la tienda
        self._inventario = [
            Camisa("Camisa de Algodón", 20.00, "M", "Algodón", "Clásico", 10),
            Pantalon("Pantalón de Mezclilla", 30.00, "L", "Denim", "Corto", 5),
            Zapato("Zapato de Cuero", 50.00, "42", "Cuero", 7),
        ]

    def ver_productos(self):
        # Muestra el inventario actual de la tienda
        print("\nCatálogo de Productos:\n")
        for idx, producto in enumerate(self._inventario, 1):
            print(f"{idx}. {producto.info()}\n")

    def iniciar_compra(self):
        # Crea un nuevo carrito y permite al usuario agregar productos
        carrito = CarritoCompras()
        while True:
            self.ver_productos()  # Muestra los productos para seleccionar
            seleccion = input("Seleccione el número de producto para agregar al carrito (o 'q' para finalizar): ")
            if seleccion.lower() == 'q':
                break  # Sale del bucle si el usuario decide finalizar
            try:
                indice = int(seleccion) - 1
                if 0 <= indice < len(self._inventario):
                    cantidad = int(input(f"Ingrese la cantidad deseada de '{self._inventario[indice]._nombre}': "))
                    carrito.agregar_item(self._inventario[indice], cantidad)  # Agrega el producto seleccionado
                else:
                    print("Opción no válida. Intente de nuevo.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")

        # Muestra el resumen de la compra al final
        print("\nResumen de la compra:\n")
        print(carrito.obtener_resumen())

