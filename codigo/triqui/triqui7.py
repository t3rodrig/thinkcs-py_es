# -*- coding: utf-8 -*-
# Triqui

def crear():
    """ Crea una matrix 3x3 vacia"""
    m =  [ [' ',' ',' '],
           [' ',' ',' '],
           [' ',' ',' '] ]
    return m

def imprimir(tablero):
    """ Imprime el tablero de juego"""
    for i in range(3):
        print('|',end='')
        for j in range(3):
            print(tablero[i][j],end='') 
        print('|')

def ganaDiagonal1(jugador,tablero):
    """Chequea si el jugador gana en la diagonal 1"""
    for i in range(3):
        if tablero[i][i]!=jugador:
            return False
    return True

def ganaDiagonal2(jugador,tablero):
    """Chequea si el jugador gana en la diagonal 2"""
    for i in range(3):
        if tablero[i][2-i]!=jugador:
            return False
    return True

def ganaFila(fila,jugador,tablero):
    """Chequea si el jugador gana en la fila dada"""
    for i in range(3):
        if tablero[fila][i]!=jugador:
            return False
    return True

def ganaHorizontal(jugador,tablero):
    """ Chequea todas las filas """
    for i in range(3):
        if ganaFila(i,jugador,tablero):
            return True
    return False


def ganaColumna(columna,jugador,tablero):
    """Chequea si el jugador gana en la columna dada"""
    for i in range(3):
        if tablero[i][columna]!=jugador:
            return False
    return True

def ganaVertical(jugador,tablero):
    """ Chequea todas las columnas """
    for i in range(3):
        if ganaColumna(i,jugador,tablero):
            return True
    return False

def valido(n):
    return 0<=n<=2

def jugar(jugador,tablero):
    """ Registra una jugada en el tablero de juego
        retorna True si el jugador gana la partida
    """
    while True:     
        print("Juegue jugador ", jugador)
        f = int(input("fila? "))
        c = int(input("columna? "))
        if type(f)==type(c)==type(1) and valido(f) and valido(c) and tablero[f][c]==' ':
            tablero[f][c] = jugador
            break      

    imprimir(triqui)
    diag = ganaDiagonal1(jugador,tablero) or ganaDiagonal2(jugador,tablero)
    linea = ganaHorizontal(jugador,tablero) or ganaVertical(jugador,tablero)
    return  diag or linea

# Agregamos una función para chequear si hay empate:
#  - el tablero está lleno y
#  - no hay ninguna casilla vacía (con el caracter ' ')
def empate(tablero):
    """ Revisa si hay un empate """
    for i in range(3):
        for j in range(3):
            if tablero[i][j]==' ':
                return False
    return True

triqui = crear()

while True:
    if jugar("O",triqui):
        print("Gana el jugador O !!!!")
        break
    if jugar("X",triqui):
        print("Gana el jugador X !!!!")
        break
    if empate(triqui):
        print("Empate !!!")
        break
