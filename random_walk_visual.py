import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk(100000)
rw.fill_walk()

fig, plot = plt.subplots()
plot.scatter(rw.xvalues,rw.yvalues, s=15)
plt.show()
