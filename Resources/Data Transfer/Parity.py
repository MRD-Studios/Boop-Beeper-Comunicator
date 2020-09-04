from numpy import count_nonzero
from functools import reduce
from numpy import random
b = 1
def encode(bits):
    inbits=bits
    parityTotal = reduce(
        lambda x, y: x ^ y,
        [i for (i, b) in enumerate(inbits) if b]
    )
    print(parityTotal)
    parityValues = format(parityTotal, '08b')
    print(parityValues)
    inbits[1] = parityValues[0]
    inbits[2] = parityValues[1]
    inbits[4] = parityValues[2]
    inbits[8] = parityValues[3]
    inbits[16] = parityValues[4]
    inbits[32] = parityValues[5]
    inbits[64] = parityValues[6]
    inbits[128] = parityValues[7]
    print(count_nonzero(inbits == 1))
    if (count_nonzero(inbits == 1) % 2) == 0: inbits[0] = 0
    else: inbits[0] = 1
    print(count_nonzero(inbits == 1))
    return inbits

def errorChecker(bits):
    return reduce(
        lambda x, y: x ^ y,
        [i for (i, b) in enumerate(bits) if b]
    )
randomData = random.randint(0, 2, 256)
data = encode(randomData)
print(errorChecker(data))