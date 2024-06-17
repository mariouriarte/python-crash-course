import matplotlib.pyplot as plt
from pprint import pprint

x_values = range(1, 1001)
# pprint(x_values)
# for x in x_values:
#     pprint(x)

y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8-poster')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, s=100)
# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
# Set size of tick labels.
ax.tick_params(labelsize=14)
ax.ticklabel_format(style='plain')
ax.scatter(x_values, y_values, color='red', s=10)
ax.scatter(x_values, y_values, color=(0, 0.8, 0), s=10)

plt.show()
# plt.savefig('squares_plot.png', bbox_inches='tight')
