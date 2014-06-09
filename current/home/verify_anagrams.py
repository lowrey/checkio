def verify_anagrams(first_word, second_word):
    second_word = "".join(second_word.lower().split(" "))
    for c in "".join(first_word.lower().split(" ")):
        pos = second_word.find(c)
        if pos < 0:
            return False
        second_word = second_word[:pos] + second_word[pos+1:]
    if second_word == "":
        return True
    return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"
