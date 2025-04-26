func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	countS := make(map[rune]int)
	countT := make(map[rune]int)

	for _, c := range s {
		countS[c]++
	}

	for _, c := range t {
		countT[c]++
	}

	for c, count := range countS {
		if countT[c] != count {
			return false
		}
	}

	for c := range countT {
		if countS[c] == 0 {
			return false
		}
	}

	return true
}
func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	count := make(map[rune]int)

	for _, c := range s {
		count[c]++
	}

	for _, c := range t {
		count[c]--
		if count[c] < 0 {
			return false
		}
	}

	return true
}