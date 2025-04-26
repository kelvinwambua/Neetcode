class Solution(object):
    def twoSum(self, nums, target):
        length = len(nums)
        for i in range(length):
            left = i
            right = length-1
            while (left < right):
                if nums[left] + nums[right] == target:
                    result = [left, right]
                    print("[" + ",".join(str(x) for x in result) + "]")
                    return result
                if (left == right):
                    left += 1
                right -= 1
