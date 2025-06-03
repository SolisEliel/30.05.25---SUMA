class Sumar:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def resultado(self):
        return self.num1 + self.num2

if __name__ == "__main__":
    try:
        nu1 = int(input("Ingrese su primer valor: "))
        nu2 = int(input("Ingrese su segundo valor: "))

        suma = Sumar(nu1, nu2)
        r = suma.resultado()

        print(f"El resultado es: {r}")

    except ValueError:
        print("Error: Solo se permiten números enteros.")
