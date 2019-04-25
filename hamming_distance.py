class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = '{0:032b}'.format(x)
        y = '{0:032b}'.format(y)
        res = 0
        print(x)
        print(y)
        for i in range(len(x)):
            if x[i] != y[i]:
                res += 1
        return res