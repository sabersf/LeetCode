class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sol = []
        tab = {}
        for i in range(len(nums)):
            if target - nums[i] in tab:
                sol.append(tab[target - nums[i]]) 
                sol.append(i)
            else:
                tab[nums[i]] = i
                
        return sol
