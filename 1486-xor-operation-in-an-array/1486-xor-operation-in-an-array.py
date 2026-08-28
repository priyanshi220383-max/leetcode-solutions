class Solution(object):
    def xorOperation(self, n, start):
        array = 0
        for i in range (n):
            num = start + 2* i
            array = array ^ num
        return array
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        