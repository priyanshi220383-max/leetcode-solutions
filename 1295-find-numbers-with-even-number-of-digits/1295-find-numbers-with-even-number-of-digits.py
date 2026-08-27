class Solution(object):
    def findNumbers(self, nums):
        array = []
        for num in nums:
            if len(str(num)) % 2 == 0:
                array.append(num)
        return len(array)
        """
        :type nums: List[int]
        :rtype: int
        """
        