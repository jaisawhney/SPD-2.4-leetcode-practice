class Solution(object):
    def containsDuplicate(self, nums):
        """
        Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

        Pseudocode:
        Create a set instead of a list to hold all the seen numbers. Sets have a higher lookup time than lists because Python sets use hashmaps under the hood

        Loop over each number in the input list
            If the number is in the set, that means that it is a duplicate, and we can return True
            Otherwise, add the number to the set

        If there is no duplicate after the loop ends, we just return False
        """

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False