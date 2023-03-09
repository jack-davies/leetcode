class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []

        nums.sort()

        ab_sum = {}
        for _a in range(len(nums)):
            for _b in range(_a+1, len(nums)):
                ab = nums[_a] + nums[_b]
                if ab in ab_sum:
                    ab_sum[ab].append((_a, _b))
                else:
                    ab_sum[ab] = ([(_a, _b)])

        # a + b = target - (c + d)
        solutions = set()
        for _c in range(len(nums)):
            for _d in range(_c+1, len(nums)):
                t_cd = target - (nums[_c] + nums[_d])
                if t_cd in ab_sum:
                    for (_a, _b) in ab_sum[t_cd]:
                        if _b < _c:
                            solutions.add((nums[_a], nums[_b], nums[_c], nums[_d]))

        return(list(solutions))
