def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def calculate() -> float:
    entrada = input("Escribe la operación (ej: 3 + 5 o 5 - 2) o 'c' para borrar: ")

    if entrada.lower() == 'c':
        print("Operación borrada.")
        return 0.0

    try:
        partes = entrada.split()
        if len(partes) != 3:
            raise ValueError("Formato incorrecto. Usa: número operador número")

        a, operador, b = partes
        a = float(a)
        b = float(b)

        if operador == '+':
            return suma(a, b)
        elif operador == '-':
            return resta(a, b)
        else:
            raise ValueError("Operador no válido. Solo se permite + o -")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception:
        print("Error inesperado. Intenta de nuevo.")
    return 0.0

if _name_ == "_main_":
    while True:
        resultado = calculate()
        print(f"Resultado: {resultado}")