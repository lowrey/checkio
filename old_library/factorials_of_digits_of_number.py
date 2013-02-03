def checkio(data):
    'calculate sum of the factorials for all digits of the specified positive integer number.'
    from math import factorial 
    fact_sum = 0
    for digit in str(data):
        fact_sum += factorial(int(digit))
    return fact_sum
	
    
if __name__ == '__main__':
    assert checkio(100) == 3, 'First'
    assert checkio(222) == 6, 'Second'
    assert checkio(1234) == 33, 'Third'
    print 'All ok'
