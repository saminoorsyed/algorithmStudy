# test recursive functions
# by Sami Syed

#imports
import recursion
import unittest

class RecursionTests(unittest.TestCase):
    #test divide search
    def test_divideSearch(self):
        arr = [1,2,45,36,12,96]
        result = recursion.divide_search(arr,12)
        self.assertEqual(4, result, "finds that the target is the 4th element")

if __name__ == '__main__':
    unittest.main()