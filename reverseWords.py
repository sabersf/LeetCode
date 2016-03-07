class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip().split()
        s.reverse()
        if len(s) == 0:
            return ""
        output = s[0]
        for i in range(1, len(s)):
            output = output + " " + str(s[i])
        return output
