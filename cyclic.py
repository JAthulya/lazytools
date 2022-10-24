#!/bin/python3
from pwnlib.util.cyclic import cyclic
from pwnlib.util.cyclic import cyclic_gen
from pwnlib.util.cyclic import cyclic_find
g = cyclic_gen()
print(g.get(50))

print(cyclic(20))
print(cyclic_find(0x6161616c))


