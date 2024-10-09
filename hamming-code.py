from functools import reduce
import numpy as np

def hamming_syndrome(bits):
    return reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(bits) if bit])

list = np.random.randint(0, 2, 16)
print(list)
print(hamming_syndrome(list))


