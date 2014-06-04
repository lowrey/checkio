def quad(a, b, c):
    from math import sqrt
    sqrt_disc =  sqrt(b*b-4*a*c)
    first_max_levels = (-b + sqrt_disc) / (2*a)
    second_max_levels = (-b - sqrt_disc) / (2*a)
    return max(first_max_levels, second_max_levels)

dirs = {'N':(0,-2), 'NE':(1,-1), 'NW':(-1,-1), 'S':(0,2), 'SE':(1,1), 'SW':(-1,1)}
dir_order = ['NE','SE','S','SW','NW','N']

#return the next position given a direction
def move_pos(pos, curr_dir):
    if type(curr_dir) is int:
        pos_dir = dirs[dir_order[curr_dir]]
        return (pos[0]+pos_dir[0], pos[1]+pos_dir[1])
    elif type(curr_dir) is str:
        pos_dir = dirs[curr_dir]
        return (pos[0]+pos_dir[0], pos[1]+pos_dir[1])
    return None

def max_w(level):
    return 2*level-1

def max_h(level):
    return 4*level-3

def dist(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    d = 0
#move diagonally until you are on the right x coordinate
    while x1 != x2:
        if x2 > x1:
            x2 -= 1
        elif x1 > x2:
            x1 -= 1
        if y2 > y1:
            y2 -= 1
        elif y1 > y2:
            y1 -= 1
        d += 1
#then move vertically
    while y1 != y2:
        if y2 > y1:
            y2 -= 2
        if y1 > y2:
            y1 -= 2
        d += 1
    return d

def gen_hex(n):
    from math import ceil
    max_levels = ceil(quad(3,-3,1-n))
    max_y = max_h(max_levels)
    max_x = max_w(max_levels)

    #create empty matrix with max num of possible entries
    grid = [[0 for i in range(max_x)] for j in range(max_y)]
    mid = (ceil(max_x/2)-1,ceil(max_y/2)-1)
    pos = mid
    curr = 1
    grid[pos[1]][pos[0]] = curr
    level = 1
    while curr < n:
        curr +=1
        pos = move_pos(pos, 'N')
        grid[pos[1]][pos[0]] = curr
        level +=1 
        for direc in dir_order:
            #if it doesn't meet the boundaries of our level
            next_pos =  move_pos(pos, direc)
            d = dist(mid, next_pos)
            while d <= level-1:
                pos = next_pos
                curr += 1
                if curr > n:
                    return grid
                grid[pos[1]][pos[0]] = curr
                next_pos =  move_pos(pos, direc)
                d = dist(mid, next_pos)
    return grid

def get_pos(matr, num):
    for y in range(len(matr)):
        for x in range(len(matr[0])):
            if matr[y][x] == num:
                return (x,y)
    return None

def checkio(data):
    "Find the destination"
    a, b = data
    n = max(data)
    hex_grid =  gen_hex(n)
    pos_a = get_pos(hex_grid, a)
    pos_b = get_pos(hex_grid, b)
    return dist(pos_a, pos_b)

if __name__ == '__main__':
    assert checkio([2, 9]) == 1, "First"
    assert checkio([9, 2]) == 1, "Reverse First"
    assert checkio([6, 19]) == 2, "Second, short way"
    assert checkio([5, 11]) == 3, "Third"
    assert checkio([13, 15]) == 2, "Fourth, One row"
    assert checkio([11, 17]) == 4, "Fifrth, One more test"

