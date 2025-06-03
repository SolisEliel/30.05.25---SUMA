import tkinter as tk
from tkinter import messagebox

class Sumar:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def resultado(self):
        return self.num1 + self.num2

def calcular_suma():
    try:
        n1 = int(entrada1.get())
        n2 = int(entrada2.get())
        suma = Sumar(n1, n2)
        resultado = suma.resultado()
        resultado_label.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa solo números enteros.")
        resultado_label.config(text="")


ventana = tk.Tk()
ventana.title("Suma de dos números")
ventana.geometry("300x200")
ventana.config(bg="#AEBED9")


et1 = tk.Label(ventana, text="Primer número:", bg="#AEBED9")
et1.pack(pady=5)

entrada1 = tk.Entry(ventana)
entrada1.pack()

et2 = tk.Label(ventana, text="Segundo número:", bg="#AEBED9")
et2.pack(pady=5)

entrada2 = tk.Entry(ventana)
entrada2.pack()

boton = tk.Button(ventana, text="Calcular suma", command=calcular_suma)
boton.pack(pady=10)

resultado_label = tk.Label(ventana, text="", font=("Arial", 12), bg="#AEBED9")
resultado_label.pack()


ventana.mainloop()
