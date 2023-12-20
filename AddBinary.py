class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c = int(a, 2) + int(b, 2)
        str1 = ""
        if c == 0:
            return str(0)
        while c >= 1:
            str1 += str(c%2)
            c = c//2

        return str1[::-1]