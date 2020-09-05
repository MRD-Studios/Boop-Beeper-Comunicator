import numpy as np
def encode(bits):
    inbits=bits
    if (np.count_nonzero(inbits == 1) % 2) == 0:
        inbits[0] = inbits[0]
    else: inbits[0] = not inbits[0]
    return inbits

def errorChecker(bits):
    if (np.count_nonzero(bits == 1) % 2) == 0:
        return "No known 1 bit Error (a 2+ bit error may stil occur)"
    else: return "Error in transfer, Data may be wrong"
randomData = np.random.randint(0, 2, 2048)
data = encode(randomData)
print(errorChecker(data))