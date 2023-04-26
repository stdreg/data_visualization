import matplotlib.pyplot as plt

squares = [0, 1,4,9,16,25,36,49]
doubles = [0, 1,2,4,8,16,32,64]

#existing pre-defined styles
print(plt.style.available)
plt.style.use("seaborn-v0_8-dark")

fig, plot = plt.subplots() # fig is the full representation, plot is one plot
plot.plot(squares)
#plot.plot(doubles, linewidth=3)
for d in doubles: # a plot can show mulitple series of data
    plot.scatter(doubles.index(d), d, s=50) #scatter to set points

#using a colormap for squares - the higher the value, the darker the point
squares_index = range(0,8)
plot.scatter(squares_index, squares, c=squares, cmap=plt.cm.Blues, s=20)


#set chart-Title and label axes
plot.set_title("Square-Numbers and Doubles", fontsize=24)
plot.set_xlabel("Value", fontsize=14);
plot.set_ylabel("Double/Square", fontsize=14);
#set size of tick-labels
plot.tick_params(axis="both", labelsize=14)

plt.show()
