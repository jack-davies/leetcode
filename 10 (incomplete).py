class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        pattern = [[char, False] for char in p]
        for i in range(len(pattern)):
            if pattern[i][0] == "*":
                pattern[i-1][1] = True
        pattern = [element for element in pattern if not(element[0] == "*")]
        print(pattern)
        
        transitions = []
        current_state = 0
        for element in pattern:
            if not(element[1]):
                transitions.append((element[0], current_state, current_state+1))
                current_state += 1
            else:
                transitions.append((element[0], current_state, current_state))
        print(transitions)
        
        # invariant: initial state = 0, final state = current_state
        
        """
        cases:
        a-z or .: deterministic transition
        a-z*: 
        .*:
        """
    

a = Solution()
print(a.isMatch("abcd", "ab.*d"))