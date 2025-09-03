from rng import *
from z3 import *

s = Solver()
NUM_TEST = 700

vec = [BitVec(f'vec_{i}', 64) for i in range(RNG_LEN)]
rng_equation = RngSource(vec)
equations = [rng_equation.uint64() for _ in range(NUM_TEST)]

rng_value = RngSource()
rng_value.seed(int(input("Enter seed: ")))
vals = [rng_value.uint64() for _ in range(NUM_TEST)]

for i in range(NUM_TEST):
    s.add(equations[i] == vals[i])

print("99%...")

if s.check() == sat:
    model = s.model()
    array_values = [model.evaluate(vec[i]).as_long() for i in range(RNG_LEN)]
    rng = RngSource(array_values)

    for _ in range(NUM_TEST):
        res = rng.uint64()

    for _ in range(10):
        print(rng.uint64(), rng_value.uint64())