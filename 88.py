class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1_ = nums1[:m]

        i, i_1, i_2 = 0, 0, 0
        while i < m + n:
            if i_2 >= n or (i_1 < m and nums1_[i_1] <= nums2[i_2]):
                nums1[i] = nums1_[i_1]
                i_1 += 1
            else:
                nums1[i] = nums2[i_2]
                i_2 += 1
            i += 1
