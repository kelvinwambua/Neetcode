class Solution(object):
    def isAnagram(self, s, t):
        a = []
        for c in s:
            a.append(ord(c))
        a.sort()
        b = []
        for c in t:
            b.append(ord(c))
        b.sort()
        if len(a)!=len(b):
            return False
        for i in range(len(a)):
            if(a[i]!=b[i]):
                return False
        return True
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
