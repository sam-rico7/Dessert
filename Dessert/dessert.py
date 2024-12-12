from abc import ABC, abstractmethod
from packaging import Packaging

class DessertItem(ABC, Packaging):
    def __init__(self, name):
        self.name = name
        self.tax_percent = 7.25
        self.packaging = None
    def __str__(self):
        return f"You ordered a {self.name}"
    def get_name(self):
        return self.name
    def calculate_tax(self):
        return round(self.calculate_cost() * (self.tax_percent/100), 2)

    @abstractmethod
    def calculate_cost(self):
        pass
    
class Candy(DessertItem):
    def __init__(self, name, candy_weight, price_per_pound):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound
        self.packaging = "Bag"
    def get_candy_weight(self):
        return self.candy_weight
    def get_price_per_pound(self):
        return self.price_per_pound
    def calculate_cost(self):
        return round(self.candy_weight * self.price_per_pound, 2)
    def __str__(self):
        return f"{self.name} ({self.packaging}), {self.candy_weight}lbs, ${self.price_per_pound}/lbs, ${self.calculate_cost()}, ${self.calculate_tax()}"
    
class Cookie(DessertItem):
    def __init__(self, name, cookie_quantity, price_per_dozen):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen
        self.packaging = "Box"
    def get_cookie_quantity(self):
        return self.cookie_quantity
    def get_price_per_dozen(self):
        return self.price_per_dozen
    def calculate_cost(self):
        return round(self.cookie_quantity * (self.price_per_dozen/12), 2)
    def __str__(self):
        return f"{self.name} ({self.packaging}), {self.cookie_quantity} cookie(s), ${self.price_per_dozen}/dozen, ${self.calculate_cost()}, ${self.calculate_tax()}"
    
class IceCream(DessertItem):
    def __init__(self, name, scoop_count, price_per_scoop):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
        self.packaging = "Bowl"
    def get_scoop_count(self):
        return self.scoop_count
    def get_price_per_scoop(self):
        return self. price_per_scoop
    def calculate_cost(self):
        return round(self.scoop_count * self.price_per_scoop, 2)
    def __str__(self):
        return f"{self.name} ({self.packaging}), {self.scoop_count} scoop(s), ${self.price_per_scoop}/scoop, ${self.calculate_cost()}, ${self.calculate_tax()}"

class Sundae(IceCream):
    def __init__(self, name, scoop_count, price_per_scoop, topping_name, topping_price):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price
        self.packaging = "Boat"
    def get_topping_name(self):
        return self.topping_name
    def get_topping_price(self):
        return self.topping_price
    def calculate_cost(self):
        return round((self.scoop_count * self.price_per_scoop) + self.topping_price, 2)
    def __str__(self):
        return f"{self.name} ({self.packaging}), {self.scoop_count} scoop(s), ${self.price_per_scoop}/scoop, {self.topping_name}, ${self.topping_price}, ${self.calculate_cost()}, ${self.calculate_tax()}"