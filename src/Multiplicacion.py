def multiplicacion():
    while True:
        try:
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            resultado = a * b
            print(f"El resultado de multiplicar {a} × {b} es: {resultado}")
            break
        except ValueError:
            print("Error: Debes ingresar valores numéricos. Intenta nuevamente.")

multiplicacion()
