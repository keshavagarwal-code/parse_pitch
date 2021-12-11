def rle2(inp):
    '''
    create a prev element and count variable
    if the variable is the same as previous increase count else append to result
    '''
    result = ""
    if inp:
        _prev = inp[0]
        _count = 1
    else:
        return ""
    
    for i in inp[1:]:
        if i == _prev:
            _count += 1
        else:
            if _count > 1:
                result += str(_count) + _prev
            else:
                result += _prev
            _prev = i
            _count = 1
    if _count:
        if _count > 1:
            result += str(_count) + _prev
        else:
            result += _prev

    return result

if __name__ == '__main__':
    assert rle2('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB') == "12WB12W3B24WB"
    assert rle2('AABBBCCCC') == "2A3B4C"
    assert rle2('') == ""
    assert rle2('XYZ') == "XYZ"
    assert rle2('  hsqq qww  ') == "2 hs2q q2w2 "