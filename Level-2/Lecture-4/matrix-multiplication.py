import tabulate 
def matrix_multiplication(a,b): 
    r1 = len(a)
    c1 = len(a[0])

    r2 = len(b)
    c2 = len(b[0])

    c = [[0 for i in range(c2)] for i in range(r1)]

    for row in range(r1):# this loop is for choosing row in matrix A 
        for col in range(c2): # this loop is for choosing col in matrix B 
            for i in range(r2): 
                c[row][col] += a[row][i] * b[i][col] 
                

    return c 


a = [[1,2,3],
     [4,5,6],
     [7,8,9]]

b = [[1,2,3],
     [4,5,6],
     [7,8,9]]

r1 = len(a)
c1 = len(a[0])

r2 = len(b)
c2 = len(b[0])

if c1 != c2: 
    print("Matrix multiplication is not possible")
else: 
    result = matrix_multiplication(a,b)
    print(tabulate.tabulate(result,headers="firstrow",tablefmt="grid"))