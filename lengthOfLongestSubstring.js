const lengthOfLongestSubstring = (s) => {
    let maxlen = 0
    let start = 0
    const letters = {}
    for (let end = 0; end < s.length; end++) {
        const current = s[end]
        if (current in letters) {
            start = Math.max(start, letters[current] + 1)
        }
        letters[current] = end
        maxlen = Math.max(end - start + 1, maxlen)
    }
    return maxlen
}

console.log(lengthOfLongestSubstring('abcabc'))
