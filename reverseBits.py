def reverseBits(n):
    ret = 0
    power = 31
    while n:
        ret += (n & 1) << power
        n = n >> 1
        power -= 1
    return ret
