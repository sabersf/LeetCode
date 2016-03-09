#second attempt
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = 1
        n = len(s)
        if n < 2:
            return n
        last_seen = {}
        temp = 0
        for i in range(n):
            if not s[i] in last_seen:
                last_seen[s[i]] = i
            else:
                temp = max(temp, last_seen[s[i]] + 1)
                last_seen[s[i]] = i
            record = max(record, i - temp + 1)
        return record
