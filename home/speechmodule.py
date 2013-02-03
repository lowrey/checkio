def digit_to_str(digit):
    return {
        1: 'one',
        2 : 'two',
        3 : 'three',
        4 : 'four',
        5 : 'five',
        6 : 'six',
        7 : 'seven',
        8 : 'eight',
        9 : 'nine',
        0 : 'zero'
    }[digit]

def tens_to_str(digit):
    return {
        2 : 'twenty',
        3 : 'thirty',
        4 : 'forty',
        5 : 'fifty',
        6 : 'sixty',
        7 : 'seventy',
        8 : 'eighty',
        9 : 'ninety',
    }[digit]

def teens_to_str(digit):
    return {
        11: 'eleven',
        12 : 'twelve',
        13 : 'thirteen',
        14 : 'fourteen',
        15 : 'fifteen',
        16 : 'sixteen',
        17 : 'seventeen',
        18 : 'eighteen',
        19 : 'nineteen',
        10 : 'ten'
    }[digit]

def checkio(number):
    str_rep = ''
    if (number > 1000) or (number < 0):
        return str_rep
    elif number == 1000:
        return 'one thousand'
    if (number / 100) >= 1:
        digit =  int((number / 100))
        str_rep += "{} hundred ".format(digit_to_str(digit))
        number -= digit * 100
    if (number / 10) >= 2:
        digit =  int((number / 10))
        str_rep += "{} ".format(tens_to_str(digit))
        number -= digit * 10
        if number == 0:
            str_rep.rstrip()
            return str_rep 
    elif (number / 10) >= 1:
        str_rep += teens_to_str(number)
        return str_rep
    str_rep += digit_to_str(number)
    return str_rep

if __name__ == '__main__':
    assert checkio(4) == 'four', "First"
    assert checkio(133) == 'one hundred thirty three', "Second"
    assert checkio(12)=='twelve', "Third"
    assert checkio(101)=='one hundred one', "Fifth"
    assert checkio(212)=="two hundred twelve", "Sixth"
    assert checkio(40)=='forty', "Seventh, forty - it is correct"
    print('All ok')
