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
        n = len(nums)

        solutions = set()
        for _a in range(n - 3):
            for _b in range(_a + 1, n - 2):
                _c, _d = _b + 1, n - 1
                ab = nums[_a] + nums[_b]
                # skip the following cases
                if ((ab + nums[_c] + nums[_c + 1] > target) or
                    (ab + nums[_d] + nums[_d - 1] < target)):
                    continue

                while _c < _d:
                    t_cd = target - nums[_c] - nums[_d]
                    if ab < t_cd:
                        _c += 1
                    elif ab > t_cd:
                        _d -= 1
                    else:
                        solutions.add((nums[_a], nums[_b], nums[_c], nums[_d]))
                        _c += 1

        return list(solutions)
