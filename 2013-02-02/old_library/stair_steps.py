def add_perms(n, path=[], paths=[]):
    if sum(path) == n:
        return (path, True)
    if sum(path) > n:
        return ([],False)
    for i in range(1,3):
        p = add_perms(n, path + [i])
        if p[1]:
            paths.append(p[0])
    return (paths, False)

def walk(stairs, action):
    if len(stairs) < action:
        return 0
    return stairs[action-1]    

def checkio(stair_values):
    outcomes = []
    paths = add_perms(len(stair_values))[0]
    for path in paths:
        outcome = 0
        temp_stairs = stair_values[:]
        for action in path:
            outcome += walk(temp_stairs, action)
            temp_stairs = temp_stairs[action:]
        outcomes.append(outcome)
    return max(outcomes)
    

if __name__ == '__main__':
   assert checkio([5,6,-10,-7,4]) == 8, 'First'
   assert checkio([-11, 69, 77, -51, 23, 67, 35, 27, -25, 95])==393, 'Second'
   assert checkio([-21, -23, -69, -67, 1, 41, 97, 49, 27])==125, 'Third'
   assert checkio([5,-3,-1,2]) == 6, 'Fifth'
   print('All ok')
