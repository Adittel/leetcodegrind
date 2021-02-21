class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        x = dict()
        #each element is value,index
        for i in range(len(nums)):
            print(nums[i])
            if (target-nums[i]) in x:
                return [x[target-nums[i]],i]
            x[nums[i]]=i
