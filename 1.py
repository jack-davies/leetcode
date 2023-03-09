class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        order = sorted(range(len(nums)), key=nums.__getitem__)
        nums.sort()
        i = 0
        j = len(nums) - 1
        while True:
            current = nums[i] + nums[j]
            if current < target:
                i += 1
            elif current > target:
                j -= 1
            else:
                return [order[i], order[j]]
