const numMatchingSubseq = function(s, words) {
    let count = 0
    for (let w of words) {
        if (find(s, w)) {
            count += 1
        }
    }
    return count
}

const find = (s, w) => {
    let index = -1
    for (const c of w) {
        const found = s.indexOf(c, index + 1)
        if (found === -1) {
            return false
        }
        index = found
    }
    return true
}