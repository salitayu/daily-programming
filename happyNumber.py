# Initialize a variable slow with the input number and fast with the squared sum of the input number's digits
# If fast is not 1 and not equal to slow, increment slow by one iteration and fast by two iterations
# Set slow to sum of digits(slow) and fast to sum of digits(sum of digits(fast))
# If fast converges to 1, return TRUE, else return FALSE
from tkinter import N


def happyNumber(n):
    seen = []
    while n > 1 and n not in seen:
        seen.append(n)
        n = pdi(n)
    return n == 1
def pdi(number):
    total = 0
    while number > 0:
        total += pow(number % 10, 2)
        number = number // 10
    return total
def sum_of_digits(number):
    total_sum = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        total_sum += digit ** 2
    return total_sum


def get_next(number):
    total_sum = 0
    while number > 0:
        number, digit = divmod(number, 10)
        total_sum += digit ** 2
    return total_sum

def is_happy(n):
    slow_runner = n
    fast_runner = get_next(n)
    while fast_runner != 1 and slow_runner != fast_runner:
        slow_runner = get_next(slow_runner)
        fast_runner = get_next(get_next(fast_runner))
    return fast_runner == 1

def ishappynumber(n):
    def sumofsquareddigits(n):
        totalsum = 0
        while n > 0:
            digit = n % 10
            n //= 10
            totalsum += digit ** 2
        return totalsum
    slowpointer = n
    fastpointer = sumofsquareddigits(n)
    while fastpointer != 1 and slowpointer != fastpointer:
        slowpointer = sumofsquareddigits(slowpointer)
        fastpointer = sumofsquareddigits(sumofsquareddigits(fastpointer))
    if fastpointer == 1:
        return True
    return False