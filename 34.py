class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(target):
            l, mid, r = 0, 0, len(nums)-1
            found = False
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                if nums[mid] > target:
                    r = mid - 1
                if nums[mid] == target:
                    found = True
                    break
            return [found, l, mid, r]

        found, *_ = binarySearch(target)
        if not found:
            return [-1, -1]

        _, first, *_ = binarySearch(target - 0.5)
        _, *_, last = binarySearch(target + 0.5)
        return [first, last]
