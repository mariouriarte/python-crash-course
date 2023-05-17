def make_pizza(size, *toppings, **kwargs):
    """Summarize the pizza we are about to make."""

    print(f'\nMaking a {size}-inch pizza whit the following toppings:')

    for topping in toppings:
        print(f'- {topping}')

    if kwargs:
        print(kwargs)
