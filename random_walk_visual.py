import matplotlib.pyplot as plt
from random_walk import RandomWalk


while True:
    steps = int(input("How many steps for the next walk? (<=0 to stop): "))
    if steps < 1:
        break

    rw = RandomWalk(steps)
    rw.fill_walk()    

    plt.style.use("classic")
    fig, plot = plt.subplots()
    point_numbers = range(rw.num_of_points)
    #emphasize start and end
    plot.scatter(rw.xvalues[0],rw.yvalues[0], c='Green', edgecolors='none', s=100)
    plot.scatter(rw.xvalues[-1],rw.yvalues[-1], c='Red', edgecolors='none', s=100)
    #color each point more dark the further the walk has gone
    plot.scatter(rw.xvalues,rw.yvalues, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=5)

    plot.get_xaxis().set_visible(False)
    plot.get_yaxis().set_visible(False)    
    plt.show()
