def checkio(text):
    letters = {}
    for c in filter(str.isalpha, text.lower()):
        if c not in letters:
            letters[c] = 1
        else:
            letters[c] += 1
    sortedl = sorted(letters.items(), key=lambda x: x[1])
    maxval = sortedl[-1][1]
    maxvals = filter(lambda i: i[1] == maxval, sortedl)
    return sorted(maxvals)[0][0]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
