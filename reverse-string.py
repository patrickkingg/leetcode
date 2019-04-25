class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=list(s)
        for i in range(len(s)):
            res[i] = s[len(s)-1-i]
        return "".join(res)