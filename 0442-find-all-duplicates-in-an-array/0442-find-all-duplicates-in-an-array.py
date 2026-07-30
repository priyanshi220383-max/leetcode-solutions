class Solution(object):
    def findDuplicates(self, nums):
        seen = set() #empty set created that stores no already seen
        ans = [] #empty list in which duplicate or single accuring item is added

        for num in nums :

            if num in seen:
                ans.append(num)
            else:
                seen.add(num)

        return ans
