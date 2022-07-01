# add a list of numbers together
def add_nums(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + add_nums(arr[1:])

# reverse a string
def reverse_string(original_string, reversed_string, current_index):
    if len(original_string) == 0:
        return
    reversed_string[current_index] = original_string[-1]
    return reverse_string(original_string[:-1], reversed_string, current_index+1)

# reverse string in place
def rev_str(string, low=0, high=None):
    if high == None:
        high = len(string) - 1
    if low >= high:
        return string
    string[low], string[high] = string[high], string[low]
    return rev_str(string, low + 1, high - 1)

def rs(input):
    if input == '':
        return ''
    return rs(input[1:]) + input[0]

print('rs input ', rs('hello'))

# reverse linked list
def reverse_list(head):
    if not head or not head.next:
        return head
    p = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return p

# check if palindrome
def palindrome_check(string):
    if len(string) == 0 or len(string) == 1:
        return True
    if string[0] != string[-1]:
        return False
    return palindrome_check(string[1:len(string)-1])

def pc(string):
    if len(string) == 0 or len(string) == 1:
        return True
    if string[0] == string[-1]:
        return pc(string[1:len(string)-1])
    return False

print('pc sally ', pc('sally'))
print('pc racecar ', pc('racecar'))

# decimal to binary
def convert_binary(number, result):
    if number == 0:
        return result
    result.append(number % 2)
    return convert_binary(number//2, result)

# convert number to base k
def convert_base(number, base):
    conversions = '0123456789ABCDEF'
    if number < base:
        return conversions[number]
    return convert_base(number // base, base) + conversions[number % base]

# merge 2 sorted linkedlist
# insert into binary search tree
# find all leaf nodes
# path sum of tree
# invert a tree
# cheapest root to leaf sales path cost
# binary inorder successor
# lowest common ancestor
# depth first search
# breadth first search
# sierpinski triangle
# exploring a maze
# drawing tree with turtle
# visualizing recursion
# stack frames
# towers of hanoi
# champage towers
# delete first occurance of string in nested array
# verify json employee of managers structure
# flatten nested list
# binary search
# fibonacci, climb stairs
# factorial
# hackerrank recursive super digit
# leetcode is same tree
# generate combinations and subsets

# merge sort
def merge_sort(arr):
    arrlen = len(arr)
    if arrlen > 1:
        mid = arrlen // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# tower of hanoi
def tower_of_hanoi(height, frompole, topole, withpole):
    if height >= 1:
        tower_of_hanoi(height - 1, frompole, withpole, topole)
        move(height - 1, frompole, topole)
        tower_of_hanoi(height - 1, withpole, topole, frompole)
def move(height, frompole, topole):
    print('moving ', height, ' from pole ', frompole, ' to pole ', topole)

if __name__ == '__main__':
    # arr = [9, 5, 8, 6, -2, 1, 7, -1, 2, 0]
    #
    # arr = [1, 2, 3]
    # print(add_nums(arr))
    #
    # merge_sort(arr)
    # print(arr)
    #
    # print(tower_of_hanoi(3, 'a', 'b', 'c')) #height, from pole, topole, withpole

    # original_string = ['h', 'e', 'l', 'l', 'o']
    # reversed_string = ['h', 'e', 'l', 'l', 'o']
    # current_index = 0
    # reverse_string(original_string, reversed_string, current_index)
    # print(reversed_string)

    # s = ['h', 'e', 'l', 'l', 'o']
    # low = 0
    # high = len(s) - 1
    # rev_str(s, low, high)
    # print(s)

    # print(palindrome_check(['r', 'a', 'c', 'e', 'c', 'a', 'r']))
    # print(palindrome_check(['a', 'b', 'c']))

    # result = []
    # convert_binary(10, result)
    # print(result[::-1])

    print(convert_base(16, 16))