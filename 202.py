class Solution:
    def isHappy(self, n: int) -> bool:
        def squarify(n: int):
            digits = map(int, str(n))
            squared = [d**2 for d in digits]
            return sum(squared)

        results = set([n])
        # Cache the attractor state
        results.update([2, 4, 16, 37, 58, 89, 145, 42, 20])

        current = n
        while True:
            current = squarify(current)
            print(current)
            if current == 1:
                return True
            if current in results:
                return False

            # Only required if cache is incomplete
            results.add(current)
