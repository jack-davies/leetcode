class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answers = [[1], [1, 1]]
        if numRows == 1:
            return [answers[0]]
        if numRows == 2:
            return answers

        for i in range(2, numRows):
            row = [1] + [None] * (i - 1) + [1]
            for j in range(i - 1):
                row[j+1] = answers[i-1][j] + answers[i-1][j+1]
            answers.append(row)

        return answers
