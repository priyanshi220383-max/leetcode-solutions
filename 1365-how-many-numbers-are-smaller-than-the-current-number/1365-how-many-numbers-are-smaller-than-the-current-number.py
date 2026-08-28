class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        array = []
        for num in nums:
            count = 0 
            for other in nums:
                if other < num:
                    count += 1
            array.append(count)

        return array
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        