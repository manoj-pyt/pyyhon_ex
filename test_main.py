import unittest
import leetcode_sum


class MyTestCase(unittest.TestCase):
    def test_something(self):
        nums = [1, 2, 3, 4]
        target = 4
        expected = [0, 2]

        actual = leetcode_sum.Solution.twoSum(self, nums, target)
        print(actual)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
