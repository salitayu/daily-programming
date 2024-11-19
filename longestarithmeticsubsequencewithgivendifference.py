def longestarithmeticsubsequence(arr, difference):
    dp = {}
    answer = 1
    for a in arr:
        beforea = dp.get(a - difference, 0)
        dp[a] = beforea + 1
        answer = max(answer, dp[a])
    return answer
