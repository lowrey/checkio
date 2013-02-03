def zero(m,n):
    new_matrix = [[0 for row in range(n)] for col in range(m)]
    return new_matrix

def checkio(parameters):
    """Return product of an MxP matrix A with an PxN matrix B."""
    matrix1,matrix2 = parameters
    if len(matrix1[0]) != len(matrix2):
        pass
    else:
        new_matrix = zero(len(matrix1),len(matrix2[0]))
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    new_matrix[i][j] += matrix1[i][k]*matrix2[k][j]
        return new_matrix
    pass
    
if __name__ == '__main__':
    assert checkio([[
                    [6,7,8], 
                    [5,4,5], 
                    [1,1,1]
                   ], 
                   [
                    [1,2,3], 
                    [1,2,3], 
                    [1,2,3]
                   ]]) == [
                            [21, 42, 63], 
                            [14, 28, 42], 
                            [3, 6, 9]
                         ], 'First'
    assert checkio([[
                    [4,4,-1,0,-1,8],
                    [2,3,7,5,2,3],
                    [3,2,5,7,3,2],
                    [1,2,2,1,1,2],
                    [1,7,6,6,5,7]
                  ], [
                      [-5,-7,-2,2,-2,16,1],
                      [0,0,4,0,-5,0,4],
                      [2,0,-2,0,2,0,1],
                      [6,4,6,-1,15,-5,5],
                      [5,-4,10,1,14,6,1],
                      [3,0,-2,0,3,0,1]]]) == [
                                                [-3,-24,-16,7,-20,58,26],
                                                [53,-2,38,1,107,19,51],
                                                [58,-5,60,2,147,31,56],
                                                [16,-7,14,2,27,17,19],
                                                [89,-3,86,1,156,16,77]
                                            ], 'Second'
    print('All Ok')
