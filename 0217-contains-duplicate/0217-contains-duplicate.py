class Solution(object):
    def containsDuplicate(self, nums):
        unique = set()
        for x in nums:
            if x in unique:
                return True
            unique.add(x)
        return False
        """
        :type nums: List[int]
        :rtype: bool
        """
        