from collections import Counter

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        counts = Counter(nums)
        nums = []
        for count in counts:
            nums += [count] * min(counts[count], 4)
        nums.sort()
            
        # a + b + c + d = target
        # a + b = target - c - d
        
        # let z = (i, j, target - c - d), i != j
        # then we are solving a + b = target - c - d with k, l != i, j
        z_vals = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                z_vals.append((i, j, target - nums[i] - nums[j]))
        

        solutions = set()
        for i, j, z in z_vals:
            left = 0
            right = len(nums) - 1
            while left < right:
                # left!=right is taken care of
                # need to check left=i, left!=j, right!=i, right!=j
                ab = nums[left] + nums[right]
                if ab > z or right == i or right == j:
                    right -= 1
                elif ab < z or left == i or left == j:
                    left += 1
                else:
                    # boutique sorting solution! 
                    # must be sorted so that set ignores duplicates
                    # we know nums[left] <= nums[right] and nums[i] <= nums[j]
                    a, b, c, d = nums[left], nums[right], nums[i], nums[j]
                    
                    # a <= b, c <= d
                    if a <= c:
                        # a <= b, a <= c, a <= d, c <= d
                        # so a is first char
                        # options are a b c d, a c b d, a c d b
                        if b <= c:
                            # b is second char
                            solutions.add((a, b, c, d))
                        else:
                            # a c b d, a c d b
                            if b <= d:
                                solutions.add((a, c, b, d))
                            else:
                                solutions.add((a, c, d, b))
                    else:
                        # a <= b, c <= d, c < a, c < b
                        # so c is first char
                        # options are c d a b, c a d b, c a b d
                        if d <= a:
                            solutions.add((c, d, a, b))
                        else:
                            # c a d b, c a b d
                            if d <= b:
                                solutions.add((c, a, d, b))
                            else:
                                solutions.add((c, a, b, d))
                    
                    right -= 1
        
        return list(solutions)
        
a = Solution()
print(a.fourSum([1, 0, -1, 0, -2, 2], 0))
print(a.fourSum([91277418,66271374,38763793,4092006,11415077,60468277,1122637,72398035,-62267800,22082642,60359529,-16540633,92671879,-64462734,-55855043,-40899846,88007957,-57387813,-49552230,-96789394,18318594,-3246760,-44346548,-21370279,42493875,25185969,83216261,-70078020,-53687927,-76072023,-65863359,-61708176,-29175835,85675811,-80575807,-92211746,44755622,-23368379,23619674,-749263,-40707953,-68966953,72694581,-52328726,-78618474,40958224,-2921736,-55902268,-74278762,63342010,29076029,58781716,56045007,-67966567,-79405127,-45778231,-47167435,1586413,-58822903,-51277270,87348634,-86955956,-47418266,74884315,-36952674,-29067969,-98812826,-44893101,-22516153,-34522513,34091871,-79583480,47562301,6154068,87601405,-48859327,-2183204,17736781,31189878,-23814871,-35880166,39204002,93248899,-42067196,-49473145,-75235452,-61923200,64824322,-88505198,20903451,-80926102,56089387,-58094433,37743524,-71480010,-14975982,19473982,47085913,-90793462,-33520678,70775566,-76347995,-16091435,94700640,17183454,85735982,90399615,-86251609,-68167910,-95327478,90586275,-99524469,16999817,27815883,-88279865,53092631,75125438,44270568,-23129316,-846252,-59608044,90938699,80923976,3534451,6218186,41256179,-9165388,-11897463,92423776,-38991231,-6082654,92275443,74040861,77457712,-80549965,-42515693,69918944,-95198414,15677446,-52451179,-50111167,-23732840,39520751,-90474508,-27860023,65164540,26582346,-20183515,99018741,-2826130,-28461563,-24759460,-83828963,-1739800,71207113,26434787,52931083,-33111208,38314304,-29429107,-5567826,-5149750,9582750,85289753,75490866,-93202942,-85974081,7365682,-42953023,21825824,68329208,-87994788,3460985,18744871,-49724457,-12982362,-47800372,39958829,-95981751,-71017359,-18397211,27941418,-34699076,74174334,96928957,44328607,49293516,-39034828,5945763,-47046163,10986423,63478877,30677010,-21202664,-86235407,3164123,8956697,-9003909,-18929014,-73824245],
-236727523))