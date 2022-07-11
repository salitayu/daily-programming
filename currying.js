// currying is translating function that takes multiple arguments into sequence of functions, each accepting one argument.

const addNums = (x) => (y) => x + y
console.log(addNums(2)(3))
