const winnerOfGame = (colors) => {
    let acount = 0
    let bcount = 0
    for (let i = 0; i < colors.length - 1; i++) {
        previous = colors[i-1]
        current = colors[i]
        next = colors[i+1]
        if (previous === 'A' && current === 'A' && next === 'A') {
            acount += 1
        } else if (previous === 'B' && current === 'B' && next === 'B') {
            bcount += 1
        }
    }
    return acount > bcount
}

console.log(winnerOfGame('AAABABB'))
console.log(winnerOfGame('AA'))
console.log(winnerOfGame('ABBBBBBBAAA'))
