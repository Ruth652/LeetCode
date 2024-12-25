class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        next_greater = {}
        stack = []

        for i in range(len(nums2)-1,-1,-1):
            while stack and stack[-1]<=nums2[i]:
                stack.pop()
            
            next_greater[nums2[i]]= stack[-1] if stack else -1
            stack.append(nums2[i])
        return [next_greater[nums] for nums in nums1]
