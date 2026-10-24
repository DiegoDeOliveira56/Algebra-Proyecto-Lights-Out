import math

def gauss_Binario(matriz):
    n = len(matriz)
    m = len(matriz[0])
    pivotes = []
    fila_pivote = 0

    for columna in range(m - 1):
        pivote = fila_pivote

        while pivote < n and matriz[pivote][columna] == 0:
            pivote += 1

        if pivote == n:
            continue

        matriz[fila_pivote], matriz[pivote] = (
            matriz[pivote], matriz[fila_pivote]
        )

        for j in range(n):
            if j != fila_pivote and matriz[j][columna] == 1:
                for k in range(m):
                    matriz[j][k] ^= matriz[fila_pivote][k]

        pivotes.append(columna)
        fila_pivote += 1

        if fila_pivote == n:
            break

    # Comprobar si el sistema es incompatible
    for fila in matriz:
        if all(valor == 0 for valor in fila[:-1]) and fila[-1] == 1:
            return None

    # Sustitución hacia atrás
    solucion = [0] * (m - 1)

    for i in range(len(pivotes) - 1, -1, -1):
        columna = pivotes[i]
        valor = matriz[i][-1]

        for j in range(columna + 1, m - 1):
            valor ^= matriz[i][j] & solucion[j]

        solucion[columna] = valor

    return solucion


def transf_LightsOut(matriz):
    # Validar que sea una matriz cuadrada
    if not matriz or any(len(fila) != len(matriz) for fila in matriz):
        return "La matriz debe ser cuadrada"

    # Validar que solo contenga ceros y unos
    for fila in matriz:
        for numero in fila:
            if numero not in (0, 1):
                return "La matriz debe contener solo 0s y 1s"

    n = len(matriz)
    cantidad = n * n

    # Convertir la matriz en un vector
    vector = [numero for fila in matriz for numero in fila]

    # Construir la matriz A
    matrizA = [[0] * cantidad for _ in range(cantidad)]

    for i in range(n):
        for j in range(n):
            columna = i * n + j

            posiciones = [
                (i, j),
                (i - 1, j),
                (i + 1, j),
                (i, j - 1),
                (i, j + 1)
            ]

            for fila, columna_tablero in posiciones:
                if 0 <= fila < n and 0 <= columna_tablero < n:
                    filaA = fila * n + columna_tablero
                    matrizA[filaA][columna] = 1

    # Construir la matriz aumentada [A | b]
    matrizAumentada = [
        matrizA[i] + [vector[i]]
        for i in range(cantidad)
    ]

    solucion = gauss_Binario(matrizAumentada)

    if solucion is None:
        return "El tablero no tiene solución"

    return solucion


print(transf_LightsOut([
    [1, 0],
    [0, 1]
]))  # 2x2

print(transf_LightsOut([
    [1, 1, 0],
    [1, 0, 0],
    [0, 0, 0]
]))  # 3x3

print(transf_LightsOut([
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 1]
])) # 4x4

print(transf_LightsOut([
    [1, 0, 0, 1],
    [0, 0, 0, 0],
    [1, 0, 1, 1],
    [0, 1, 1, 0]
]))  # 4x4 (no tiene solución)