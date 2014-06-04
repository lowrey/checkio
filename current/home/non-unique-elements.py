def checkio(data):
    def unique(l):
        for n in l:
            if len(list(x for x in l if x == n)) == 1:
                yield n
    return list(filter(lambda x: not x in unique(data), data))


#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#or remove elements from original list (but it's bad practice for many real cases)
#Loop over original list


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(checkio([1]), list), "The result must be a list"
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"
