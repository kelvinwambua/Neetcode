//Time complexity: O(n^2)
//Space complexity: O(1)
// This is a brute force solution that checks every pair of elements in the array.
func containsDuplicate(nums []int) bool {
	for i, num := range nums {
		for j := i + 1; j < len(nums); j++ {
			if num == nums[j] {
				return true
			}
		}

	}
	return false

// Time complexity: O(n)
// Space complexity: O(n)

func containsDuplicate(nums []int) bool {

	seen := make(map[int]bool)

	for _, num := range nums {

		if seen[num] {
			return true
		}

		seen[num] = true
	}

	return false

}
