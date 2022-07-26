const findAnagrams = function(s, p) {
    const plen = p.length
    const result = []
    const d = {}
    let count = 0
    for (let i = 0; i < plen; i++) {
        const item = p[i]
        if (item in d) {
            d[item] += 1
        } else {
            count += 1
            d[item] = 1
        }
    }
    let result = []
    let left = 0
    for (let right = 0; right < s.length; right++) {
        if (d[s[right]] != null) d[s[right]]--
        if (d[s[right]]==0) count--
        if (count == 0) result.push(left)
        if (right - left + 1 == plen) {
            if (d[s[left]] != null) d[s[left]]++
            if (d[s[left++]] == 1) count++
        }
    }
    return result
}