from die import Die
from matplotlib import pyplot as plt

num_roles = int(input("How many times should the dice get rolled? "))
roll_results = []
die = Die()
for i in range(num_roles):
    roll_results.append(die.roll())
print(roll_results)

frequencys = []
for side in range(1,die.num_sides+1):
    frequency = roll_results.count(side)
    frequencys.append(frequency)

fig, plot = plt.subplots()
plot.set_title(f"Result of rolling a {die.num_sides}-sided Dice {num_roles} times")
plot.bar(range(1,die.num_sides+1), frequencys)
plt.show()