from pysort import insertion
from ._common import CommonSortTestCase

import unittest

class InsertionSortTest(unittest.TestCase, CommonSortTestCase):
    sorter = insertion

