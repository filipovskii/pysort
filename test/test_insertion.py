from pysort import insertion
import unittest

class InsertionSortTest(unittest.TestCase):

    def test_simple_sort(self):
        a = [3,5,4,1,7]
        insertion.sort(a)

        self.assertEqual([1,3,4,5,7], a)

if __name__ == '__main__':
  unittest.main()
