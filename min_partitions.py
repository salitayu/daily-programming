'''
A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.
Input: n = "32"
Output: 3
Explanation: 10 + 11 + 11 = 32
'''
def minPartitions(n):
    maxnum = 0
    for i in range(0, len(n)):
        maxnum = max(maxnum, ord(n[i]) - ord('0'))
n = "32"
print(minPartitions(n))