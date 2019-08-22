import matplotlib.pyplot as plt
import numpy as np
coeff = 10;
B=1/coeff;
A = 1 - B;
a = np.zeros(100)
b = np.zeros(100)
for i in range(100):
	a[i] = i
plt.plot(a)
b[0] = a[0]
for i in np.arange(1, 100, 1):
	b[i] = b[i - 1] * A + a[i] * B
plt.plot(b)
plt.show()
