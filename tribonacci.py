def tribonacci(n):
    results = [0, 1, 1]
    if n < 2:
        return results[n]
    for i in range(2, n):
        results.append(results[i] + results[i - 1] + results[i - 2])
    return results[-1]

print(tribonacci(25))