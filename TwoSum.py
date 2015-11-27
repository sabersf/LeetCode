class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums) # <-- for sets
        index1 = 1
        index2 = n
        #initial solution 6k seconds
        #for i in range(0,n):
        #    for j in range(i+1,n):
        #        if nums[i] + nums[j] == target:
        #            index1 = i+1
        #            index2 = j+1
        #second solution 5 seconds!:
        mark = [0] * 65536 #<-- when you can't use numpy.zeros()
        for i in range(0,n):
            if mark[target - nums[i]] > 0:
                index1 = i + 1
                index2 = mark[target - nums[i]] 
                if index2 < index1:
                    temp = index1
                    index1 = index2
                    index2 = temp
            else:
                mark[nums[i]]  = i + 1
        return [index1, index2]
