import plotly.express as px

from dice import Dice

if __name__ == "__main__":
    dice_1 = Dice()
    dice_2 = Dice(10)

    results = []
    for roll_num in range(50_000):
        result = dice_1.roll() + dice_2.roll()
        results.append(result)

    # Analyze the results.
    frequencies = []
    max_result = dice_1.num_sides + dice_2.num_sides
    poss_results = range(2, max_result + 1)

    for value in poss_results:
        print(value)
        frequency = results.count(value)
        frequencies.append(frequency)

    # Visualize the results.
    title = "Results of Rolling a D6 and a D10 50,000 Times"
    labels = {'x': 'Result', 'y': 'Frequency of Result'}
    fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
    # Further customize chart.
    fig.update_layout(xaxis_dtick=1)
    fig.show()
    # fig.write_html('dice_visual_d6d10.html')