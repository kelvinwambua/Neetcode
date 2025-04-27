class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))  # Convert sorted list to string
            if sorted_word not in anagrams:
                anagrams[sorted_word] = []
            anagrams[sorted_word].append(word)
        return list(anagrams.values())