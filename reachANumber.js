const reachNumber = function(target) {
    const target = Math.abs(target)
    let sum = 0
    for(let step = 0; step < Infinity; step++) {
        sum += step
        let delta = sum - step
        if (delta > 0 && delta % 2 === 0) {
            return step
        }
    }
}
