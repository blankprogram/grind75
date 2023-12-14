class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        if len(s) % 2 != 0:
            return False
        
        bracket_pairs = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)
            elif char in [')', ']', '}']:
                if stack and stack[-1] == bracket_pairs[char]:
                    stack.pop()
                else:
                    return False
        return not stack
