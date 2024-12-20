
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-3,3,100)
y=np.sin(np.pi*x)
#设置画布大小为
plt.figure(figsize=(8,6))
plt.title(r'$y=\sin(\pi\times x)$')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, y, color='green', lw=2, linestyle='-', label='sin(x)')
plt.legend(loc='lower right')
plt.savefig("f.eps")