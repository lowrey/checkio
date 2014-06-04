def checkio(n):
    '''
    Let G(S) denote the sum of the elements of set S and F(n) be the sum of G(s) 
    for all subsets of the set consisting of the first n natural numbers. 
    For example, F(3) = (1) + (2) + (3) + (1 + 2) + (1 + 3) + (2 + 3) + (1 + 2 + 3) = 24. 
    Given n, calculate F(1) + F(2) + ... + F(n)
    '''
    from itertools import combinations
    n_sum = 0
    for f in range(n):
        f_list = [x + 1 for x in range(f+1)]
        for i in range(f+1):   
            for j in combinations(f_list, (i+1)):
                n_sum += sum(j)          
    return n_sum

if __name__ == '__main__':
    #assert checkio(2) == 7, "First"
    assert checkio(3) == 31, "Second"
    assert checkio(1) == 1, "Third"
    print('All ok')
