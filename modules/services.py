# ESTE MODULO DETERMINA LAS FUNCIONES CON LAS CUALES SE DESARROLLA EL JUEGO

import random
import time


# FUNCION PARA IMPRIMIR LA MATRIZ
def mostrar_matriz(matriz):
    print("   1   2   3   4   5")
    print("  --- --- --- --- ---")
    for i, fila in enumerate(matriz):
        fila_str = " | ".join(fila)
        print(f"{i + 1}| {fila_str} |")
        print("  --- --- --- --- ---")
    print()
    time.sleep(1)   # ANIMACION DE RETARDO DE 1 SEGUNDO


# FUNCION QUE DETERMINA LA SECUENCIA DEL JUEGO
def juego(matriz, jugador, item):
    if jugador == 1:
        # JUGADOR 1 COLOCA SU ITEM (1) EN LAS COLUMNA 1 AL 4
        for columna in range(4):
            fila = random.randint(0, 2)  #ELIGE UNA FILA AL AZAR
            matriz[fila][columna] = item   #COLOCA EL ITEM (1) EN LA POSICION
            print(f"JUGADOR 1 - TURNO {columna+1}")
            mostrar_matriz(matriz)
            time.sleep(1)
    elif jugador == 2:
        # JUGADOR 2 COLOCA SU ITEM (0) EN LA COLUMNA 5
        for columna in range(4, 5):
            fila = random.randint(0, 2)   #ELIGE UNA FILA AL AZAR
            matriz[fila][columna] = item   #COLOCA EL ITEM (1) EN LA POSICION
            time.sleep(1)
            print(f"JUGADOR 2 - TURNO {columna + 1}")
            mostrar_matriz(matriz)


# FUNCIONES QUE DETERMINAN AL GANADOR DEL JUEGO

# FUNCION PARA DETERMINAR EL INDICE DE LAS FILAS DE LAS COLUMNAS 4 Y 5
def buscar_indice_fila(matriz, indice_columna, valor):
    indice = -1   # SE INICIALIZA EN -1 PARA INDICAR QUE NO EXISTE EL VALOR EN LA MATRIZ

    for i, fila in enumerate(matriz):
        # CONDICIONAL PARA QUE BUSQUE EL VALOR (1 O 0) EN LA FILA i DE LA COLUMNA INDICADA EN indice_columna
        if fila[indice_columna] == valor:
            indice = i   #ASIGNA EL NUMERO DE FILA DONDE SE ENCUENTRA UBICADO EL 1 O EL 0
            break
    return indice


# FUNCION PARA DETERMINAR AL GANADOR DEL JUEGO
def verificar_ganador(matriz):
    # SE BUSCA EL INDICE DE LA FILA DE LA COLUMNA 4 DONDE SE ENCUENTRA EL 1
    jugador1 = buscar_indice_fila(matriz, 3, '1')

    # SE BUSCA EL INDICE DE LA FILA DE LA COLUMNA 4 DONDE SE ENCUENTRA EL 0
    jugador2 = buscar_indice_fila(matriz, 4, '0')

    # SI EL INDICE DEL JUGADOR 1 Y EL 2 COINCIDE, GANA EL JUGADOR 2 PORQUE BLOQUEO EL TIRO, SINO GANA EL JUGADOR 1
    if jugador1 == jugador2: return 2
    else: return 1