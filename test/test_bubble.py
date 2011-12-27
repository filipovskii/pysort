from pysort import bubble
import unittest

class BubbleSortTest(unittest.TestCase):

    def test_simple_sort(self):
        a = [2,4,1,3,7,3]
        print(a)

        bubble.sort(a)
        print(a)

        self.assertEqual(a, [1,2,3,3,4,7])

    def test_no_elements(self):
        a = []

        bubble.sort(a)
        
        self.assertEqual(a, [])
