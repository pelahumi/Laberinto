"""""
lab = [
    [" ","X","X","X","X","X"]
    [" ","X","X","X","X","X"]
    [" ","X"," "," "," "," "]
    [" ","X"," ","X","X"," "]
    [" "," "," ","X","X"," "]
    ["X","X","X","X","X"," "]
    ]
"""""
muros = (
    (0,1),(0,2),(0,3),(0,4),(0,5),
    (1,1),(1,2),(1,3),(1,4),(1,5),
    (2,1),
    (3,1),(3,3),(3,4),
    (4,3),(4,4),
    (5,3),(5,4),
    (6,0),(6,1),(6,2),(6,3),(6,4))


def crear_laberinto(tamano, muros):
    #La siguiente función creará el laberinto

    laberinto=[]
    for i in range(tamano):
        fila = []
        #Este bucle recorrerá las filas del laberinto y las añadirá a la lista fila
        
        for j in range(tamano):
            if tuple([i,j]) in muros:
                fila.append("X")
            else:
                fila.append(" ")
        #Condicionales para saber si la coordenada es un muro o un espacio libre

        laberinto.append(fila)
    return laberinto
maze = crear_laberinto(5,muros)

for i in maze:
    print("".join(i))

#2º parte

def solucion_laberinto(laberinto):
    fila = 0
    columna = 0
    solucion = ["Abajo"]
    #Bucle para que encuentre la salida
    while (fila < n-1 and columna < n-1):
        if solucion[-1] != "Arriba" and fila + 1 < n and laberinto[fila + 1][columna] != X:
            fila += 1
            solucion.append("Abajo")
        if solucion[-1] != "Abajo" and fila - 1 > 0 and laberinto[fila - 1][columna] != X:
            fila -= 1 
            solucion.append("Arriba")
        if solucion[-1] != "Izquierda" and columna + 1 < n and laberinoto[fila][columna + 1] != X:
            columna += 1
            solucion..append("Derecha")
        else:
            columna -= 1
            solucion.append("Izquierda")
    return solucion
    #Nos almacena cada movimiento en la lista de solucion


    