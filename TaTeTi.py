import tkinter as tk
import random

def inicializar_tablero():
    """
    Crea e inicializa el tablero de juego con espacios vacíos.
    """
    tablero = [[' ' for _ in range(3)] for _ in range(3)]
    return tablero

def actualizar_botones(tablero):
    """
    Actualiza el texto y color de los botones en la ventana según el tablero actual.
    """
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == 'O':
                botones[i][j]['text'] = 'O'
                botones[i][j]['bg'] = '#a1e9c7'  # Color verde claro para ficha O
                botones[i][j]['fg'] = '#000000'  # Texto negro para ficha O
            elif tablero[i][j] == 'X':
                botones[i][j]['text'] = 'X'
                botones[i][j]['bg'] = '#4caf50'  # Color verde para ficha X
                botones[i][j]['fg'] = '#000000'  # Texto negro para ficha X
            else:
                botones[i][j]['text'] = ' '
                botones[i][j]['bg'] = '#c8e6c9'  # Color verde claro para espacios vacíos
                botones[i][j]['fg'] = '#000000'  # Texto negro para espacios vacíos

def reiniciar_juego():
    """
    Reinicia el juego: limpia el tablero, los botones y el resultado.
    """
    global tablero
    tablero = inicializar_tablero()
    actualizar_botones(tablero)
    resultado['text'] = ''
    habilitar_botones()

def jugar_humano(fila, columna):
    """
    Permite al jugador humano realizar un movimiento en el tablero.
    """
    if tablero[fila][columna] == ' ' and resultado['text'] == '':
        tablero[fila][columna] = 'O'
        actualizar_botones(tablero)
        if ganador(tablero, 'O'):
            resultado['text'] = "¡Has ganado!"
            deshabilitar_botones()
        elif esta_lleno(tablero):
            resultado['text'] = "Es un empate."
            deshabilitar_botones()
        else:
            jugar_maquina()

def jugar_maquina():
    """
    Permite a la máquina realizar un movimiento en el tablero.
    """
    while True:
        fila = random.randint(0, 2)
        columna = random.randint(0, 2)
        if tablero[fila][columna] == ' ':
            tablero[fila][columna] = 'X'
            actualizar_botones(tablero)
            if ganador(tablero, 'X'):
                resultado['text'] = "¡La máquina ha ganado!"
                deshabilitar_botones()
            elif esta_lleno(tablero):
                resultado['text'] = "Es un empate."
                deshabilitar_botones()
            break

def ganador(tablero, simbolo):
    """
    Verifica si el jugador con el símbolo dado ha ganado.
    """
    # Verificar filas y columnas
    for i in range(3):
        if all(tablero[i][j] == simbolo for j in range(3)) or all(tablero[j][i] == simbolo for j in range(3)):
            return True

    # Verificar diagonales
    if tablero[0][0] == simbolo and tablero[1][1] == simbolo and tablero[2][2] == simbolo:
        return True
    if tablero[0][2] == simbolo and tablero[1][1] == simbolo and tablero[2][0] == simbolo:
        return True
    return False

def esta_lleno(tablero):
    """
    Verifica si el tablero está lleno.
    """
    for fila in tablero:
        if ' ' in fila:
            return False
    return True

def deshabilitar_botones():
    """
    Deshabilita todos los botones del tablero.
    """
    for i in range(3):
        for j in range(3):
            botones[i][j]['command'] = None

def habilitar_botones():
    """
    Habilita todos los botones del tablero.
    """
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == ' ':
                botones[i][j]['command'] = lambda i=i, j=j: jugar_humano(i, j)

# Inicializar la GUI
ventana = tk.Tk()
ventana.title('TaTeTi')

# Definir estilos de colores verdes
color_fondo_botones = '#c8e6c9'  # Fondo verde claro para los botones
color_texto_botones = '#000000'  # Texto negro para los botones

tablero = inicializar_tablero()
botones = [[tk.Button(ventana, text=' ', width=10, height=3,
                      bg=color_fondo_botones, fg=color_texto_botones,
                      command=lambda i=i, j=j: jugar_humano(i, j))
             for j in range(3)] for i in range(3)]

# Colocar los botones en la ventana
for i in range(3):
    for j in range(3):
        botones[i][j].grid(row=i, column=j)

resultado = tk.Label(ventana, text='', font=('Helvetica', 20))
resultado.grid(row=3, column=0, columnspan=3)

boton_reiniciar = tk.Button(ventana, text="Reiniciar juego", command=reiniciar_juego)
boton_reiniciar.grid(row=4, column=0, columnspan=3)

ventana.mainloop()
