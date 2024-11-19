from dessert import *

class DessertShop:
    def __init__(self):
        self.order = Order()

    def user_prompt_candy(self):
        """Prompt user for candy details and create a Candy object."""
        name = input("Enter the type of candy: ")
        weight = self._get_valid_float("Enter the weight (in pounds): ")
        price = self._get_valid_float("Enter the price per pound: ")
        return Candy(name, weight, price)

    def user_prompt_cookie(self):
        """Prompt user for cookie details and create a Cookie object."""
        name = input("Enter the type of cookie: ")
        quantity = self._get_valid_int("Enter the quantity purchased: ")
        price = self._get_valid_float("Enter the price per dozen: ")
        return Cookie(name, quantity, price)

    def user_prompt_icecream(self):
        """Prompt user for ice cream details and create an IceCream object."""
        name = input("Enter the type of ice cream: ")
        scoops = self._get_valid_int("Enter the number of scoops: ")
        price = self._get_valid_float("Enter the price per scoop: ")
        return IceCream(name, scoops, price)

    def user_prompt_sundae(self):
        """Prompt user for sundae details and create a Sundae object."""
        name = input("Enter the type of ice cream: ")
        scoops = self._get_valid_int("Enter the number of scoops: ")
        price = self._get_valid_float("Enter the price per scoop: ")
        topping = input("Enter the topping: ")
        topping_price = self._get_valid_float("Enter the price for the topping: ")
        return Sundae(name, scoops, price, topping, topping_price)

    def _get_valid_float(self, prompt):
        """Helper method to get a valid float input."""
        while True:
            try:
                value = float(input(prompt))
                if value <= 0:
                    raise ValueError("The value must be positive.")
                return value
            except ValueError as e:
                print(f"Invalid input. Please enter a positive number. ({e})")

    def _get_valid_int(self, prompt):
        """Helper method to get a valid integer input."""
        while True:
            try:
                value = int(input(prompt))
                if value <= 0:
                    raise ValueError("The quantity must be positive.")
                return value
            except ValueError as e:
                print(f"Invalid input. Please enter a valid integer. ({e})")

def main():
    shop = DessertShop()

    while True:
        print("\n1: Candy")
        print("2: Cookie")
        print("3: Ice Cream")
        print("4: Sundae")
        print("What would you like to add to the order? (1-4, Enter for done): ", end="")
        choice = input().strip()

        if choice == "":
            break

        if choice == "1":
            item = shop.user_prompt_candy()
        elif choice == "2":
            item = shop.user_prompt_cookie()
        elif choice == "3":
            item = shop.user_prompt_icecream()
        elif choice == "4":
            item = shop.user_prompt_sundae()
        else:
            print("Invalid choice, please choose a valid option.")
            continue

        shop.order.add(item)

    print("\nReceipt:")
    data = [["Name", "Price", "Tax"]]
    
    subtotal = 0.0
    total_tax = 0.0
    
    for item in shop.order.order:
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
    data.append(['Total items in the order', str(len(shop.order)), ''])

    import receipt
    receipt.make_receipt(data, 'receipt.pdf')

if __name__ == "__main__":
    main()