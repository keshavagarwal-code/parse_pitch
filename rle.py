def add_to_result(_temp):
    rslt = ""
    prev_elem = list(_temp.keys())[0]
    if _temp[prev_elem] >= 1:
        rslt += str(_temp[prev_elem] + 1) + prev_elem
    else:
        rslt += prev_elem
    _temp = {}
    return rslt

def rle(inp):
    '''
    add consecutive elements to hashmap(dict) and update count
    if next element not in dict and count >= 1 add to reesult
    else, only add count
    '''
    result = ""
    _temp = {}
    for i in inp:
        if i in _temp:
            _temp[i] += 1
        else:
            if not _temp:
                _temp[i] = 0
            else:
                result += add_to_result(_temp)
                _temp = {}
                _temp[i] = 0
    if _temp:
        result += add_to_result(_temp)
    return result

if __name__ == '__main__':
    assert rle('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB') == "12WB12W3B24WB"
    assert rle('AABBBCCCC') == "2A3B4C"
    assert rle('') == ""
    assert rle('XYZ') == "XYZ"
    assert rle('  hsqq qww  ') == "2 hs2q q2w2 "