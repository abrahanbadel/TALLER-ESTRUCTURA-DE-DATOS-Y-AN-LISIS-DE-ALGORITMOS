class Pila:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = []
    
    def esta_vacia(self):
        return len(self.stack) == 0
    
    def esta_llena(self):
        return len(self.stack) == self.max_size
    
    def push(self, item):
        if not self.esta_llena():
            self.stack.append(item)
        else:
            print("Error: La pila está llena.")
    
    def pop(self):
        if not self.esta_vacia():
            return self.stack.pop()
        else:
            print("Error: La pila está vacía.")
    
    def mostrar_pila(self):
        return self.stack[::-1]  # Mostrar en orden inverso

def convertir(numero, base):
    pila = Pila(32)  # Tamaño arbitrario de la pila
    simbolos_hex = "0123456789ABCDEF"
    
    print(f"\nProcedimiento para convertir el número {numero} a base {base}:")
    
    while numero > 0:
        residuo = numero % base
        print(f"{numero} dividido entre {base} da un cociente de {numero // base} y un residuo de {residuo}")
        pila.push(simbolos_hex[residuo])  # En caso de hexadecimal, convertimos el residuo
        numero = numero // base
    
    # Mostrar contenido de la pila
    print("Contenido actual de la pila (orden invertido):", pila.mostrar_pila())
    
    # Formar el número en la nueva base
    numero_convertido = ""
    while not pila.esta_vacia():
        numero_convertido += pila.pop()
    
    return numero_convertido

def menu():
    while True:
        print("\n=== Conversor de Bases Numéricas ===")
        print("1. Convertir Decimal a Binario (Base 2)")
        print("2. Convertir Decimal a Octal (Base 8)")
        print("3. Convertir Decimal a Hexadecimal (Base 16)")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '4':
            print("Saliendo del programa.")
            break
        
        if opcion not in ['1', '2', '3']:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            continue
        
        try:
            numero_decimal = int(input("Ingrese el número decimal a convertir: "))
            if numero_decimal < 0:
                print("Por favor, ingrese un número positivo.")
                continue
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")
            continue
        
        if opcion == '1':
            resultado = convertir(numero_decimal, 2)
            print(f"\nEl número en binario es: {resultado}")
        elif opcion == '2':
            resultado = convertir(numero_decimal, 8)
            print(f"\nEl número en octal es: {resultado}")
        elif opcion == '3':
            resultado = convertir(numero_decimal, 16)
            print(f"\nEl número en hexadecimal es: {resultado}")

# Llamada al menú
menu()
