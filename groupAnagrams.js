/**
 * @param {string[]} strs
 * @param {string[][]} anagrams
 * Given an array of strings strs, group the anagrams together and return in any order 
 */
const groupAnagrams = (strs) => {
    const results = {}
    for (let i = 0; i < strs.length; i++) {
        current = [...strs[i]].sort()
        if (current in results) {
            results[current].push(strs[i])
        } else {
            results[current] = [strs[i]]
        }
    }
    let resultsList = []
    for (let i in results) {
        resultsList.push(results[i])
    }
    return resultsList
}

console.log(groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
