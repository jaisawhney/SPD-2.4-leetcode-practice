class Solution(object):
    def buildArray(self, nums):
        """
        Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

        Pseudocode:
        The question is worded in a really confusing way, but I would do the following:
        If memory is not an issue, I would clone the input list, res, so that we can update the values without interfering with our loop

        Loop for the length of the input list:
            If the current index is less than the length of the input
                Set the element at the index in the cloned list to the element at
        """

        res = nums[:]
        for i in range(len(nums)):
            if i < len(nums):
                res[i] = nums[nums[i]]
        return res