class Solution(object):
    def minimumDifference(self, nums, k):
        nums.sort()
        answer = float('inf')

        for i in range(k-1 , len(nums)):
            difference = nums[i] - nums[i - k + 1]
            answer = min(answer, difference )

        return answer