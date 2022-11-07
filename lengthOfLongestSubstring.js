const lengthOfLongestSubstring = (s) => {
    d = {}
    let start = 0
    let maxlen = 0
    for (let end = 0; end < s.length; end++) {
        const curr = s[end]
        if (curr in d) {
            start = Math.max(start, d[curr] + 1)
        }
        d[curr] = end
        maxlen = Math.max(maxlen, end - start + 1)
    }
    return maxlen
}

console.log(lengthOfLongestSubstring('abcabc'))
