class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums) - 1

        while lower < upper:
            current = (lower + upper) // 2
            if nums[current] < target:
                lower = current + 1
            elif nums[current] > target:
                upper = current - 1
            else:
                return current

        # lower >= upper
        if nums[lower] >= target:
            return lower
        return lower + 1
