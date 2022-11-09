const longestPalindrome = (s) => {
    let max ="";
    let currMax = "";
    if(s === "" || s.length < 1){
        return "";
    }
    for(let i = 0; i < s.length; i++) {
        const left = expandAroundCenter(s, i, i);
        const right = expandAroundCenter(s, i, i+1);
        let currMax = left.length >= right.length ? left : right;
        max = currMax.length > max.length ? currMax : max;
    }
    return max;
}
const expandAroundCenter = (s, left, right) => {
    let curr = "";
    while (left >= 0 && right < s.length && s[left] === s[right]) {
        curr = s.substring(left, right + 1);
        left -= 1;
        right += 1;
    }
    return curr;
}