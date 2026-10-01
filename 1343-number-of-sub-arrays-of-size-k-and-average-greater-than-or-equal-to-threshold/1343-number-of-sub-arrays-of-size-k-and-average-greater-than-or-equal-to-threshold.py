class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        current_sum = sum(arr[:k])
        count = 0
        if current_sum >= threshold * k:
            count += 1

        for i in range(k, len(arr)):
            current_sum = current_sum - arr[i - k] + arr[i]
            if current_sum >= threshold * k:
                count += 1
        return count

        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        