# defaultdict demo

from collections import defaultdict

dd = defaultdict(int)

s = 'The Brown Quick Fox jumps over the Lazy Dog'

words = s.split()

for word in words:
    dd[word] += 1

for k, v in dd:
    print(f"{k} : {v}")