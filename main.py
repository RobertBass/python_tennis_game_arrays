"""G11-TLL-01

INTEGRANTES:
ANGULO CUERO EVELIN NASLIN
BRAVO TORRES VICTOR ROBERTO
GARCIA PACHECO GEORGE WASHINGTON
LOOR DELGADO TERESA MONSERRATE
SANCHEZ VINCES FABRICIO ALEXANDER

TALLER DE ORDENAMIENTO Y OPTIMIZACION

EL TALLER CONSISTE EN LA CREACION DE UNA SIMULACION DE JUEGO DE PING PONG UTILIZANDO UNA MATRIZ DE 3X5

DE ACUERDO A LOS REQUERIMIENTOS, LAS COLUMNAS REPRESENTAN EL AVANCE DE LA PELOTA EN EL TABLERO, MIENTRAS QUE
LAS FILAS REPRESENTAN LA TRAYECTORIA.

EL JUGADOR QUE LANZA LA PELOTA, INICIA DESDE UNA FILA AL AZAR EN LA COLUMNA UNO Y ES REPRESENTADO POR EL VALOR 1
LUEGO AVANZA HASTA LA COLUMNA 2, EN EL CUAL SE SELECCIONA AL AZAR UNA DE LAS TRES FILAS PARA EMPEZAR A REPRESENTAR
LA TRAYECTORIA DE LA PELOTA Y ASI SUCEDERA HASTA LA COLUMNA 4.
LA COLUMNA 5 QUEDA EXCLUSIVAMENTE PARA EL JUGADOR 2, EL CUAL REPRESENTA A LA RAQUETA QUE TRATARA DE BLOQUEAR EL TIRO.
LA RAQUETA ESTA REPRESENTADA POR EL VALOR 0.

EL GANADOR SE DETERMINA COMPARANDO LA POSICION (FILA) EN LA COLUMNA 4 DEL JUGADOR 1 Y LA POSICION (FILA) DEL JUGADOR 2
EN LA COLUMNA 5. SI COINCIDE LA FILA DE AMBOS JUGADORES, EL GANADOR SERA EL JUGADOR 2, CASO CONTRARIO EL JUGADOR 1.

EL JUEGO HA SIDO DISENADO CON PROGRAMACION MODULAR:
- DENTRO DE LA CARPETA MODULES ENCONTRAREMOS LOS ARCHIVOS QUE REPRESENTAN LAS BASES Y MECANISMOS DEL JUEGO
  - array.py: CREACION DE LA MATRIZ
  - services.py: LOS METODOS NECESARIOS PARA EL DESARROLLO DEL JUEGO
  - game.py: IMPLEMENTACION DEL JUEGO CON EL ARREGLO Y LOS METODOS
- EL ARCHIVO main.py ES EL ENCARGADO DE LA EJECUCION DEL JUEGO.

"""


# MODULO DE EJECUCION DEL JUEGO


from modules.game import *

# EJECUTABLE DEL JUEGO
if __name__ == "__main__":
    jugar()