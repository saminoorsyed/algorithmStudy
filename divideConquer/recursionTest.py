# test recursive functions
# by Sami Syed

#imports
import recursion
import unittest

class RecursionTests(unittest.TestCase):
    #test divide search
    def test_BinarySearch(self):
        arr = [1,2,12,22,96,105,600]
        result = recursion.search(arr, 12)
        self.assertEqual(2, result, "finds that the target is the 4th element")

if __name__ == '__main__':
    unittest.main()