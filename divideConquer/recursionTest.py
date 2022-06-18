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
        a = [1,3,4,5,6,7,8,9]
        result = search(a, 9)
        self.assertEqual(7,result,"finds that the target is in the 7th element")
if __name__ == '__main__':
    unittest.main()