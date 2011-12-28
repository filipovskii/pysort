from pysort import bubble
from ._common import CommonSortTestCase

import unittest
import inspect

class BubbleSortTest(unittest.TestCase, CommonSortTestCase):
    sorter = bubble
