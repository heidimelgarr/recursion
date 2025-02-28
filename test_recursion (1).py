"""
Recursion Test Suite
"""

import unittest
from recursion import (
    group_sum,
    group_sum_6,
    group_no_adj,
    group_sum_5,
    group_sum_clump,
    split_array,
    split_odd_10,
    split_53,
)


class TestGroupSum(unittest.TestCase):
    """Group Sum Tests"""

    def test_1(self):
        """group_sum(): Target sum formed by 2 and 8"""
        start = 0
        nums = [2, 4, 8]
        target = 10
        actual = group_sum(start, nums, target)
        expected = True
        self.assertEqual(actual, expected)

    def test_2(self):
        """group_sum(): Target sum cannot be formed"""
        start = 0
        nums = [2, 4, 8]
        target = 9
        actual = group_sum(start, nums, target)
        expected = False
        self.assertEqual(actual, expected)

    def test_3(self):
        """group_sum(): Target sum is last element"""
        start = 0
        nums = [2, 4, 8]
        target = 8
        actual = group_sum(start, nums, target)
        expected = True
        self.assertEqual(actual, expected)

    def test_4(self):
        """group_sum(): Target sum is last element, different start"""
        start = 1
        nums = [2, 4, 8]
        target = 8
        actual = group_sum(start, nums, target)
        expected = True
        self.assertEqual(actual, expected)

    def test_5(self):
        """group_sum(): 1 element, has target"""
        start = 0
        nums = [1]
        target = 1
        actual = group_sum(start, nums, target)
        expected = True
        self.assertEqual(actual, expected)

    def test_6(self):
        """group_sum(): Start is out of bounds"""
        start = 1
        nums = [9]
        target = 0
        actual = group_sum(start, nums, target)
        expected = True
        self.assertEqual(actual, expected)

    def test_7(self):
        """group_sum(): Empty list"""
        start = 0
        nums = []
        target = 0
        actual = group_sum(start, nums, target)
        expected = True
        self.assertEqual(actual, expected)


class TestGroupSum6(unittest.TestCase):
    """Group Sum 6 Tests"""

    def test_1(self):
        """group_sum_6(): Target sum formed by 6 and 2"""
        start = 0
        nums = [5, 6, 2]
        target = 8
        actual = group_sum_6(start, nums, target)
        expected = True
        self.assertEqual(actual, expected)

    def test_2(self):
        """group_sum_6(): Target sum cannot be formed"""
        start = 0
        nums = [5, 6, 2]
        target = 9
        actual = group_sum_6(start, nums, target)
        expected = False
        self.assertEqual(actual, expected)

    def test_3(self):
        """group_sum_6(): 1 element, has target"""
        start = 0
        nums = [1]
        target = 1
        actual = group_sum_6(start, nums, target)
        expected = True
        self.assertEqual(actual, expected)

    def test_4(self):
        """group_sum_6(): Empty list"""
        start = 0
        nums = []
        target = 0
        actual = group_sum_6(start, nums, target)
        expected = True
        self.assertEqual(actual, expected)

    def test_5(self):
        """group_sum_6(): Target sum can be formed by 2 and 6"""
        start = 0
        nums = [3, 2, 4, 6]
        target = 8
        actual = group_sum_6(start, nums, target)
        expected = True
        self.assertEqual(actual, expected)

    def test_6(self):
        """group_sum_6(): Target sum can be formed with both 6's"""
        start = 0
        nums = [1, 6, 2, 6, 4]
        target = 12
        actual = group_sum_6(start, nums, target)
        expected = True
        self.assertEqual(actual, expected)

    def test_7(self):
        """group_sum_6(): Target sum can be formed, but 6 not chosen"""
        start = 0
        nums = [1, 6, 2, 6, 4]
        target = 4
        actual = group_sum_6(start, nums, target)
        expected = False
        self.assertEqual(actual, expected)


class TestGroupNoAdj(unittest.TestCase):
    """Group No Adj Tests"""

    def test_1(self):
        """group_no_adj(): Target sum formed by 2 and 10"""
        start = 0
        nums = [2, 5, 10, 4]
        target = 12
        actual = group_no_adj(start, nums, target)
        expected = True
        self.assertEqual(actual, expected)

    def test_2(self):
        """group_no_adj(): Target sum would require adjacent numbers (10, 4)"""
        start = 0
        nums = [2, 5, 10, 4]
        target = 14
        actual = group_no_adj(start, nums, target)
        expected = False
        self.assertEqual(actual, expected)

    def test_3(self):
        """group_no_adj(): Target sum would require adjacent numbers (2, 5)"""
        start = 0
        nums = [2, 5, 10, 4]
        target = 7
        actual = group_no_adj(start, nums, target)
        expected = False
        self.assertEqual(actual, expected)

    def test_4(self):
        """group_no_adj(): Target sum can be formed by 5 and last 2"""
        start = 1
        nums = [2, 5, 10, 4, 2]
        target = 7
        actual = group_no_adj(start, nums, target)
        expected = True
        self.assertEqual(actual, expected)

    def test_5(self):
        """group_no_adj(): Empty list"""
        start = 0
        nums = []
        target = 0
        actual = group_no_adj(start, nums, target)
        expected = True
        self.assertEqual(actual, expected)

    def test_6(self):
        """group_no_adj(): 1 element, has target"""
        start = 0
        nums = [1]
        target = 1
        actual = group_no_adj(start, nums, target)
        expected = True
        self.assertEqual(actual, expected)

    def test_7(self):
        """group_no_adj(): 1 element, target is 0"""
        start = 0
        nums = [9]
        target = 0
        actual = group_no_adj(start, nums, target)
        expected = True
        self.assertEqual(actual, expected)

    def test_8(self):
        """group_no_adj(): Target sum excluded by start"""
        start = 2
        nums = [1, 2, 2, 3, 3]
        target = 6
        actual = group_no_adj(start, nums, target)
        expected = False
        self.assertEqual(actual, expected)


class TestGroupSum5(unittest.TestCase):
    """Group Sum 5 Tests"""

    def test_1(self):
        """group_sum_5(): Target sum can be formed by 5, 10, 4"""
        start = 0
        nums = [2, 5, 10, 4]
        target = 19
        actual = group_sum_5(start, nums, target)
        expected = True
        self.assertEqual(actual, expected)

    def test_2(self):
        """group_sum_5(): Target sum cannot be formed because 5 must be included"""
        start = 0
        nums = [2, 5, 10, 4]
        target = 12
        actual = group_sum_5(start, nums, target)
        expected = False
        self.assertEqual(actual, expected)

    def test_3(self):
        """group_sum_5(): Cannot form because 5 must be chosen and 1 cannot be chosen"""
        start = 0
        nums = [3, 5, 1]
        target = 4
        actual = group_sum_5(start, nums, target)
        expected = False
        self.assertEqual(actual, expected)

    def test_4(self):
        """group_sum_5(): 1 is after after 5 so 1 cannot be chosen"""
        start = 1
        nums = [3, 5, 1]
        target = 9
        actual = group_sum_5(start, nums, target)
        expected = False
        self.assertEqual(actual, expected)

    def test_5(self):
        """group_sum_5(): 1 element, has target"""
        start = 0
        nums = [1]
        target = 1
        actual = group_sum_5(start, nums, target)
        expected = True
        self.assertEqual(actual, expected)

    def test_6(self):
        """group_sum_5(): 1 element, target is 0"""
        start = 0
        nums = [9]
        target = 0
        actual = group_sum_5(start, nums, target)
        expected = True
        self.assertEqual(actual, expected)

    def test_7(self):
        """group_sum_5(): Empty list"""
        start = 0
        nums = []
        target = 0
        actual = group_sum_5(start, nums, target)
        expected = True
        self.assertEqual(actual, expected)


class TestGroupSumClump(unittest.TestCase):
    """Group Sum Clump Tests"""

    def test_1(self):
        """group_sum_clump(): Target sum formed by 2 and 8"""
        start = 0
        nums = [2, 4, 8]
        target = 10
        actual = group_sum_clump(start, nums, target)
        expected = True
        self.assertEqual(actual, expected)

    def test_2(self):
        """group_sum_clump(): Target sum formed, multiple possible combinations"""
        start = 0
        nums = [1, 2, 4, 8, 1]
        target = 14
        actual = group_sum_clump(start, nums, target)
        expected = True
        self.assertEqual(actual, expected)

    def test_3(self):
        """group_sum_clump(): Target sum cannot be formed"""
        start = 0
        nums = [2, 4, 4, 8]
        target = 14
        actual = group_sum_clump(start, nums, target)
        expected = False
        self.assertEqual(actual, expected)

    def test_4(self):
        """group_sum_clump(): Target sum can be formed by 8 and 2 clump"""
        start = 0
        nums = [8, 2, 2, 1]
        target = 12
        actual = group_sum_clump(start, nums, target)
        expected = True
        self.assertEqual(actual, expected)

    def test_5(self):
        """group_sum_clump(): Target sum cannot be formed with 2 clump"""
        start = 0
        nums = [8, 2, 2, 1]
        target = 11
        actual = group_sum_clump(start, nums, target)
        expected = False
        self.assertEqual(actual, expected)

    def test_6(self):
        """group_sum_clump(): 1 element, has target"""
        start = 0
        nums = [1]
        target = 0
        actual = group_sum_clump(start, nums, target)
        expected = True
        self.assertEqual(actual, expected)

    def test_7(self):
        """group_sum_clump(): Target sum is 9 but must pick all 9's"""
        start = 0
        nums = [7, 8, 9, 9, 9]
        target = 9
        actual = group_sum_clump(start, nums, target)
        expected = False
        self.assertEqual(actual, expected)

    def test_8(self):
        """group_sum_clump(): Target sum is 9, start allows to pick 1 9"""
        start = 3
        nums = [7, 8, 9, 9, 8]
        target = 9
        actual = group_sum_clump(start, nums, target)
        expected = True
        self.assertEqual(actual, expected)


class TestSplitArray(unittest.TestCase):
    """Split Array Tests"""

    def test_1(self):
        """split_array(): Even split, both groups equal sum"""
        nums = [2, 2]
        actual = split_array(nums)
        expected = True
        self.assertEqual(actual, expected)

    def test_2(self):
        """split_array(): Uneven split"""
        nums = [2, 3]
        actual = split_array(nums)
        expected = False
        self.assertEqual(actual, expected)

    def test_3(self):
        """split_array(): Able to split, both groups sum to 5"""
        nums = [2, 5, 3]
        actual = split_array(nums)
        expected = True
        self.assertEqual(actual, expected)

    def test_4(self):
        """split_array(): Even split"""
        nums = [1, 1, 1, 1, 1, 1]
        actual = split_array(nums)
        expected = True
        self.assertEqual(actual, expected)

    def test_5(self):
        """split_array(): Uneven split"""
        nums = [1, 1, 1, 1, 1]
        actual = split_array(nums)
        expected = False
        self.assertEqual(actual, expected)

    def test_6(self):
        """split_array(): Empty list"""
        nums = []
        actual = split_array(nums)
        expected = True
        self.assertEqual(actual, expected)

    def test_7(self):
        """split_array(): 1 number"""
        nums = [1]
        actual = split_array(nums)
        expected = False
        self.assertEqual(actual, expected)

    def test_8(self):
        """split_array(): Uneven split"""
        nums = [3, 5]
        actual = split_array(nums)
        expected = False
        self.assertEqual(actual, expected)


class TestSplitOdd10(unittest.TestCase):
    """Split Odd 10 Tests"""

    def test_1(self):
        """split_odd_10(): Able to split, sides sum to 10 and 5"""
        nums = [5, 5, 5]
        actual = split_odd_10(nums)
        expected = True
        self.assertEqual(actual, expected)

    def test_2(self):
        """split_odd_10(): Unable to split, one side is even and other side is 10"""
        nums = [5, 5, 6]
        actual = split_odd_10(nums)
        expected = False
        self.assertEqual(actual, expected)

    def test_3(self):
        """split_odd_10(): Able to split, results in one side being 7 and one side being 10"""
        nums = [5, 5, 6, 1]
        actual = split_odd_10(nums)
        expected = True
        self.assertEqual(actual, expected)

    def test_4(self):
        """split_odd_10(): Able to split, results in one side being 7 and one side being 10"""
        nums = [6, 5, 5, 1]
        actual = split_odd_10(nums)
        expected = True
        self.assertEqual(actual, expected)

    def test_5(self):
        """split_odd_10(): Unable to split, one side is 12 and other side is 10"""
        nums = [6, 5, 5, 5, 1]
        actual = split_odd_10(nums)
        expected = False
        self.assertEqual(actual, expected)

    def test_6(self):
        """split_odd_10(): Able to split, one side is 1 and other side sums to 0"""
        nums = [1]
        actual = split_odd_10(nums)
        expected = True
        self.assertEqual(actual, expected)

    def test_7(self):
        """split_odd_10(): Empty list"""
        nums = []
        actual = split_odd_10(nums)
        expected = False
        self.assertEqual(actual, expected)


class TestSplit53(unittest.TestCase):
    """Split 53 Tests"""

    def test_1(self):
        """split_53(): Able to split, both groups equal in sum"""
        nums = [1, 1]
        actual = split_53(nums)
        expected = True
        self.assertEqual(actual, expected)

    def test_2(self):
        """split_53(): Unable to split, both groups not equal in sum"""
        nums = [1, 1, 1]
        actual = split_53(nums)
        expected = False
        self.assertEqual(actual, expected)

    def test_3(self):
        """split_53(): Able to split, both groups equal in sum (4)"""
        nums = [2, 4, 2]
        actual = split_53(nums)
        expected = True
        self.assertEqual(actual, expected)

    def test_4(self):
        """split_53(): Unable to split, both groups not equal in sum"""
        nums = [2, 2, 2, 1]
        actual = split_53(nums)
        expected = False
        self.assertEqual(actual, expected)

    def test_5(self):
        """split_53(): Able to split, [5, 1], [3, 3]"""
        nums = [3, 3, 5, 1]
        actual = split_53(nums)
        expected = True
        self.assertEqual(actual, expected)

    def test_6(self):
        """split_53(): Unable to split, multiples of 3 and 5 cannot be in the same split"""
        nums = [3, 5, 8]
        actual = split_53(nums)
        expected = False
        self.assertEqual(actual, expected)

    def test_7(self):
        """split_53(): Able to split"""
        nums = [2, 4, 6]
        actual = split_53(nums)
        expected = True
        self.assertEqual(actual, expected)

    def test_8(self):
        """split_53(): Empty list"""
        nums = []
        actual = split_53(nums)
        expected = True
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
