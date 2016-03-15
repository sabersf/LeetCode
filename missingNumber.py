class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(len(nums))
        nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        while left < right - 1:
            middle = (left + right) / 2
            if nums[middle] == (left + right) / 2:
                left = middle
            else:
                right = middle
        if nums[left] == left:
            return right
        return left
