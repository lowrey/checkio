def permutate(n, i, perms):
    if i == len(n) - 1:
        perms.append(n[:])
    else:
        for j in range(i, len(n)):
            n[i], n[j] = n[j], n[i]
            permutate(n, i + 1, perms)
            n[i], n[j] = n[j], n[i] # swap back, for the next loop

def calc_diff(l, i):
    first, second = (l[:i], l[i:])
    total = sum(second) - sum(first)
    return abs(total)

def checkio(stones):
    '''
    minimal possible weight difference between stone piles
    '''
    perms = []
    permutate(stones, 0, perms)
    min_perms = []
    for perm in perms:
        calcs = []
        for i in range(len(perm)):
            calcs.append(calc_diff(perm, i))
        min_perms.append(min(calcs))
    return min(min_perms)

if __name__ == '__main__':
    assert checkio([10,10]) == 0, 'First, with equal weights'
    assert checkio([10]) == 10, 'Second, with a single stone'
    assert checkio([5, 8, 13, 27, 14]) == 3, 'Third'
    assert checkio([5,5,6,5]) == 1, 'Fourth'
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, 'Fifth'
    assert checkio([1, 1, 1, 3]) == 0, "Six, don't forget - you can hold different quantity of parts"
    print ('All is ok')
