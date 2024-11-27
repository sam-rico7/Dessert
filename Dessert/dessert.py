from abc import ABC, abstractmethod
from typing import Optional
from packaging import Packaging

class DessertItem(ABC, Packaging):
    def __init__(self, name):
        self.name = name
        self.tax_percent = 7.25
        self.packaging: Optional[str] = None  # Default is None

    def __str__(self):
        return f"{self.name} ({self.packaging})"

    def get_name(self):
        return self.name

    def calculate_tax(self):
        return self.calculate_cost() * (self.tax_percent / 100)

    @abstractmethod
    def calculate_cost(self):
        pass


class Candy(DessertItem):
    def __init__(self, name, candy_weight, price_per_pound):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound
        self.packaging = "Bag"  # Default packaging for Candy

    def __str__(self):
        return f"{self.name} ({self.packaging}), {self.candy_weight}lbs, " \
               f"${self.price_per_pound}/lb, Cost: ${self.calculate_cost():.2f}, Tax: ${self.calculate_tax():.2f}"

    def get_candy_weight(self):
        return self.candy_weight

    def get_price_per_pound(self):
        return self.price_per_pound

    def calculate_cost(self):
        return self.candy_weight * self.price_per_pound


class Cookie(DessertItem):
    def __init__(self, name, cookie_quantity, price_per_dozen):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen
        self.packaging = "Box"  # Default packaging for Cookie

    def __str__(self):
        return f"{self.name} ({self.packaging}), {self.cookie_quantity} cookies, " \
               f"${self.price_per_dozen}/dozen, Cost: ${self.calculate_cost():.2f}, Tax: ${self.calculate_tax():.2f}"

    def get_cookie_quantity(self):
        return self.cookie_quantity

    def get_price_per_dozen(self):
        return self.price_per_dozen

    def calculate_cost(self):
        return self.cookie_quantity * (self.price_per_dozen / 12)


class IceCream(DessertItem):
    def __init__(self, name, scoop_count, price_per_scoop):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
        self.packaging = "Bowl"  # Default packaging for Ice Cream

    def __str__(self):
        return f"{self.name} ({self.packaging}), {self.scoop_count} scoops, " \
               f"${self.price_per_scoop}/scoop, Cost: ${self.calculate_cost():.2f}, Tax: ${self.calculate_tax():.2f}"

    def get_scoop_count(self):
        return self.scoop_count

    def get_price_per_scoop(self):
        return self.price_per_scoop

    def calculate_cost(self):
        return self.scoop_count * self.price_per_scoop


class Sundae(IceCream):
    def __init__(self, name, scoop_count, price_per_scoop, topping_name, topping_price):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price
        self.packaging = "Boat"  # Default packaging for Sundae

    def __str__(self):
        return f"{self.name} Sundae ({self.packaging}), {self.scoop_count} scoops, " \
               f"Topping: {self.topping_name}, Cost: ${self.calculate_cost():.2f}, Tax: ${self.calculate_tax():.2f}"

    def get_topping_name(self):
        return self.topping_name

    def get_topping_price(self):
        return self.topping_price

    def calculate_cost(self):
        return (self.scoop_count * self.price_per_scoop) + self.topping_price

