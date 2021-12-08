laberinto = [
    [" ","X","X","X","X","X"]
    [" ","X","X","X","X","X"]
    [" ","X"," "," "," "," "]
    [" ","X"," ","X","X"," "]
    [" "," "," ","X","X"," "]
    ["X","X","X","X","X"," "]
    ]

muros = (
    (0,1),(0,2),(0,3),(0,4),(0,5),
    (1,1),(1,2),(1,3),(1,4),(1,5)
    (2,1)
    (3,1),(3,3),(3,4)
    (4,3),(4,4)
    (5,3),(5,4)
    (6,0),(6,1),(6,2),(6,3),(6,4))


def crear_laberinto(tamaño, muros):
    #La siguiente función creará el laberinto

    laberinto=[]
    for i in range(tamaño):
        fila = []
        #Este bucle recorrerá las filas del laberinto y las añadirá a la lista fila
        
        for j in range(tamaño):
            if tuple([i,j]) in muros:
                fila.append("X")
            else:
                fila.append(" ")
        #Condicionales para saber si la coordenada es un muro o un espacio libre
        
        laberinto.append(fila)
    