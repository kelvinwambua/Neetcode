class Solution(object):
    def isAnagram(self, s, t):
        newString = []  
        for i in range((len(s)-1), -1, -1):   
            newString.append(s[i])  
        if newString == t:
            return True
        else:
            return False
    solution = Solution()
    print(solution.isAnagram("anagram", "nagaram"))

