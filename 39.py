class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Backtracking/DFS solution
        """
        results = []

        def search(elements: List[int], sum: int, idx: int):
            for i in range(idx, len(candidates)):
                if sum == target:
                    results.append(elements)
                    return
                if sum + candidates[i] > target:
                    pass
                elif sum + candidates[i] <= target:
                    search(elements + [candidates[i]], sum + candidates[i], i)

        for i in range(len(candidates)):
            search([candidates[i]], candidates[i], i)

        return results
