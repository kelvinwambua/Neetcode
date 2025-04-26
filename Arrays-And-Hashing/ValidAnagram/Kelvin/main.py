class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        for c in countS:
            if countS[c] != countT.get([c],0):
                return False
   

#Same as above but using Counter from collections
class Solution(object):
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)
   

# Increases Time COmplexity but decreases Space Complexity as we do not declare a new memory structure
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
