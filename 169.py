class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Boyer-Moore majority vote algorithm
        """

        count = 0
        for i in range(len(nums)):
            if count == 0:
                candidate = nums[i]
                count += 1
            else:
                if nums[i] == candidate:
                    count += 1
                else:
                    count -= 1
        return candidate
