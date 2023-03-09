class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        final = False

        def bump(num: int):
            if num == len(nums):
                return True
            elif 0 < num < len(nums):
                if nums[num] != num:
                    bumped, nums[num] = nums[num], num
                    return False or bump(bumped)

        for num in nums:
            if bump(num):
                final = True

        for i in range(1, len(nums)):
            if nums[i] != i:
                return i
        if final:
            return len(nums) + 1
        return len(nums)
