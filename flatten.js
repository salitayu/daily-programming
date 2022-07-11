let result = []
function flatten(nestedList) {
    for (let i = 0; i < nestedList.length; i++) {
        if (nestedList[i].length > 0) {
            flatten(nestedList[i])
        } else {
            result.push(nestedList[i])
        }
    }
    return result
}

const flat = (arr) => {
    return arr.reduce((acc, next) => {
        const isArray = Array.isArray(next)
        return acc.concat(isArray ? flatten(next) : next)
    }, [])
}

if (!Array.prototype.flatten) {
    Array.prototype.flatten = function() {
        return flatten(this)
    }
}

let arr = [1, 2, [3, 4, [5, 6]]]
console.log(arr.flatten())

console.log(flatten([1,2,[3,4,[5,6]]]))
