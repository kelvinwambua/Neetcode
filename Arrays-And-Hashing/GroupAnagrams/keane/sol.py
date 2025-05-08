class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        for word in strs:
            count=[0] * 26
            for c in word:
                    count[ord(c) - ord("a")] += 1
            if tuple(count) not in my_dict.keys():
                my_dict.update({tuple(count):[word]})
            else:
                my_dict[tuple(count)].append(word)
        return my_dict.values()
