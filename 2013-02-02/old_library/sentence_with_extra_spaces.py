def checkio(string):
    'return sentence without extra spaces'
    return " ".join(filter(len,string.split(" ")))
    
if __name__ == '__main__':
    assert checkio('I  like   python') == "I like python", 'First'
    print('All ok')
        
