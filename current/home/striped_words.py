VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    def is_vowel(c):
        return c.upper() in VOWELS
    def is_striped(w):
        if len(w) < 2:
            return False
        s = is_vowel(w[0])
        for c in w[1:]:
            if not c.isalpha:
                continue
            if s == is_vowel(c): return False
            s = not s
        return True
    c = 0
    import re
    for w in re.split('\s|(?<!\d)[,.]|[,.](?!\d)', text):
        if is_striped(w):
            c += 1
    return c

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
