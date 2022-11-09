/**
 * @param {string} s
 * @return {number}
 */
 const lengthOfLongestSubstring = (s) => {
    let maxlen = 0;
    let currlen = 0;
    let i = 0;
    let result = '';
    while (i < s.length) {
        const curr = s[i];
        if (result.includes(curr)) {
            result = '';
            maxlen = Math.max(maxlen, currlen);
            i = i - currlen + 1;
            currlen = 0;
        } else {
            i = i + 1;
            currlen = currlen + 1;
            result = result + curr;
            maxlen = Math.max(maxlen, currlen);
        }
    }
    return maxlen;
};