def bubblesort(A):
    for i in range(0, len(A)): #Para i en 1 hasta longitd de A
        for j in range(0, len(A)-i-1):
            print(A)
            if A[j]>A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
A=[5,4,3,2,1]
bubblesort(A)
print("\n")
print(A)
