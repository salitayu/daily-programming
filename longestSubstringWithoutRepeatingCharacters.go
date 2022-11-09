package main

import "strconv"

func lengthOfLongestSubstring(s string) int {
	maxlen := 0
	start := 0
	subs := make(map[string]int)
	for end := range s {
		curr := strconv.Itoa(int(s[end]))
		_, ok := subs[curr]
		if ok {
			start = max(start, subs[curr]+1)
		}
		subs[curr] = end
		maxlen = max(maxlen, end-start+1)
	}
	return maxlen
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
