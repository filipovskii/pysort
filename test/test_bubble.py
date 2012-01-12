from pysort import bubble
from ._common import CommonSortTestCase

import unittest

class BubbleSortTest(unittest.TestCase, CommonSortTestCase):
    sorter = bubble
