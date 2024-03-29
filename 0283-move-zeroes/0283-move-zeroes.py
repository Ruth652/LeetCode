class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i==0:
                nums.remove(i)
                nums.append(i)
    """
    cclass Solution(object):
    def moveZeroes(self, nums):
       
        for i in range(len(nums)):
            if nums[i]==0
            nums[i+1],nums[i]=nums[i],nums[i+1]
            
"""