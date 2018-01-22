# Writing a function that can find the position of first substring of a string
# find_substring('hello, trinity', 'tri') == 6

def find_substring(string, sub):
        """
        :type string: str
        :type sub: str
        :rtype: int
        """
        return string.find(sub)

assert find_substring("hello, trinity", "tri") == 7
assert find_substring("hello, trinity", "yaping") == -1
assert find_substring("", "tri") == -1
