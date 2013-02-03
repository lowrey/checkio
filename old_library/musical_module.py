def checkio(values):
    'Calculate the greatest common divisor of two numbers'
    a, b = values    
    gcd = 1
    for i in range(1,min(a,b)+1):
        if (a % i) == 0 and (b % i) == 0:
            gcd = i
    return gcd

if __name__ == '__main__':
    assert checkio((12, 8)) == 4, "First"
    assert checkio((14, 21)) == 7, "Second"
    print('All ok')
    

