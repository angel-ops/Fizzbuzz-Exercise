#TIC TAC TOE CONSOLA
#Variables globales
juego_sigue = True
winner = None
current_player = 'X'

def main():
  #GATO
  tablero = [' ',' ',' ',
              ' ',' ',' ',
              ' ',' ',' ']
  
  #DIBUJAR TABLERO
  def dibujar_tablero():
    print('En donde va ser tu siguiente jugada?')
    print('')
    print(tablero[0]  + ' | ' + tablero[1] + ' | ' + tablero[2])
    print('--+---+---')
    print(tablero[3]  + ' | ' + tablero[4] + ' | ' + tablero[5])
    print('--+---+---')
    print(tablero[6]  + ' | ' + tablero[7] + ' | ' + tablero[8])
    print('')
  
  
  #DISPLAY
  def jugar():
    
    #dibujar el tablero inicial
    dibujar_tablero()
    
    while juego_sigue:
      
      simbolos()

      
      juego_terminado()

      
      cambio_de_jugador()

    if winner == 'X'  or winner == 'O':
      print('El ganador es: ' + winner)
    elif winner == None:
      print('Empate')
  

  #TURNO DE JUGADORES
  def simbolos():
    global current_player
    #indicador_de_turno()
    print('Turno: ' + current_player)
    print('')
    posicion = input('Cual posición del 1-9 quieres poner el simbolo? ')
    posicion = int(posicion) - 1
    print('')
    tablero[posicion] = current_player
    dibujar_tablero()

  #JUEGO

  #CHECAR GANADOR
  def juego_terminado():
    ganador()
    empate()
    return

  def ganador():
    global winner
    rows_winner = checar_filas()
    columns_winner = checar_columnas()
    diagonals_winner = checar_diagonales()
    
    if rows_winner:
      winner = rows_winner
    elif columns_winner:
      winner = columns_winner
    elif diagonals_winner:
      winner = diagonals_winner
    else:
      winner = None
    return


  #VAMOS A CHECAR LAS FILAS,COLUMNAS Y DIAGONALES PARA VER SI NO SON IGUALES 
  def checar_filas():
    #GLOBAL SETTINGS
    global juego_sigue
    
    fila_1 = tablero[0] == tablero[1] == tablero[2] != ' '
    fila_2 = tablero[3] == tablero[4] == tablero[5] != ' '
    fila_3 = tablero[6] == tablero[7] == tablero[8] != ' '

    if fila_1 or fila_2 or fila_3:
      juego_sigue = False

    if fila_1:
      return tablero[0]
    elif fila_2:
      return tablero[3]
    elif fila_3:
      return tablero[6]
    return

  def checar_columnas():
    global juego_sigue
    columna_1 = tablero[0] == tablero[3] == tablero[6] != ' '
    columna_2 = tablero[1] == tablero[4] == tablero[7] != ' '
    columna_3 = tablero[2] == tablero[5] == tablero[8] != ' '

    if columna_1 or columna_2 or columna_3:
      juego_sigue = False

    if columna_1:
      return tablero[0]
    elif columna_2:
      return tablero[1]
    elif columna_3:
      return tablero[2]
    return

  def checar_diagonales():
    global juego_sigue
    diagonal_1 = tablero[0] == tablero[4] == tablero[8] != ' '
    diagonal_2 = tablero[2] == tablero[4] == tablero[6] != ' '

    if diagonal_1 or diagonal_2:
      juego_sigue = False

    if diagonal_1:
      return tablero[4]
    elif diagonal_2:
      return tablero[4]
    return

  def empate():
    global juego_sigue
    if ' ' not in tablero:
      juego_sigue = False 
    return
    
  def cambio_de_jugador():
    global current_player
    if current_player == 'X':
      current_player = 'O'
    elif current_player == 'O':
      current_player = 'X'
    return
  
  jugar()
  
main()
