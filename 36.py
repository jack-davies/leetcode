class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValid(segment: List[str]):
            # Checks a segment of nine elements for duplicates
            numbers = [n for n in segment if n != "."]
            return len(numbers) == len(set(numbers))

        for row in range(9):
            if not isValid(board[row]):
                return False

        for col in range(9):
            segment = [board[i][col] for i in range(9)]
            if not isValid(segment):
                return False

        for i in range(3):
            for j in range(3):
                segment = [board[(i * 3) + k // 3][(j * 3) + k % 3] for k in range(9)]
                if not isValid(segment):
                    return False

        return True
