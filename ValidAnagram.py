class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        table = defaultdict(int)
        for char in s:
            table[char] += 1

        for char in t:
            table[char] -= 1

        for count in table.values():
            if count != 0:
                return False

        return True