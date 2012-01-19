from pysort import quick
from ._common import CommonSortTestCase

import unittest

class QuickSortTest(unittest.TestCase, CommonSortTestCase):
    sorter = quick
