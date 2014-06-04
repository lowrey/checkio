def shortest_path(src, dest):
    direcs = ((1,-2),(2,-1),(2,1),(1,2),(-1,2),\
                (-2,1),(-2,-1),(-1,-2))
    queue = []
    queue.append([src])
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == dest:
            return len(path)-1
        for d in direcs:
            new_x = node[0]+d[0]
            new_y = node[1]+d[1]
            new_node = (new_x,new_y)
            #check to see if new pos. is on the board
            if new_x >= 0 and new_y >= 0:
                if new_x <= 7 and new_y <= 7:
                    new_path = list(path)
                    new_path.append(new_node)
                    queue.append(new_path)


def checkio(move_string):
    '''
    Find a length of the shortest path of knight
    '''
    src, dest = move_string.split("-")
    #convert chess notation to array notation
    src = (ord(src[0])-97, abs(8-int(src[1])))
    dest = (ord(dest[0])-97, abs(8-int(dest[1])))
    return shortest_path(src, dest)

if __name__ == "__main__":
    assert checkio("b1-d5") == 2, "First"
    assert checkio("a6-b8") == 1, "Second"
    assert checkio("h1-g2") == 4, "Third"
    assert checkio("h8-d7") == 3, "Fourth"
    assert checkio("a1-h8") == 6, "Fifth"
    print("All ok")

