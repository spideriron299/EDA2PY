cadena = "Amor y deseo son dos cosas diferentes; que no todo lo que se ama se desea, ni todo lo que se desea se ama. (Don Quijote)"
nueva_cadena = []
for i in range(len(cadena)):
    if cadena.find(';'):
        x = cadena.find(';')

for j in range(len(cadena)):
    if j < x:
        y = cadena[j].upper()
        nueva_cadena.append(y)
    else:
        y = cadena[j].lower()
        nueva_cadena.append(y)
        
print(*nueva_cadena)