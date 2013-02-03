def checkio(number):
    'return roman numeral using the specified integer value from range 1...3999'
    ret = ""
    numerals = (('M',1000),('CM',900),('D',500),('CD',400),('C',100),('XC',90),('L',50),('XL',40),('X',10),('IX',9),('V',5),('IV',4),('I', 1))
    for num_pair in numerals:
        numeral, val = num_pair
        x, rem = divmod(number, val)
        for _ in range(x):
            ret += numeral
            number -= val
    return ret    
    
if __name__ == '__main__':
    assert checkio(6) == 'VI', 'First'
    assert checkio(76) == 'LXXVI', 'Second'
    assert checkio(499) == 'CDXCIX', 'Third'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', 'Fourth'
    print('All ok')
