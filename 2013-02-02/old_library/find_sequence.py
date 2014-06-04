def checkio(matr):
    'return whether the specified square matrix is skew-symmetric or not'
    for i in range(len(matr[0])):
        for j in range(len(matr)):
            if matr[i][j] != matr[j][i] * -1 or matr[j][i] != matr[i][j] * -1:
                return False
    return True

if __name__ == '__main__':
    """
    assert checkio([[0, 1,2],
                    [-1,0,1],
                    [-2,-1,0]]) == True, 'First'
    assert checkio([[0, 1,2],
                    [-1,1,1],
                    [-2,-1,0]]) == False, 'Second'
                    """
    assert checkio([[0, 1,2],
                    [-1,0,1],
                    [-3,-1,0]]) == False, 'Third'
    print('All ok')
