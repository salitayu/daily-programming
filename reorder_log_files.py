def reorderLogFiles(self, logs):
        '''Input: List of logs
        Each log is a space delimited string of words. First word is identifier
        Letter Logs: All words except identifier consist of lowercase English letters.
        Digit Logs: All words except identifier consists of digits.
        Reorder logs:
        Letter Logs come before digit logs
        Letter Logs are sorted lexicographically by their contents. If their contents are the same, sort them lexicographically by their identifiers.
        Return the final order of the logs.
        '''
        letters = []
        digits = []
        result = []
        for i in logs:
            count = 0
            for j in i:
                if j.isalpha() or j == ' ':
                    count += 1
            if count == len(i) - 1:
                letters.append(i)
            else:
                digits.append(i)
        # letters.sort()
        # newletters = ['art can', 'own kit dig', 'art zero']
        # newletters.sort()
        # print(newletters)
        newletters = []
        for i in letters:
            count = 0
            for j in i:
                if j == ' ':
                    count += 1
                if count >= 1:
                    newletters.append(j)
                    count += 1
        print('newletters ', newletters)
        for i in digits:
            result.append(i)
        return result