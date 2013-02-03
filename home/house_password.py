def checkio(data):
    'Return True if password strong and False if not'
    if len(data) < 10:
        return False
    contains = { 'digit': False, 'upper': False, 'lower': False }
    for char in data:
        if char.isdigit():
            contains['digit'] = True
        if char.isupper():
            contains['upper'] = True
        if char.islower():
            contains['lower'] = True
    for v in contains.values():
        if not v:
            return False
    return True

if __name__ == '__main__':
    assert checkio('A1213pokl')==False, 'First'
    assert checkio('bAse730onE4')==True, 'Second'
    assert checkio('asasasasasasasaas')==False, 'Third'
    assert checkio('QWERTYqwerty')==False, 'Fourth'
    assert checkio('123456123456')==False, 'Fifth'
    assert checkio('QwErTy911poqqqq')==True, 'Sixth'
    print('All ok')
