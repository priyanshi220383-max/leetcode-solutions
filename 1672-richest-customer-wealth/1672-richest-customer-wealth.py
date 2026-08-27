class Solution(object):
    def maximumWealth(self, accounts):
        maximum = 0
        for customer in accounts:
            wealth = 0
            for money in customer:
                wealth += money
            if wealth > maximum:
                maximum = wealth
        return maximum
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        