class Solution(object):
    def buildArray(self, nums):
        array = []
        for i  in range(len(nums)) :
            array.append(nums[nums[i]])
        return array
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        