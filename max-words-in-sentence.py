class Solution(object):
    def mostWordsFound(self, sentences):
        """
        You are given an array of strings sentences, where each sentences[i] represents a single sentence. Return the maximum number of words that appear in a single sentence.

        Pseudocode:
        Right away, I can think of a few solutions to solve this

        First, create a variable, longest_sentence, to keep track of the number of words in the longest sentence
        Second, loop over each of the sentences in sentence
            Count the number of words in each sentence
            If the number of words in the sentence is greater than longest_sentence
                Update longest_sentence to reflect that

        Otherwise, return longest_sentence

        If the .count or .split method is used, the time complexity will be O(n^2)
        """
        longest_sentence = 0
        for sentence in sentences:
            num_words = len(sentence.split(" "))

            if longest_sentence < num_words:
                longest_sentence = num_words

        return longest_sentence