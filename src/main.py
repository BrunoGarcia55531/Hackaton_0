def calculate() -> float:
    entrada = input("Escribe la operación (ej: 3 + 5) o 'c' para borrar: ")
    if entrada.lower() == 'c':
        print("Operación borrada.")
        return 0.0
    try:
        a, operador, b = entrada.split()
        a = float(a)
        b = float(b)
        if operador == '+':
            return a + b
        elif operador == '-':
            return a - b
        else:
            print("Operador no válido. Usa + o -")
            return 0.0

    except Exception:
        print("Entrada inválida. Usa el formato: número operador número (ej. 2 + 2)")
        return 0.0


if __name__ == "__main__":
    while True:
        resultado = calculate()
        print(f"Resultado: {resultado}")