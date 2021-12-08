# Laberinto

Esta tarea consistió en dos partes:
1) Hacer un programa que cree un laberinto
2) Hacer un programa que imprima la solucion al laberinto

Mi dirección de este repositorio es el siguiente:[GitHub](https://github.com/pelahumi/Laberinto)
https://github.com/pelahumi/Laberinto

El diagrama de flujo de esta tarea es el siguiente:
![Diagrama de flujo](https://github.com/pelahumi/Laberinto/blob/main/Captura%20de%20pantalla%202021-12-08%20a%20las%2020.31.26.png)

El código de la tarea es el siguiente:
'''"""""
lab = [
    [" ","X","X","X","X"]
    [" ","X","X","X","X"]
    [" ","X"," "," "," "]
    [" "," "," ","X"," "]
    ["X","X","X","X"," "]
    ]
"""""
muros = ((0,1),(0,2),(0,3),(0,4),(1,1),(1,2),(1,3),(1,4),(2,1),(3,3),
(4,0),(4,1),(4,2),(4,3))


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
maze = crear_laberinto(6,muros)

for i in maze:
    print("".join(i))

#2º parte

def solucion_laberinto(laberinto):
    fila = 0
    columna = 0
    n = 6
    solucion = ["Abajo"]
    #Bucle para que encuentre la salida
    while (fila < n-1 and columna < n-1):
        if solucion[-1] != "Arriba" and fila + 1 < n and laberinto[fila + 1][columna] != "X":
            fila += 1
            solucion.append("Abajo")
        if solucion[-1] != "Abajo" and fila - 1 > 0 and laberinto[fila - 1][columna] != "X":
            fila -= 1 
            solucion.append("Arriba")
        if solucion[-1] != "Izquierda" and columna + 1 < n and laberinto[fila][columna + 1] != "X":
            columna += 1
            solucion.append("Derecha")
        if solucion[-1] != "Derecha" and columna - 1 > 0 and laberinto[fila][columna - 1] != "X":
            columna -= 1
            solucion.append("Izquierda")
    return solucion
    #Nos almacena cada movimiento en la lista de solucion

print("Para encontrar la salida del laberinto tienes que seguir los siguientes pasos: " + str(solucion_laberinto(maze)))
