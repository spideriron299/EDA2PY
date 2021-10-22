#Ordenamiento por Mezcla
#Divide y venceras usando Recursividad y Baktraking
def crearSubArreglo(A, indIzq, indDer):
    return A[r+1]

def Merge(A,p,q,r):
    Izq = crearSubArreglo(A,p,q)
    Der = crearSubArreglo(A,q+1,r)
    i=0
    j=0
    for k in range(p, r+1):
        if(j>=len(Der)) or (i < len (Izq)and  Izq[i] < Der[j]):
            A[k]= Izq[i]
            print("Lista izquierda", Izq)
            i=i+1
        else:
            A[k]=Der[j]
            print("Lista derecha", Der) 
            j=j+1
def MergeSort(A,p,r):
    if r-p > 0:
        q= int((p+r)/2)
        MergeSort(A,p,q)
        MergeSort(A,q+1,r)
        Merge(A,p,q,r)

A=[9,4,8,2,5,3,53,85]
MergeSort(A,0,7)
print(A)
