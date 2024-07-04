# Define Functions for addition, subtraction
def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]

def subtract_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]

# Strassen multiplication
def strassen_multiply(A, B):
    if len(A) == 1:
        return [[A[0][0] * B[0][0]]]

    # Split matrices into submatrices
    n = len(A)
    mid = n // 2

    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    # Calculate P recursively
    P1 = strassen_multiply(A11, subtract_matrices(B12, B22))
    P2 = strassen_multiply(add_matrices(A11, A12), B22)
    P3 = strassen_multiply(add_matrices(A21, A22), B11)
    P4 = strassen_multiply(A22, subtract_matrices(B21, B11))
    P5 = strassen_multiply(add_matrices(A11, A22), add_matrices(B11, B22))
    P6 = strassen_multiply(subtract_matrices(A12, A22), add_matrices(B21, B22))
    P7 = strassen_multiply(subtract_matrices(A11, A21), add_matrices(B11, B12))

    C11 = add_matrices(subtract_matrices(add_matrices(P5, P4), P2), P6)
    C12 = add_matrices(P1, P2)
    C21 = add_matrices(P3, P4)
    C22 = subtract_matrices(subtract_matrices(add_matrices(P5, P1), P3), P7)

    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(mid):
        for j in range(mid):
            C[i][j] = C11[i][j]
            C[i][j + mid] = C12[i][j]
            C[i + mid][j] = C21[i][j]
            C[i + mid][j + mid] = C22[i][j]

    return C

if __name__ == '__main__':
    ## Define matrices
    A = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]
    
    B = [[17, 18, 19, 20],
         [21, 22, 23, 24],
         [25, 26, 27, 28],
         [29, 30, 31, 32]]

    # Print result
    result = strassen_multiply(A, B)
    for row in result:
        print("\t".join([str(i) for i in row]))
