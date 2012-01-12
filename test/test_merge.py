from pysort import merge
from ._common import CommonSortTestCase

import unittest

class MergeSortTest(unittest.TestCase, CommonSortTestCase):
    sorter = merge
