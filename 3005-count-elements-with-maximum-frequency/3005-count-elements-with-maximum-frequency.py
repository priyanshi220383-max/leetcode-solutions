from collections import Counter
class Solution(object):
    def maxFrequencyElements(self, nums):
        freq = Counter(nums)
        max_frequency = max(freq.values())
        return sum( n for n in freq.values() if n == max_frequency)      
        """
        :type nums: List[int]
        :rtype: int
        """
        