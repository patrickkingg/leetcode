class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for i in range(left, right + 1):
            count = 0
            num = str(i)
            length = len(num)
            for d in num:
                if int(d) != 0 and i % int(d) == 0:
                    count += 1
                else:
                    break

            if count == length:
                result.append(i)

        return res