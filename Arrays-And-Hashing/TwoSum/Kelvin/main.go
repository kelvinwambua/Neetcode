// My initial slow solution
// Time complexity: O(n^2)
// Space complexity: O(1)
// This is a brute force solution that checks every pair of elements in the array.
func twoSum(nums []int, target int) []int {
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[i]+nums[j] == target {
				return []int{i, j}
			}
		}
	}
	return []int{}
}

func twoSum(nums []int, target int) []int {
	store := make(map[int]int)
	for i, num := range nums {
		if (target-num) == target {
			return []int{i, store[target-num]}
		}
		store[num] = i
	return []int{}


}