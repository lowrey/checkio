def unlist(inlist, outlist):
    for item in inlist:
        if isinstance(item, list):
            unlist(item, outlist)
        else:
            outlist.append(item)
    return outlist

def checkio(arr):
    'convert all elements in arr in one row'
    return unlist(arr,[])

if __name__ == '__main__':
    assert checkio([1,2,3]) == [1,2,3], 'First'
    assert checkio([1,[2,2,2],4]) == [1,2,2,2,4], 'Second'
    assert checkio([[[2]],[4,[5,6,[6],6,6,6],7]])\
                              == [2,4,5,6,6,6,6,6,7], 'Third'
    print('All ok')
