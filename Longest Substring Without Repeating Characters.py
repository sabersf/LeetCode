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
        next_seen = [n] * n
        mark = [0] * n
        for i in range(n):
            next_seen[i] = s.find(s[i], i+1)
            if next_seen[i] < 0:
                next_seen[i] = n
        #print next_seen
        for i in range(n):
            if mark[i] > 0:
                continue
            if next_seen[i] - i < record:
                continue
            j = i + 1
            while j < next_seen[i]:
                if next_seen[j] < next_seen[i]:
                    next_seen[i] = next_seen[j]
                j += 1
            if j - i > record:
                record = j - i
                for t in range(i,j):
                    mark[t] = 1
        return record
