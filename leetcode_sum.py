class Solution(object):

    def __init__(self,nums,target):
        self.nums=nums
        self.target=target
    def twoSum(self):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #nums = [1, 2, 3, 4]
        #target = 4
        i = 0
        j = 1

        for i in range(len(self.nums)):
            for j in range(i + 1, len(self.nums)):
                mysum = self.nums[i] + self.nums[j]
                print(i, j)
                if mysum == self.target:
                    return i,j