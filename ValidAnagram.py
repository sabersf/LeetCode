class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = sorted(list(s))
        t = sorted(list(t))
        if len(s) != len(t):
            return False
        if len(s) == 0:
            return True
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True
