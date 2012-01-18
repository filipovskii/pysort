from pysort import heap
from ._common import CommonSortTestCase

import unittest

class HeapSortTest(unittest.TestCase, CommonSortTestCase):
    sorter = heap

    def test_max_heapify(self):
        a = [2, 4, 3]
        heap.max_heapify(a, 0)
        self.assertEqual([4, 2, 3], a)

