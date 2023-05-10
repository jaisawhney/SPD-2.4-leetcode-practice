class Solution(object):
    def runningSum(self, nums):
        """
        Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]). Return the running sum of nums.

        Pseudocode:
        If we are allowed to modify the input parameter all we need to do is as follows:
        Loop the length of nums starting at index 1 times
            Increment the number in the list at the current index by the number in the list at index-1
        Return the list

        If we are not allowed to modify the input parameter, we can make a clone using [:]
        """

        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
