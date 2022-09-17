# Deque max_len demo

from collections import deque

d = deque([], maxlen=3)

for i in range(6):
    d.append(i)
    print(d)