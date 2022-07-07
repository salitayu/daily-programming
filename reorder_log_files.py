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
        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            # type of log 0 digit 1 letter, rest content of letter logs, identifier of letter logs
            return (0, rest, _id) if rest[0].isalpha() else (1, )
        return sorted(logs, key=get_key)