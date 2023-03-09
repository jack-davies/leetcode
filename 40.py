class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []

        def dfs(els: List[int], sum: int, idx: int):
            if sum > target:
                return
            elif sum == target:
                results.append(els)
            else:
                for i in range(idx, len(candidates)):
                    if i > idx and candidates[i] == candidates[i-1]:
                        # Skip testing multiple paths of same element
                        continue
                    dfs(els + [candidates[i]], sum + candidates[i], i+1)

        dfs([], 0, 0)

        return results
