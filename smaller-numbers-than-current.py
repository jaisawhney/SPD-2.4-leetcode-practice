class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.

        Input: nums = [8,1,2,2,3]
        Output: [4,0,1,1,3]

        Pseudocode (brute force):
        Create a dictionary to map the current index to the number of occurrences found for that index
        
        Loop over the numbers in input "nums"
            
            Create an inner loop to loop over all the numbers in the input
                For each iteration, compare if the outer loop number is greater than the inner loop number.
                    If it is, add 1 to the the number occurrences at that index        
        Return the values of the dictionary
        """
        num_dict = {}

        for idx, num in enumerate(nums):
            num_dict[idx] = 0
            for num_two in nums:
                if num_two < num:
                    num_dict[idx] += 1
        print(num_dict)
        return num_dict.values()
