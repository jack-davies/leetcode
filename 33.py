class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        This is a naive solution: the following two steps
        could be combined into a single search.
        """
        # Find the pivot
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[left] <= nums[mid] and nums[mid] >= nums[right]:
                # Pivot is > mid point
                left = mid + 1
                continue
            elif nums[left] >= nums[mid] and nums[mid] <= nums[right]:
                # Pivot is <= mid point
                right = mid
                continue
            break

        pivot = left

        # binary search about pivot
        def mv(i: int):
            return (i + pivot) % len(nums)

        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mv(mid)] < target:
                left = mid + 1
            elif nums[mv(mid)] > target:
                right = mid - 1
            else:
                return mv(mid)

        return -1
