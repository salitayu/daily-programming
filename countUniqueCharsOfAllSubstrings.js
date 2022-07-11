const uniqueLetterString = (s) => {
    let result = 0
    const n = s.length
    const hash = {}
    for (let i = 0; i < n; i++) {
        const letter = s[i]
        if (hash[letter] === undefined) {
            hash[letter] = [i]
        } else {
            hash[letter].push(i)
        }
    }
    for (let letter in hash) {
        const arr = hash[letter]
        let lastIdx = arr[0]
        let lastRange = arr[0] + 1
        for (let i = 1; i < arr.length; i++) {
            const currIdx = arr[i]
            const currRange = currIdx - lastIdx
            result += lastRange * currRange
            lastIdx = currIdx
            lastRange = currRange
        }
        result += lastRange * (n - lastIdx)
    }
    return result
}