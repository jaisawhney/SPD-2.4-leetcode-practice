class Solution(object):
    def removeElement(self, nums, val):
        """
        Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

        Pseudocode:
        Declare an int to be our starting index/pointer (0)

        Loop for the length of the input list
            If the number at the current index does not equal the value to remove
                Update the number at the current pointer to the number at the current index (loop)
                Move the pointer to the right
        Return the index
        """

        idx = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[idx] = nums[i]
                idx += 1
        return idx