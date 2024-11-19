def countNicePairs(nums):
    def reverse(num):
        result = 0
        while num > 0:
            result = result * 10 + num % 10
            num //= 10
        return result
    answer = 0
    array = []
    dictionary = {}
    modulo = 10 ** 9 + 7
    for i in range(0, len(nums)):
        array.append(nums[i] - reverse(nums[i]))
    for i in range(0, len(array)):
        current = array[i]
        if current in dictionary:
            answer = (answer + dictionary[current]) % modulo
        dictionary[current] = dictionary.setdefault(current, 0) + 1
    return answer
print(countNicePairs([7,3,4,4,2,4,3,3]))