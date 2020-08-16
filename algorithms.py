def sqm(base, exp, mod):

    # INIT ALGORITHM
    tmp = int(base ** 2) % mod
    if int(bin(exp)[3]) == 1:
        tmp = int(base * tmp) % mod

    # SQM
    for bit in range(4, len(bin(exp))):
        currBit = int(bin(exp)[bit])
        tmp = int(tmp ** 2) % mod
        if currBit:  # IS 1 THEN MULTIPLY
            tmp = int(base * tmp) % mod

    return tmp
