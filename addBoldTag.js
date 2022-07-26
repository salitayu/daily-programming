function addBoldTag(s, d) {
    const n = s.length
    const flag = new Array(n)
    let currentEnd = 0
    let ans = ''
    for(let i = 0; i < n; i++) {
        for (let w of d) {
            if (s.startsWith(w, i)) {
                currentEnd = Math.max(currentEnd, i + w.length)
            }
        }
        if (i < currentEnd) {
            flag[i] = true
        } else {
            flag[i] = false
        }
    }
    for(let i = 0; i < n; i++) {
        if(flag[i] && (i == 0 || (i > 0 && !flag[i-1]))) {
            ans += '<b>'
        }
        ans += s[i]
        if (flag[i] && (i==n-1 || (i < n - 1 && !flag[i+1]))) {
            ans += '</b>'
        }
    }
    return ans
}

console.log(addBoldTag('abcxyz123', ['a', '123']))
