class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            x = target - nums[i]

            if x in nums:
                if nums.index(x) == i:
                    continue
                return [i, nums.index(x)]