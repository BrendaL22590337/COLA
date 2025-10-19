# cola_simulador.py
# Simulación de una cola usando lista en Python

class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)
        print(f"'{item}' agregado a la cola.")

    def desencolar(self):
        if self.esta_vacia():
            print("La cola está vacía, no se puede desencolar.")
        else:
            eliminado = self.items.pop(0)
            print(f"Elemento eliminado: '{eliminado}'")

    def frente(self):
        if self.esta_vacia():
            print("La cola está vacía.")
        else:
            print(f"Elemento al frente: '{self.items[0]}'")

    def mostrar(self):
        if self.esta_vacia():
            print(" La cola está vacía.")
        else:
            print("\n--- Contenido de la cola (frente → final) ---")
            for i, elemento in enumerate(self.items):
                print(f"{i + 1}: {elemento}")
            print("---------------------------------------------")


def menu():
    cola = Cola()
    while True:
        print("\n===== MENÚ COLA =====")
        print("1. Encolar (Agregar)")
        print("2. Desencolar (Eliminar)")
        print("3. Ver frente")
        print("4. Mostrar cola")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            dato = input("Ingresa el elemento a encolar: ")
            cola.encolar(dato)
        elif opcion == '2':
            cola.desencolar()
        elif opcion == '3':
            cola.frente()
        elif opcion == '4':
            cola.mostrar()
        elif opcion == '5':
            print("Saliendo del programa de Cola...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


# Programa principal
if __name__ == "__main__":
    menu()

