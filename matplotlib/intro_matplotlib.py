import matplotlib.pyplot as plt
import scipy as scipy
from scipy import stats

x = [11,15,20, 21, 45, 58]
y = [5,10,15,23, 56, 34]

plt.xlabel("Variable x")
# Text(0.5, 0, 'variable x')
plt.ylabel("Variable y")
# Text(0.5, 0, 'variable y')
plt.title("Mi primer gráfico")
# Text(0.5,1.0,'mi primer gráfico')

plt.grid(True)
plt.plot(x,y)
plt.show()

stats.describe(temp)