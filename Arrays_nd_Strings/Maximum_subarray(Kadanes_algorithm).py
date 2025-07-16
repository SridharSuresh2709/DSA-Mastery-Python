class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxEle = float('-inf')
        sum = 0
        for i in range(len(nums)):
            sum = sum + nums[i]
            if sum > maxEle:
                maxEle = sum
            if sum < 0:
                sum = 0
        return maxEle
        