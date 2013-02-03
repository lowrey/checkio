def checkio(txt):
    '''
    string with dot separated numbers, which inserted after every third digit from right to left
    '''
    words = txt.split(" ")
    output = []
    for word in words:
        if word.isdigit():
            new_word = ""
            count = 0
            for i in reversed((range(len(word)))):
                new_word = word[i] + new_word
                count += 1
                if ((count % 3) == 0) and i != 0:
                    new_word = "." + new_word
            output.append(new_word)
        else:
            output.append(word)
    output = " ".join(output)
    return output
                

if __name__ == '__main__':
    assert checkio('123456') == '123.456'
    assert checkio('333') == '333'
    assert checkio('9999999') == '9.999.999'
    assert checkio('123456 567890') == '123.456 567.890'
    assert checkio('price is 5799') == 'price is 5.799'
    assert checkio('he was born in 1966th') == 'he was born in 1966th'
    print('All ok')
