const words = ['water', 'lily', 'top', 'tap']
const makeWords = (length) => {
    let results = ''
    let wordlens = {}
    let totals = length - 1
    for (let i = 0; i < words.length; i++) {
        const current = words[i]
        const currentlen = current.length
        if (currentlen in wordlens) {
            wordlens[currentlen].push(current)
        } else {
            wordlens[currentlen] = [current]
        }
    }
    console.log('wordlens ', wordlens)
    for (let key in wordlens) {
        const diff = totals - key
        const value = wordlens[key]
        if (diff in wordlens) {
            if (diff === key) {
                results = wordlens[diff][1] + '-' + value[1]
            } else {
                results = wordlens[diff][0] + '-' + value[0]
            }
            break
        } else {
            continue
        }
    }
    return results
}
console.log(makeWords(7))
