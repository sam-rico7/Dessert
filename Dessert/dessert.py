from abc import ABC, abstractmethod

class DessertItem(ABC):
    tax_percent: float = 7.25   
    def __init__(self, name: str):
        self.name = name
    @abstractmethod
    def calculate_cost(self) -> float:
        pass
    def calculate_tax(self) -> float:
        return self.calculate_cost() * (self.tax_percent / 100)
    def __str__(self):
        return self.name


class Candy(DessertItem):
    def __init__(self, name: str = '', candy_weight: float = 0.0, price_per_pound: float = 0.0):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound
    def calculate_cost(self) -> float:
        return self.candy_weight * self.price_per_pound


class Cookie(DessertItem):
    def __init__(self, name: str = '', cookie_quantity: int = 0, price_per_dozen: float = 0.0):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen
    def calculate_cost(self) -> float:
        return (self.cookie_quantity / 12) * self.price_per_dozen


class IceCream(DessertItem):
    def __init__(self, name: str = '', scoop_count: int = 0, price_per_scoop: float = 0.0):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
    def calculate_cost(self) -> float:
        return self.scoop_count * self.price_per_scoop


class Sundae(IceCream):
    def __init__(self, name: str = '', scoop_count: int = 0, price_per_scoop: float = 0.0, 
                 topping_name: str = '', topping_price: float = 0.0):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price
    def calculate_cost(self) -> float:
        return super().calculate_cost() + self.topping_price


class Order:
    def __init__(self):
        self.order = []
    def add(self, item: DessertItem):
        self.order.append(item)
    def __len__(self):
        return len(self.order)
    def order_cost(self) -> float:
        return sum(item.calculate_cost() for item in self.order)
    def order_tax(self) -> float:
        return sum(item.calculate_tax() for item in self.order)


def main():
    orderone = Order()
    orderone.add(Candy("Candy Corn", 1.5, .25))
    orderone.add(Candy("Gummy Bears", .25, .35))
    orderone.add(Cookie("Chocolate Chip", 6, 3.99))
    orderone.add(IceCream("Pistachio", 2, .79))
    orderone.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    orderone.add(Cookie("Oatmeal Raisin", 2, 3.45))

    data = [["Name", "Price", "Tax"]]
    
    subtotal = 0.0
    total_tax = 0.0
    
    for item in orderone.order:
        cost = item.calculate_cost()
        tax = item.calculate_tax()
        
        subtotal += cost
        total_tax += tax
        
        cost_str = f"${cost:.2f}"
        tax_str = f"${tax:.2f}"
        
        data.append([item.name, cost_str, tax_str])
    
    total_cost = subtotal + total_tax
    data.append(['Order Subtotals', f"${subtotal:.2f}", f"${total_tax:.2f}"])
    data.append(['Order Total', f"${total_cost:.2f}", ''])
    data.append(['Total items in the order', str(len(orderone)), ''])

    import receipt
    receipt.make_receipt(data, 'receipt.pdf')


if __name__ == "__main__":
    main()