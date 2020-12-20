import pygame
import numpy as np
import time
import sys 

if(len(sys.argv) < 2  or len(sys.argv) > 4 ):
    print('\n\n\nEjecute:\n         python ' + str(sys.argv[0]) + ' [regla] [tiempo (segundos)] [lattice] ')
    print('         Para mayor información consulte README.md.\n\n\n')
    exit(0)
elif(int(sys.argv[1]) < 0 or int(sys.argv[1]) > 255):
    print('regla debe estar entre 0 y 255')
    exit(0)
elif(int(sys.argv[3]) < 0 ):
    print('lattice debe ser positivo')
    exit(0)


pygame.init()
bg = 'white'
cuadro = 'black'
linea = 'gray'
regla = int(sys.argv[1])
tiempo = int(sys.argv[2])
#Define el numero de celdas del juego en x
nxC = int(sys.argv[3])


pauseExect = True
run = True
z = y = 0
time_sleep = 0.5    

rule= list(np.binary_repr(regla, width=8))
rule.reverse()

def imprimirCuadricula(nyC, nxC, tamCelda, pygame,):
    #Dibujar cuadricula
    screen.fill(bg)

    #Define el estado de las celdas. Vivas = 1 ; Muertas = 0
    gameState = np.zeros((nxC, nyC))
    gameState[int(nxC / 2), 0] = 1
    newGameState = np.copy(gameState)

    for y in range(0, nyC):
        for x in range(0, nxC):                          
            poly = [((x) * tamCelda, (y) * tamCelda),
                    ((x + 1) * tamCelda , (y)* tamCelda),
                    ((x + 1) * tamCelda , (y + 1) * tamCelda),
                    ((x) * tamCelda , (y + 1) * tamCelda)]
                
            if gameState[x, y] == 1:
                pygame.draw.polygon(screen, cuadro, poly, 0)   
            else:
                pygame.draw.polygon(screen, linea, poly, 1)
    return gameState, newGameState

def process_events(pauseExect, run, time_sleep, y, gameState, newGameState, global_time):
    for event in pygame.event.get():   
        if event.type == pygame.QUIT: run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: pauseExect = not pauseExect
            elif (event.key == pygame.K_UP):
                if(time_sleep > 0.2):
                    time_sleep = time_sleep - 0.1
                elif(time_sleep - 0.01 > 0):
                    time_sleep = time_sleep - 0.01
                else:
                    time_sleep = 0
            elif (event.key == pygame.K_DOWN):
                time_sleep = time_sleep + 0.1
            elif (event.key == pygame.K_ESCAPE):
                gameState, newGameState = imprimirCuadricula(nyC, nxC, tamCelda, pygame)
                pauseExect = True
                y = 0
                global_time = 0
    return pauseExect, run, time_sleep, y, gameState, newGameState, global_time

def process_mouse():
    mouseClick = pygame.mouse.get_pressed()
    if sum(mouseClick) > 0 :
        posX, posY = pygame.mouse.get_pos()
        celX, celY = int(np.floor(posX / tamCelda)), int(np.floor(posY / tamCelda))
        if(celX < nxC and celY < nyC):
            gameState[celX, celY] =  not mouseClick[2]
            newGameState[celX, celY] = not mouseClick[2]
            poly = [((celX) * tamCelda, (celY) * tamCelda),
                ((celX + 1) * tamCelda , (celY)* tamCelda),
                ((celX + 1) * tamCelda , (celY + 1) * tamCelda),
                ((celX) * tamCelda , (celY + 1) * tamCelda)]
            
            if gameState[celX, celY] == 1:
                pygame.draw.polygon(screen, cuadro, poly, 0)   
            else:
                pygame.draw.polygon(screen, bg, poly, 0)
            pygame.draw.polygon(screen, linea, poly, 1)

#Define el tamaño de la pantalla del juego
zise = width, height = 1700, 950 


#Define el tamaño de cada celda del juego
#dimCW   dimCH
tamCelda = (width - 1) / nxC

#Define el numero de celdas del juego en y
nyC = int(height / tamCelda)

screen = pygame.display.set_mode((width,height))
screen.fill(bg)


gameState, newGameState = imprimirCuadricula(nyC, nxC, tamCelda, pygame)


start_time = 0
end_time = 0
global_time = 0


while run:
    start_time = time.time()
    pauseExect, run, time_sleep, y, gameState, newGameState, global_time = process_events(pauseExect, run, time_sleep, y, gameState, newGameState, global_time)                
    process_mouse()
     
             
    if not pauseExect and global_time < tiempo:
        
        time.sleep(time_sleep)
        
        for x in range(0, nxC):
            
            ruleIndex = 4 * gameState[(x - 1) % nxC, y] + \
                    2 * gameState[x , y] + \
                    1 * gameState[(x + 1) % nxC, y] 

            newGameState[x, (y + 1) % nyC] = rule[int(ruleIndex)]
                        
            poly = [((x) * tamCelda, (y) * tamCelda),
                    ((x + 1) * tamCelda , (y)* tamCelda),
                    ((x + 1) * tamCelda , (y + 1) * tamCelda),
                    ((x) * tamCelda , (y + 1) * tamCelda)]
                
            if newGameState[x, y] == 1:
                pygame.draw.polygon(screen, cuadro, poly, 0)   
            else:
                pygame.draw.polygon(screen, bg, poly, 0)
            pygame.draw.polygon(screen, linea, poly, 1)
        
           
    else:
        pauseExect = True
    """ if not pauseExect and (z + 1 ) < nyC:
        y = (y + 1) % nyC
        z = y
    elif not pauseExect :
        pauseExect = True
        z = 1 """
    gameState = np.copy(newGameState)          
    pygame.display.flip()

    end_time = time.time() 
    xx = end_time- start_time
    
    if not pauseExect :
        y = (y + 1) % nyC
        global_time += xx

    
pygame.quit()