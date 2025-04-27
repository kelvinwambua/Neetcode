class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        j = 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[j]:
                return True
            i += 1
            j += 1
        return False
