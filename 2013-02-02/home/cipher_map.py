def associate_string(cipher_str, data_str):
    ret_dict = []
    for i in range(len(cipher_str)):
        if cipher_str[i] == 'X':
            ret_dict.append((True, data_str[i]))
        else:
            ret_dict.append((False, data_str[i]))
    return ret_dict

def transform(cipher, data):
    ret_array = []
    for i in range(len(cipher)):
        ret_array.append(associate_string(cipher[i], data[i]))
    return ret_array
    
def get_chars(data):
    ret_chars = ''
    for line in data:
        for char_tuple in line:
            if char_tuple[0]:
                ret_chars += char_tuple[1]
    return ret_chars
    
def turn_keys(data):
    new_bool_data = []
    for i in range(len(data[0])):
        new_char_list = []
        for char_list in data:
            new_char_list.append(char_list[i][0])
        new_char_list.reverse()
        new_bool_data.append(new_char_list)
    new_data = []
    for i in range(len(data)):
        new_char_list = []
        for j in range(len(char_list)):
            new_char_list.append((new_bool_data[i][j], data[i][j][1]))
        new_data.append(new_char_list)
    
    return new_data

def checkio(input_data):
    'Return password of given cipher map'
    ret_chars = ''
    data = transform(input_data[0],input_data[1])
    ret_chars += get_chars(data)
    for i in range(len(data)-1):
        data = turn_keys(data)
        ret_chars += get_chars(data)
    print ret_chars
    return ret_chars
    

if __name__ == '__main__':
    assert checkio([[
    'X...',
    '..X.',
    'X..X',
    '....'],[
    'itdf',
    'gdce',
    'aton',
    'qrdi']]) == 'icantforgetiddqd', 'First'

    assert checkio( [[
    '....',
    'X..X',
    '.X..',
    '...X'],[
    'xhwc',
    'rsqx',
    'xqzz',
    'fyzr']]) == 'rxqrwsfzxqxzhczy', 'Second'
    print('All ok')
