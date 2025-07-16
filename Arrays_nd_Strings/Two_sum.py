class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}  # num : i 
        for i , num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target - num] , i]
            hashmap[num] = i 
        return []
    