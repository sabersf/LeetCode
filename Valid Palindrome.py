class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        left = 0
        right = len(s) -1
        palindrome = True
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if not s[left] == s[right]:
                palindrome = False
                break
            left += 1
            right -= 1
        return palindrome
