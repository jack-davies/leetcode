class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def sortFrom(idx):
            """
            Bubble sort. Sorry bout it!
            """
            for i in range(idx, len(nums)):
                for j in range(i, len(nums)):
                    if nums[j] < nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]

        def insert(i: int, j: int):
            bumped = nums[i]
            while j <= i:
                print(j, nums, bumped)
                nums[j], bumped = bumped, nums[j]
                j += 1

        for i in range(len(nums)-1, -1, -1):
            for j in range(len(nums)-1, i, -1):
                if nums[j] > nums[i]:
                    insert(j, i)
                    sortFrom(i+1)
                    return

        sortFrom(0)
