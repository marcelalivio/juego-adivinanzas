import random

# Convierte un número decimal a binario (sin el prefijo '0b')
def decimal_a_binario(n):
    return bin(n)[2:]

# Convierte una cadena binaria a decimal
def binario_a_decimal(b):
    return int(b, 2)

  # Nicolas
def jugar_una_vez():
    intentos_maximos = 3
    intentos = 0
    modo = random.choice(['bin_a_dec', 'dec_a_bin'])  # Tipo de desafío
    numero = random.randint(0, 15)  # Número dentro del rango elegido

    if modo == 'bin_a_dec':
        bin_num = decimal_a_binario(numero)
        print(f"\n🤖 ¿Cuál es el número decimal equivalente a {bin_num} (binario)?")

        while intentos < intentos_maximos:
            respuesta = input(f"Intento {intentos+1}: ")

            if respuesta.isdigit() and int(respuesta) == numero:
                print("🎉 ¡Correcto! ¡Ganaste!")
                return
            else:
                print("❌ Incorrecto.")
                intentos += 1

        print(f"\n💀 Se acabaron los intentos. La respuesta correcta era {numero}.")

     # Marcela
    else:
        print(f"\n🤖 ¿Cuál es el número binario equivalente a {numero} (decimal)?")

        while intentos < intentos_maximos:
            respuesta = input(f"Intento {intentos+1}: ")

            if all(ch in '01' for ch in respuesta) and binario_a_decimal(respuesta) == numero:
                print("🎉 ¡Correcto! ¡Ganaste!")
                return
            else:
                print("❌ Incorrecto.")
                intentos += 1

        print(f"\n💀 Se acabaron los intentos. La respuesta correcta era {decimal_a_binario(numero)}.")

def juego_adivinanza():
    print("🎮 ¡Bienvenido al juego de adivinanza binaria!")

    while True:
        jugar_una_vez()
        otra_vez = input("\n¿Querés jugar otra vez? (s/n): ").lower()
        if otra_vez != 's':
            print("👋 ¡Gracias por jugar! Hasta la próxima.")
            break

if __name__ == "__main__":
    juego_adivinanza()
