class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        def xor(nums: List[int]):
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 2:
                return nums[0] ^ nums[1]
            return xor(nums[:len(nums)//2]) ^ xor(nums[len(nums)//2:])

        return xor(nums)
