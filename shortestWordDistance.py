import math

def shortestWordDistance(word1, word2):
    words = ['practice', 'makes', 'perfect', 'coding', 'makes']
    word1_index = -1
    word2_index = -1
    shortestDistance = math.inf
    for i in range(0, len(words)):
        current = words[i]
        if current == word1:
            word1_index = i
        if current == word2:
            word2_index = i
        if word1_index != -1 and word2_index != -1:
            shortestDistance = min(abs(word2_index - word1_index), shortestDistance)
    return shortestDistance

print(shortestWordDistance('coding', 'practice'))
print(shortestWordDistance('makes', 'coding'))
