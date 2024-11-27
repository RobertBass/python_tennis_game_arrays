# MODULO PARA LA IMPLEMENTACION DEL JUEGO CON LAS FUNCIONALIDADES CREADAS EN EL MODULO SERVICES

from modules.services import *
from modules.array import *

# FUNCION PARA INICIAR EL JUEGO
def jugar():
    while True:
        print("\n\n")
        print("***********************************************************")
        print("¡BIENVENIDO AL JUEGO DE PING PONG CON MATRICES!")
        print("***********************************************************")
        print("\n")
        print("MATRIZ INICIAL:")
        matriz = crear_matriz()
        mostrar_matriz(matriz)

        # Turno del jugador 1 (item '1')
        juego(matriz, 1, '1')

        # Turno del jugador 2 (item '0')
        juego(matriz, 2, '0')

        # Verificar el resultado
        ganador = verificar_ganador(matriz)
        if ganador == 1:
            print("¡EL JUGADOR 1 GANA LA PARTIDA!")
        elif ganador == 2:
            print("¡EL JUGADOR 2 GANA LA PARTIDA!")

        # PREGUNTAR SI DESEAN JUGAR DE NUEVO
        while True:
            repetir = input("¿QUIERES VOLVER A JUGAR? (s/n): ").strip().lower()
            if repetir == 's':
                break  # REINICIAR EL JUEGO
            elif repetir == 'n':
                print("¡GRACIAS POR JUGAR. VUELVE PRONTO")
                return  # FIN DEL JUEGO
            else:
                print("OPCION NO VALIDA. ESCRIBE 's' o 'n'.")