import bisect

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """        
        def no_smaller_elements(x):
            l1_min = bisect.bisect_left(nums1, x)
            l2_min = bisect.bisect_left(nums2, x)
            l1_max = bisect.bisect_right(nums1, x)
            l2_max = bisect.bisect_right(nums2, x)
            print("there are between", l1_min + l2_min, "and", l1_max + l2_max - 1, "elements smaller than", x)
            return l1_min + l2_min, l1_max + l2_max - 1
        
        def search(l, total):
            if len(l) == 0:
                return -1, None
            
            lo = 0
            hi = len(l) - 1
            
            offset = (total+1) % 2
            # print("offset", offset)
            while lo <= hi:
                mid = (lo + hi) // 2
                n_min, n_max = no_smaller_elements(l[mid])
                min_diff = (n_min * 2) - (total - 1)
                max_diff = (n_max * 2) - (total - 1)
                print("the size difference between partitions is between", min_diff, "and", max_diff)
                if max_diff < -offset:
                    lo = mid + 1
                    print("new lo", lo)
                elif min_diff > offset:
                    hi = mid - 1
                    print("new hi", hi)
                else:
                    print("solution.", mid, min_diff, max_diff)
                    return mid, -(min(min_diff, max_diff, key=abs))
            return -1, None
        
        total = len(nums1) + len(nums2)
        
        element1, e1_diff = search(nums1, total)
        element2, e2_diff = search(nums2, total)
        print("first element", element1, "diff", e1_diff)
        print("second element", element2, "diff", e2_diff)
        if element2 == -1:
            if total % 2 == 1:
                return nums1[element1]
            else:
                return (nums1[element1] + nums1[element1 + e1_diff]) / 2
        elif element1 == -1:
            if total % 2 == 1:
                return nums2[element2]
            else:
                return (nums2[element2] + nums2[element2 + e2_diff]) / 2
        else:
            if total % 2 == 1 or nums1[element1] != nums2[element2]:
                return (nums1[element1] + nums2[element2]) / 2
            else:
                offset = nums1[element1]
                if element1 < len(nums1) - e1_diff and element2 < len(nums2) - e2_diff:
                    offset = min(nums1[element1 + e1_diff], nums2[element2 + e2_diff])
                return (nums1[element1] + offset) / 2
    
a = [1,2]
b = [1,2]

c = Solution()
print(c.findMedianSortedArrays(a,b))
    
