def formaArreglo(tamano):
    Arr=[None]*tamano
    return Arr

def obtenerLlaveNumerica(llave):
        hash=0
        for char in str(llave):
            hash+=ord(char)
        return hash

def H(llaveN):
    return llaveN%5

def agregar(llave,valor,map,tamano):
    llave_hash=H(obtenerLlaveNumerica(llave))
    ParllaveValor=[llave,valor]
    if map[llave_hash] is None:
        map[llave_hash]=list([ParllaveValor])
        return True
    else:
        for par in map[llave_hash]:
            if par[0]==llave:
                par[1]=valor
                return True
            for j in range(tamano):
                llave=(llave_hash+j)%13