class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        Write a function to find the longest common prefix string amongst an array of strings.

        Input: strs = ["flower","flow","flight"]
        Output: "fl"
        
        Pseudocode:
        If the input is empty just, return an empty string immediately

        Otherwise, loop over the length of the smallest string in the list
            If the letter at the idx of the smallest string is not the same as the same letter of the largest string, we have found the largest prefix and can break the loop
            Else add the current letter to the prefix
        
        Return the prefix
        """
        
        if len(strs) == 0:
            return ""

        prefix = ""

        min_str = min(strs)
        max_str = max(strs)

        for idx in range(len(min_str)):
            if min_str[idx] != max_str[idx]:
                break
            prefix += min_str[idx]
        return prefix
