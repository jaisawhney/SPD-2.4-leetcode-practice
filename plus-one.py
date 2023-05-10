class Solution(object):
    def plusOne(self, digits):
        """
        You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order.

        Pseudocode:
        Traverse the digits in reverse
            If the digit at the index is 9, then decrease the index by 1 and set that number to 0
            Else break loop

        If the index is greater than or equal to 0
            Increase the digit at the index by 1
            Return the modified digits

        Otherwise, that means the input list must be all 9s. In that case, just return 1 + the modified digits
        """

        idx = len(digits) - 1
        while digits[idx] == 9:
            digits[idx] = 0
            idx -= 1

        if idx >= 0:
            digits[idx] += 1
            return digits

        return [1] + digits
