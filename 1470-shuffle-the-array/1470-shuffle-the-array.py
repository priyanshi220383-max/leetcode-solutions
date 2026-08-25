class Solution(object):
    def shuffle(self, nums, n):
        array = []
        for i in range(n) :
           array.append(nums[i])
           array.append(nums[i+n])
            
        return array
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        