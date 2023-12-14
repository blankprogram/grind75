class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        formatted = ''.join(char.lower() for char in s if char.isalnum())

        return formatted == formatted[::-1]