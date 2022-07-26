const mostVisitedPattern = function(username, timestamp, website) {
    const map = {}
    for (let i = 0; i < username.length; i++) {
        const user = username[i]
        const data = { time: timestamp[i], site: website[i] }
        if (map[user]) {
            map[user].push(data)
        } else {
            map[user] = [data]
        }
    }
    const freqCount = {}
    for (let user in map) {
        const data = map[user]
        data.sort((a, b) => a.time - b.time)
        const set = new Set()
        for(let i = 0; i < data.length; i++) {
            for (let j = i + 1; j < data.length; j++) {
                for (let k = j + 1; k < data.length; k++) {
                    const sequence = [data[i].site, data[j].site, data[k].site]
                    const str = JSON.stringify(sequence)
                    if (set.has(str)) {
                        continue
                    }
                    set.add(str)
                    if (freqCount[str]) {
                        freqCount[str]++
                    } else {
                        freqCount[str] = 1
                    }
                }
            }
        }
    }
    const countToSequence = {}
    let max = -1
    for (let sequence in freqCount) {
        const freq = freqCount[sequence]
        max = Math.max(max, freq)
        if (countToSequence[freq]) {
            countToSequence[freq].push(sequence)
        } else {
            countToSequence[freq] = [sequence]
        }
    }
    const strSequences = countToSequence[max]
    const sequences = strSequences.map((strSequence) => JSON.parse(strSequence))
    return sequences.sort()[0]
}
