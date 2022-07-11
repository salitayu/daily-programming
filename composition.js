// function composition is the combination of two functions into one that when applied, returns the result of the chained functions.
const compose = f => g => x => f(g(x))

console.log(compose(x => x * 4) (x => x + 3) (2))
// (2 + 3)(4) = 20
