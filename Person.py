import MenuItem as order


class Person:
    drinks = []
    food = []

    def __init__(self, _drink, _food):
        """
        The constructor to make a Person object sitting at the table
        :param _drink: The inital drink the person orders
        :param _food: The initial dish the person orders
        """
        self.drinks.append(_drink)
        self.food.append(_food)

    def add_drink(self, _drink):
        """
        If the person would like a different drink then use this function
        :param _drink: The drink that needs to be added to the order
        :return: no return value
        """
        self.drinks.append(_drink)

    def remove_drink(self, _drink):
        """
        This removes a drink from the order for whatever reason. If the drink
        is not found it'll print that the order doesn't have the drink
        :param _drink: The drink to be removed
        :return: no return value
        """
        try:
            self.drinks.remove(_drink)
        except ValueError:
            print("This order doesn't have that drink.")

    def add_food(self, _food):
        """
        This adds a food item to the order
        :param _food: The food item to be added
        :return: no return item
        """
        self.food.append(_food)

    def remove_food(self, _food):
        """
        If need be, this removes a food item from the order. If the food item
        cannot be found then it'll print out that the food item cannot be found
        in the order.
        :param _food: The food item to be removed
        :return: no return value
        """
        try:
            self.food.remove(_food)
        except ValueError:
            print("This order doesn't have that food.")

    def get_total(self):
        """
        This gets the total price of the order by adding all of the prices together
        :return: The total price of the order
        """
        total = 0.00

        for _drink in self.drinks:
            total = total + _drink.get_price()

        for _food in self.food:
            total = total + _food.get_price()

        return total


if __name__ == "__main__":
    water = order.MenuItem("water", 0.00)
    soda = order.MenuItem("soda", 3.99)
    pizza = order.MenuItem("pizza", 5.00)
    lasagna = order.MenuItem("lasagna", 4.00)

    matthew = Person(water, pizza)
    matthew.remove_drink(water)
    matthew.add_drink(soda)
    print(matthew.get_total())