class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for i,n in enumerate(nums):
            if target-n in hashmap:
                return [hashmap[target-n], i]
            else:
                hashmap[n] = i
        return None
            