class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        SList = list(S)
        SList.sort()

        res = 0
        for stone in SList:
            i = 0
            while i < len(J):
                if J[i] == stone:
                    res += 1
                    i += 1
                else:
                    i += 1
        return res
