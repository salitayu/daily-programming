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

def reachNumber(target):
    target = abs(target)
    k = 0
    while target > 0:
        k += 1
        target -= k
    return k if target % 2 == 0 else k + 1 + k % 2
