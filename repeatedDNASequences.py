# def repeatedDNASequences(s):
#     seen = {}
#     result = set()
#     if len(s) >= 10:
#         for i in range(0, len(s) - 9):
#             current = s[i:i+10]
#             if current in seen:
#                 seen[current] += 1
#                 result.add(current)
#             else:
#                 seen[current] = 1
#     return result
def repeated_dna_sequences(s, k):
    d = {}
    temp = []
    result = []
    for end in range(0, len(s)):
        current = s[end]
        if len(temp) == k:
            temp1 = ''.join(temp)
            if temp1 in d:
                result.append(temp1)
            temp.pop(0)
        else:
            temp.append(current)
            d[''.join(temp)] = 1
    return result
print(repeated_dna_sequences("GGGGGGGGGGGGGGGGGGGGGGGGG", 12))