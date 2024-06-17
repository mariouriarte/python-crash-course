from random import randint
from pprint import pprint
import plotly.express as px


class Dice:
    """A class representing a single die."""

    def __init__(self, num_sides=6):
        """Assume a six-sided dice."""
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)


if __name__ == "__main__":
    dice = Dice()
    print('One dice')

    results = []
    for roll_num in range(1000):
        result = dice.roll()
        results.append(result)
    print(results)

    # analyze the results
    frequencies = []
    poss_results = range(1, dice.num_sides + 1)
    pprint(poss_results)
    for value in poss_results:
        frequency = results.count(value)
        frequencies.append(frequency)

    # pprint(frequencies)

    # Visualize the results.
    title = "Results of Rolling One D6 1,000 Times"
    labels = {'x': 'Result', 'y': 'Frequency of Result'}
    fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
    fig.show()
