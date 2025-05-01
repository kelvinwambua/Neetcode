class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        a = [int(abs(x)) for x in nums]
        b = [x for x in nums if x < 0]
        b.sort()
        a.sort()
        if a[0] not in nums:
            return b[-1]
        return a[0]

