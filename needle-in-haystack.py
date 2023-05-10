class Solution(object):
    def strStr(self, haystack, needle):
        """
        Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

        Pseudocode:
        If we're allowed to use any built-in Python method (probably not), all we need to do is check if the needle is in the haystack
            If it is, return the index using .index
        Otherwise, return -1
        """

        if needle in haystack:
            return haystack.index(needle)
        return -1
