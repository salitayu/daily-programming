"""
Reverse the entire string.

Start iterating over the reversed string using two pointers, start and end.

While iterating over the strings, check for spaces between the words.

Once a space is found between words, update the end pointer accordingly.

Now use the two pointers to reverse characters in the word.

Once the word has been reversed, update the start and end pointer to the index of the space.

Repeat the process until the entire string is iterated.
"""
def reverse_words(sentence):
    # convert string to list and trim spaces
    l = trim(sentence)
    # reverse whole string
    reverse(l, 0, len(l) - 1)
    # reverse each word
    reverse_word(l)
    return ''.join(l)
def trim(s):
    left, right = 0, len(s) - 1
    # remove leading spaces
    while left <= right and s[left] == ' ':
        left += 1
    # remove trailing spaces
    while left <= right and s[right] == ' ':
        right -= 1
    # reduce multiple spaces to single one
    output = []
    while left <= right:
        if s[left] != ' ':
            output.append(s[left])
        elif output[-1] != ' ':
            output.append(s[left])
        left += 1
    return output
def reverse(l, left, right):
    while left < right:
        l[left], l[right] = l[right], l[left]
        left, right = left + 1, right - 1
def reverse_word(l):
    n = len(l)
    start = end = 0
    while start < n:
        # go to end of word
        while end < n and l[end] != ' ':
            end += 1
        # reverse word
        reverse(l, start, end - 1)
        # move to next word
        start = end + 1
        end += 1
print(reverse_words("Hello   World"))