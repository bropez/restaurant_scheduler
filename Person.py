import MenuItem as order
import menu


class Person:
    drinks = []
    food = []

    def __init__(self, _name, _drink=menu.water, _food=menu.bread):
        """
        The constructor to make a Person object sitting at the table
        :param _drink: The inital drink the person orders
        :param _food: The initial dish the person orders
        """
        self.name = _name
        self.drinks.append(_drink)
        self.food.append(_food)

    def set_name(self, _name):
        """
        Setter for the name attribute for the Person
        :param _name: The name to be changed to
        :return: No return value
        """
        self.name = _name

    def get_name(self):
        """
        The getter for the person's name
        :return: The name of the Person
        """
        return self.name

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

    def print_drinks(self):
        """
        Printing all of the items that the person ordered
        :return: No return value
        """
        for beverage in self.drinks:
            print(beverage.get_name())

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

    def print_food(self):
        """
        Prints all of the dishes that the Person has ordered
        :return: No return value
        """
        for dish in self.food:
            print(dish.get_name())

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
    # this is just testing if the class works correctly
    matthew = Person("matthew", menu.water, menu.pizza)
    matthew.remove_drink(menu.water)
    matthew.add_drink(menu.sprite)
    matthew.print_drinks()
    print(matthew.get_total())
