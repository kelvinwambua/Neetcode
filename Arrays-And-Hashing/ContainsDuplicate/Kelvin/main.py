#Basically this is cheating, but it works
# Time complexity: O(n^2)
# Space complexity: O(1)
class Solution(object):
    def containsDuplicate(self, nums):
        for i in nums:
            if nums.count(i) > 1:
                return True
        return False

#Solution 2
# Time complexity: O(n^2)
# Space complexity: O(1)
# This is a brute force solution that checks every pair of elements in the array.
class Solution(object):
    def containsDuplicate(self, nums):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

#Solution 3
# Time complexity: O(n)
# Space complexity: O(n)
# This is a hash set solution that uses a hash set to store the elements in the array.
class Solution(object):
    def containsDuplicate(self, nums):
        hash_set = set()
        for num in nums:
            if num in hash_set:
                return True
            hash_set.add(num)
        return False
