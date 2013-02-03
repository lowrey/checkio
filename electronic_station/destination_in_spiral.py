def get_circuit(max_elem):
    #get length of the matrix
    from math import ceil,sqrt
    root = ceil(sqrt(max_elem))
    if root%2 == 0:
        root += 1
    matr_len = root**2
    #genrate values within matrix
    matr = [[0 for i in range(root)] for j in range(root)]
    visited = [[False for i in range(root)] for j in range(root)]
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    curr_direction = 0
    curr_num = matr_len
    curr_pos = (0,0)
    while curr_num:
        x, y = curr_pos
        matr[y][x] = curr_num
        curr_num -= 1
        if not curr_num: #if done filling the matrix in
            continue
        visited[y][x] = True
        next_x, next_y = (x+directions[curr_direction][0],\
            y+directions[curr_direction][1])
        if next_x >= len(matr[0]) or next_y >= len(matr)\
             or visited[next_y][next_x]:
            curr_direction += 1
            if curr_direction >= len(directions):
                curr_direction = 0
            next_x, next_y = (x+directions[curr_direction][0], \
                y+directions[curr_direction][1])
        curr_pos = (next_x,next_y)
    return matr

def get_pos(matr, num):
    for y in range(len(matr)):
        for x in range(len(matr[0])):
            if matr[y][x] == num:
                return (x,y)

def checkio(data):
    "Find the destination"
    a, b = data
    matr = get_circuit(max(data))
    a_pos = get_pos(matr,a)
    b_pos = get_pos(matr,b)
    dist = abs(b_pos[0]-a_pos[0]) + abs(b_pos[1]-a_pos[1])
    print(a_pos,b_pos,dist)
    return dist

if __name__ == '__main__':
    assert checkio([1, 9]) == 2, "First"
    assert checkio([9, 1]) == 2, "Reverse First"
    assert checkio([10, 25]) == 1, "Neighbours"
    assert checkio([5, 9]) == 4, "Diagonal"
    assert checkio([26, 31]) == 5, "One row"
    assert checkio([50, 16]) == 10, "One more test"

