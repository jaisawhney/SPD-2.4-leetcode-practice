class Solution(object):
    def removeDuplicates(self, nums):
        """
        Given an integer array nums sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.
        Then return the number of unique elements in nums.

        Pseudocode:
        Iterate throughout the input list
            If the number is unique, move the index to the right
        Return the index + 1 for the sorted array
        """
        idx = 0
        for i in range(len(nums)):
            if nums[idx] != nums[i]:
                idx += 1
                nums[idx] = nums[i]
        return idx + 1
