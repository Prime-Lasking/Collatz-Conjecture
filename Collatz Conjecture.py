import matplotlib.pyplot as plt
import numpy as np
import math
N = 87
Collatz = []
def collatz(a):
    while a != 1:
        if a % 2 == 0:
            a = a // 2
            Collatz.append(math.log10(a))
        else:
            a = 3 * a + 1
            Collatz.append(math.log10(a))
collatz(N)
print(Collatz)
y = np.array(Collatz)
plt.plot(y)
plt.title(f'Collatz Sequence for {N}')
plt.xlabel('Term Index')
plt.ylabel('Value')
plt.grid(True)
plt.show()
