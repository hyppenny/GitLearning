# Writing a function that can find the position of first substring of a string
# find_substring('hello, trinity', 'tri') == 6

import unittest


def find_substring(string, sub):
    """
    :type string: str
    :type sub: str
    :rtype: int
    """
    if not sub:
        return 0

    for i in range(0, len(string) - len(sub) + 1):
        match = True
        for j in range(0, len(sub)):
            if string[i + j] != sub[j]:
                match = False
                break
        if match:
            return i
    return -1


class TestFindSubstring(unittest.TestCase):

    def test(self):
        self.assertEqual(find_substring('hello, trinity, trinity college', 'tri'), 7)
        self.assertEqual(find_substring('hello, tronity, trinity college', 'trinity '), 16)
        self.assertEqual(find_substring('hello, trnity', 'tri'), -1)

    def test_boundary(self):
        self.assertEqual(find_substring('', '12'), -1)
        self.assertEqual(find_substring('', ''), 0)
        self.assertEqual(find_substring('121', ''), 0)
