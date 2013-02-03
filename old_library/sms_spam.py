def checkio(line):
    '''
    Output a single number representing the cost of the given slogan, according to Petr's pricing.
    '''
    cost = 0
    keys = ('abc','def','ghi','jkl','mno','pqr','stu','vwx','yz','.,!',' ')
    for char in line:
        for key in keys:
            if char in key:                
                cost += key.find(char) + 1
    return cost
                

if __name__ == '__main__':
    assert checkio('diamonds are forever') == 38, 'First'
    assert checkio('just do it') == 18, 'Second'
    assert checkio('tastes great, less filling') == 48, 'Third'
    print('All is ok')
