# Writing a function that can find the position of first substring of a string
# find_substring('hello, trinity', 'tri') == 6

def find_substring(string, sub):
    """
    :type string: str
    :type sub: str
    :rtype: int
    """
    index = 0
    if sub and sub in string:
        c = sub[0]
        for s in string:
            if s == c:
                if string[index:index + len(sub)] == sub:
                    return index
            index += 1
    elif not sub:
        return 0
    else:
        return -1


assert find_substring("hello, trinity", "tri") == "hello, trinity".find("tri")
assert find_substring("hello, trinity", "as") == "hello, trinity".find("as")
assert find_substring("hello, trinity", "") == "hello, trinity".find("")
assert find_substring("", "tri") == "".find("tri")