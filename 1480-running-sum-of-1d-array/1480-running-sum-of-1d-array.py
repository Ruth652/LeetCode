class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        accumulator=0
        for i in range(len(nums)):
            accumulator+=nums[i]
            nums[i]=accumulator
        return nums
        