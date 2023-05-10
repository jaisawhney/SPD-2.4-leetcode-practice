class Solution(object):
    def getConcatenation(self, nums):
        """
        Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

        Pseudocode:
        I would approach this problem by looping over the length of the input array and appending the num at that index to the input itself
        Now all we need to do is return the modified input list
        """
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums
