def visit_pos(matr, visited, pos):
    i,j = pos
    visited[i][j] = True
    if i-1 >= 0 and not visited[i-1][j]: #can go left
        if matr[i-1][j] == matr[i][j]:
            visit_pos(matr, visited, [i-1,j])
    if i+1 < len(matr[0]) and not visited[i+1][j]: #can go right
        if matr[i+1][j] == matr[i][j]:
            visit_pos(matr, visited, [i+1,j])
    if j+1 < len(matr) and not visited[i][j+1]: #can go up
        if matr[i][j+1] == matr[i][j]:
            visit_pos(matr, visited, [i,j+1])
    if j-1 >= 0 and not visited[i][j-1]: #can go down
        if matr[i][j-1] == matr[i][j]:
            visit_pos(matr, visited, [i,j-1])
    count = 0
    for y in visited:
        for x in y:
            if x:
                count += 1
            #count += x
    return count

def checkio(matr):
    '''
    Given matrix  NxN (3<=N<=10).
    Numbers between 1 and 5 are elements of A.
    Find the biggest union of the same numbers in group and the number.
    Say, group is a bunch of numbers that stay near each other.
    '''
    biggest = [0,1]
    for i in range(len(matr[0])):
        for j in range(len(matr)):
            visited = [[False for x in matr[0]] for y in matr]
            count = visit_pos(matr, visited, [i,j])
            if count > biggest[0]:
                biggest = [count, matr[i][j]]
    return biggest


if __name__ == '__main__':
    assert checkio([
        [1,2,3,4,5],
        [1,1,1,2,3],
        [1,1,1,2,2],
        [1,2,2,2,1],
        [1,1,1,1,1]
    ])==[14,1], 'First'

    assert checkio([
        [2, 1, 2, 2, 2, 4],
        [2, 5, 2, 2, 2, 2],
        [2, 5, 4, 2, 2, 2],
        [2, 5, 2, 2, 4, 2],
        [2, 4, 2, 2, 2, 2],
        [2, 2, 4, 4, 2, 2]
    ])==[19,2], 'Second'
    print('All ok')
