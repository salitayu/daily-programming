for i in range(1, 100):
    result = ''
    if i % 3 == 0:
        result += 'Fizz'
    if i % 5 == 0:
        result += 'Buzz'
    if result == '':
        result = str(i)
    print(result)

for num in range(1, 100):
    resultstring = ''
    if i % 3 == 0:
        resultstring += 'Fizz'
    if i % 5 == 0:
        resultstring += 'Buzz'
    if result == '':
        resultstring += str(i)
    print(resultstring)
    