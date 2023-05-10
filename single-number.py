class Solution(object):
    def singleNumber(self, nums):
        """
        Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

        It is guaranteed that all but one element will appear twice

        Pseudocode:
        The first thing I think of when I see this problem is by using a dictionary to hold the number of occurrences

        Iterate over each num in the input list nums
            Increment the number of occurrences in the dictionary by 1 for each number in the list

        Iterate over the now-full dictionary
            If the value of the key is one, then we've found the single number
        """

        seen = {}

        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

        for num in seen.keys():
            if seen[num] != 2:
                return num