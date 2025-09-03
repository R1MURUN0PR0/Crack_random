import random
from gf2bv import LinearSystem
from gf2bv.crypto.mt import MT19937

def untemper(y):
    # 1. Rev: y ^= (y >> 18)
    y ^= (y >> 18)
    # 2. Rev: y ^= (y << 15) & 0xefc60000
    y ^= (y << 15) & 0xefc60000
    # 3. Rev: y ^= (y << 7) & 0x9d2c5680
    temp = y
    for _ in range(4):
        temp = y ^ (temp << 7) & 0x9d2c5680
    y = temp
    # 4. Rev: y ^= (y >> 11);
    temp = y
    for _ in range(2):
        temp = y ^ (temp >> 11)
    y = temp
    return y

state = random.getstate()

outputs = [ random.getrandbits(32) for _ in range(1000) ]
recovered_state = (3, tuple([ untemper(v) for v in outputs[:624] ] + [0]), None)

random.setstate(recovered_state)
for i in range(1000):
    assert outputs[i] == random.getrandbits(32)
