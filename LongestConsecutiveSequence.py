class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        nums = sorted(set(nums))
        count = 0
        n = len(nums)
        ind = 0
        while ind < n:
            temp = 1
            while ind < (n - 1) and nums[ind+1] - nums[ind] == 1:
                temp += 1
                ind += 1
            if temp > count:
                count = temp
            ind += 1
        return count
