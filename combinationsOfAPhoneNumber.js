let output = []
d = {'2':['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7':['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
var getCombos = function(combo, digits) {
    if (digits.length === 0) {
        output.push(combo)
        return
    }
    for (let letter of d[digits[0]]) {
        getCombos(combo + letter, digits.substring(1, digits.length))
    }
}
var letterCombinations = function(digits) {
    if (digits === '') {
        return []
    }
    getCombos('', digits)
    return output
}
console.log(letterCombinations("2"))