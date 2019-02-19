class MenuItem:

    def __init__(self, _name, _price):
        """
        The constructor for a menu item. It saves the name of the food or drink and it's price
        :param _name: The name of the menu item
        :param _price: The price of the menu item
        """
        self.name = _name
        self.price = _price

    def set_price(self, _price):
        """
        Changes the price of the menu item
        :param _price: The new price to be set to
        :return: The new price
        """
        self.price = _price
        return self.price

    def get_price(self):
        """
        Get the price of the menu item
        :return: The current price of the menu item
        """
        return self.price

    def set_name(self, _name):
        """
        Sets a new name for the menu item
        :param _name: The new name to be set
        :return: The new name that was set
        """
        self.name = _name
        return self.name

    def get_name(self):
        """
        Gets the current name of the menu item
        :return: The current name of the menu item
        """
        return self.name

