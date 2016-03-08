class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if len(str) == 0:
            return 0
        res = 0
        neg = False
        count = 0
        while len(str) > 0 and (str[0] == '+' or str[0] == '-'):
            if str[0] == '-':
                neg = True
                str=str[1:]
                count += 1
            if len(str) == 0:
                return 0
            if str[0] == '+':
                str = str[1:]
                count += 1
            if len(str) == 0:
                return 0
        if count > 1:
            return 0
        for i in range(len(str)):
            if ord(str[i]) >= ord('0') and ord(str[i]) <= ord('9'):
                res = (res*10) + (ord(str[i]) - ord('0'))
            else:
                break
        if neg:
            res *= -1
        return -2147483648 if res < -2147483648 else 2147483647 if res > 2147483647 else res
        
