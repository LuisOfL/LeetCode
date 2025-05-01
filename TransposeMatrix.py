def transposeMatrix(arr):
    n = len(arr)
    m = len(arr[0])
    matrixT = []
    for i in range(m):
        temp = []
        for j in range(n):
            temp.append(arr[j][i])
        matrixT.append(temp)
    return matrixT

arr = [[2,3,4],
       [5,6,7]]

arrT = transposeMatrix(arr)
print(arrT)
