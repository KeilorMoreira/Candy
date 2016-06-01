import pygame,sys
from random import randint

pygame.init()
LARGO  = 50
ALTO = 50

MARGEN = 5


pygame.display.set_caption("Retículas y Matrices")
d1 = pygame.image.load("d1.png")
d2 = pygame.image.load("d2.png")
d3 = pygame.image.load("d3.png")
d4 = pygame.image.load("d4.png")
d5 = pygame.image
fondo = pygame.image.load("fondo.png")

matriz = [[4, 2, 3, 3, 2, 4, 4, 4, 2],
          [4, 1, 4, 1, 4, 1, 2, 3, 3],
          [3, 2, 2, 3, 2, 3, 2, 1, 1],
          [4, 3, 2, 3, 2, 4, 3, 4, 1],
          [3, 1, 4, 1, 3, 1, 4, 2, 3],
          [3, 2, 2, 1, 4, 2, 4, 1, 4],
          [1, 3, 1, 2, 2, 3, 2, 3, 4],
          [4, 4, 3, 3, 2, 3, 4, 2, 2],
          [1, 1, 3, 4, 1, 1, 4, 4, 2]]

"""
contador = 0
for x in range(10): # LLenar matriz con random
    aux = []
    for y in range(10):
        aux.append(randint(1,4))
    matriz.append(aux)
    print(aux)
"""




puntaje = 50

def explotar(lista):
    if (len(lista)==4):
        d5.load("bomb.png")
    elif(len(lista)==5):
        d5.load("bombS.png")

    for fila in matriz:
        for ele in fila:
            print("")
    return

def verificarFilas():
    contador = 0
    listPos=[]
    for fil in matriz:
        for col in fila:
            if(matriz[fil][col] == matriz[fil][col+1]):
                listPos.append((fil,col))
                contador +=1
                if (contador >= 3):
                    explotar(listPos)
            elif(matriz[fil][col] != matriz[fil][col]):
                contador=0
    return

def verificarColumnas():
    return



def cambiar(t1,t2):
    n1,n2 = t1
    n3,n4 = t2
    n5 = matriz [n3][n4]  # Respladamos el contenido que reescribiremos
    matriz [n3][n4] = matriz[n1][n2]
    matriz [n1][n2] = n5













DIMENSION_VENTANA = [700, 525]
pantalla = pygame.display.set_mode(DIMENSION_VENTANA)






reloj = pygame.time.Clock()
tpa = ()
bandera = False
while True:
    #pantalla.blit(fondo,(0,0))
    a= pygame.draw.rect(pantalla,pygame.Color("Black"),[0,0,700,525])
    b= pygame.draw.rect(pantalla,pygame.Color("White"),[0,0,525,525])

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            columna = pos[0] // (LARGO + MARGEN)
            fila = pos[1] // (ALTO + MARGEN)
            if(bandera == False):
                tpa = (fila, columna)
                bandera = True
                print("Inicial",(fila, columna))
            else:
                print("Comparado con :",(fila, columna))
                if(((tpa[1]-1==columna and tpa[0]== fila) or  (tpa[1]+1==columna and tpa[0]== fila) or (tpa[0]-1==fila and tpa[1] == columna) or (tpa[0]+1==fila and tpa[1]==columna))):
                    cambiar(tpa, (fila, columna))
                    print("Movimiento valido")

                else:
                    print("Movimiento no valido")
                tpa = ()
                bandera = False
            #print("Click ", pos, "Coordenadas de la retícula: ", fila, columna)


    


    for fila in range(9):

        for columna in range(9):

            if matriz[fila][columna] == 1:
                pantalla.blit(d1,[(MARGEN+LARGO) * columna + MARGEN,(MARGEN+ALTO) * fila + MARGEN,LARGO,ALTO])
            elif matriz[fila][columna] == 2:
                pantalla.blit(d2,[(MARGEN+LARGO) * columna + MARGEN,(MARGEN+ALTO) * fila + MARGEN,LARGO,ALTO])
            elif matriz[fila][columna] == 3:
                pantalla.blit(d3,[(MARGEN+LARGO) * columna + MARGEN,(MARGEN+ALTO) * fila + MARGEN,LARGO,ALTO])
            elif matriz[fila][columna] == 4:
                pantalla.blit(d4,[(MARGEN+LARGO) * columna + MARGEN,(MARGEN+ALTO) * fila + MARGEN,LARGO,ALTO])



    # Limitamos a 20 fotogramas por segundo.
    reloj.tick(20)

    # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()

# Pórtate bien con el IDLE.
pygame.quit()
