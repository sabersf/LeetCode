class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = False
        if x < 0:
            neg = True
            x *= -1
        res = 0
        while x > 0:
            res = (res*10) + (x % 10)
            x /= 10
        if neg:
            res *= -1
        if res > 2**31-1 or res < -2**31+1:
            return 0
        return res
