import Person
import menu


class Table:
    def __init__(self, _chairs=3, _name="walk in"):
        """
        Constructor for the Table class
        :param _chairs: The amount of chairs set at the table
        :param _name: The optional name for a potential reservation or walk in
        """
        self.chairs = _chairs
        self.customers = []
        for person in range(self.chairs):
            self.customers.append(Person.Person(_name))
        self.reservation_holder = self.customers[0]

    def get_chairs(self):
        """
        Getter for the amount of chairs the table has
        :return: The amount of current chairs
        """
        return self.chairs

    def set_reservation_name(self, _name):
        """
        Setter for the reservation name
        :param _name: The new name that the reservation should be set to
        :return: No return value
        """
        self.reservation_holder.set_name(_name)

    def get_reservation_name(self):
        """
        Getter for the current reservation name
        :return: The current reservation name
        """
        return self.reservation_holder.get_name()

    def add_drink_order(self, chair_num, _drink):
        """
        Add a drink order to a certain customer in the chosen seat
        :param chair_num: The chosen customer to change order
        :param _drink: The drink to add to the customer's order
        :return: No return value
        """
        self.customers[chair_num].add_drink(_drink)

    def add_food_order(self, chair_num, _dish):
        """
        Add a dish order to a customer in the chosen seat
        :param chair_num: The chosen customer to change order
        :param _dish: The dish to add to the customer's order
        :return: No return value
        """
        self.customers[chair_num].add_food(_dish)

    def table_info(self):
        """
        Print the names of each of the customers sitting at the table
        :return: No return value
        """
        for customer in self.customers:
            print(customer.get_name())

    def table_total(self):
        """
        Returns the price of each of the customer's orders combined
        :return: The total price of each customer's orders combined
        """
        total = 0.00

        for customer in self.customers:
            total = total + customer.get_total()

        return total


if __name__ == "__main__":
    new_table = Table(4)
    # new_table.set_reservation_name("benny")
    # print(new_table.get_reservation_name())
    new_table.customers[0].print_food()
