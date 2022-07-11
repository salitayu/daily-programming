const merge = (intervals) => {
    let previous = [null, -1]
    let result = [previous]
    intervals = intervals.sort((a, b) => a[0] - b[0])
    for (let i = 0; i < intervals.length; i++) {
        const current = intervals[i]
        if (current[0] > result[result.length - 1][1]) {
            result.push(current)
        } else {
            result[result.length-1][1] = Math.max(current[1], result[result.length-1][1])
        }
    }
    return result.slice(1, result.length)
}
