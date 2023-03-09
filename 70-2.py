class Solution:
    def climbStairs(self, n: int) -> int:
        """
        This inefficient (time exceeded) solution is included to demonstrate
        the intuition behind the fibonacci solution to the problem.
        """

        results = [
            [[1]],
            [[1, 1], [2]]
        ]
        i = 2

        while i < n:
            i += 1
            current = (
                list(map(lambda x: x + [1], results[i-1-1])) +
                list(map(lambda x: x + [2], results[i-2-1]))
            )
            results.append(current)

        return len(results[n-1])
