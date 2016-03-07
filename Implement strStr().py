class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        ind = -1
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1
        for i in range(len(haystack)):
            if i + len(needle) > len(haystack):
                return -1
            match = True
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    match = False
                    break
            if match:
                return i
        return ind
