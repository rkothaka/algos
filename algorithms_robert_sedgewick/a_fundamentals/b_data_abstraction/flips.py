import counter
from random import random


trials = 1_000_000

heads = counter.Counter("heads")
tails = counter.Counter("tails")

for _ in range(trials):
    if random() < 0.5:
        heads.increment()
    else:
        tails.increment()

print(heads)
print(tails)
print(abs(heads.tally() - tails.tally()))
