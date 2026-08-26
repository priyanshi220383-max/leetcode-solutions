class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maximum = max(candies)
        array = []
        for candy in candies :
            if candy + extraCandies >= maximum:
                array.append(True)
            else:
                array.append(False)
        return array
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        