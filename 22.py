class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        last_partial = [("", n, n)]

        for i in range(2*n):
            current_partial = []
            for last in last_partial:
                if last[1] > 0:
                    current_partial.append((last[0]+"(", last[1]-1, last[2]))
                if last[2] > last[1]:
                    current_partial.append((last[0]+")", last[1], last[2]-1))
            last_partial = current_partial

        return [p[0] for p in current_partial]
