def busquedaLineal(A, n, x):
    encontrado = "Valor no encontrado"
    for k in range(n+1):
        if A[k] == x:
            encontrado = k

    return encontrado


A = [1, 4, 6, 8, 9, 11]
v = []
print(busquedaLineal(A, 5, 8))
