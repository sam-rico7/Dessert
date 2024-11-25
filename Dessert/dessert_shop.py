from dessert import Candy, Cookie, IceCream, Sundae, Order

class DessertShop:
    @staticmethod
    def user_prompt_candy():
        name = input("Enter the type of candy: ").strip()
        while True:
            try:
                weight = float(input("Enter the weight (in lbs): "))
                if weight < 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a positive number for weight.")
        while True:
            try:
                price_per_pound = float(input("Enter the price per pound: "))
                if price_per_pound < 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a positive number for price.")
        return Candy(name, weight, price_per_pound)

    @staticmethod
    def user_prompt_cookie():
        name = input("Enter the type of cookie: ").strip()
        while True:
            try:
                quantity = int(input("Enter the quantity purchased: "))
                if quantity < 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a positive integer for quantity.")
        while True:
            try:
                price_per_dozen = float(input("Enter the price per dozen: "))
                if price_per_dozen < 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a positive number for price.")
        return Cookie(name, quantity, price_per_dozen)

    @staticmethod
    def user_prompt_icecream():
        name = input("Enter the type of ice cream: ").strip()
        while True:
            try:
                scoops = int(input("Enter the number of scoops: "))
                if scoops < 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a positive integer for scoops.")
        while True:
            try:
                price_per_scoop = float(input("Enter the price per scoop: "))
                if price_per_scoop < 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a positive number for price.")
        return IceCream(name, scoops, price_per_scoop)

    @staticmethod
    def user_prompt_sundae():
        name = input("Enter the type of ice cream: ").strip()
        while True:
            try:
                scoops = int(input("Enter the number of scoops: "))
                if scoops < 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a positive integer for scoops.")
        while True:
            try:
                price_per_scoop = float(input("Enter the price per scoop: "))
                if price_per_scoop < 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a positive number for price.")
        topping = input("Enter the topping: ").strip()
        while True:
            try:
                topping_price = float(input("Enter the price for the topping: "))
                if topping_price < 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a positive number for topping price.")
        return Sundae(name, scoops, price_per_scoop, topping, topping_price)


def main():
    order = Order()
    while True:
        print("1: Candy")
        print("2: Cookie")
        print("3: Ice Cream")
        print("4: Sundae")
        choice = input("What would you like to add to the order? (1-4, Enter for done): ").strip()
        if not choice:
            break
        if choice == '1':
            order.add(DessertShop.user_prompt_candy())
        elif choice == '2':
            order.add(DessertShop.user_prompt_cookie())
        elif choice == '3':
            order.add(DessertShop.user_prompt_icecream())
        elif choice == '4':
            order.add(DessertShop.user_prompt_sundae())
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, or press Enter to finish.")

    data = [["Name", "Cost", "Tax"]]
    subtotal = 0.0
    total_tax = 0.0

    for item in order.order:
        cost = item.calculate_cost()
        tax = item.calculate_tax()
        subtotal += cost
        total_tax += tax
        data.append([item.name, f"${cost:.2f}", f"${tax:.2f}"])

    total_cost = subtotal + total_tax
    data.append(['Order Subtotals', f"${subtotal:.2f}", f"${total_tax:.2f}"])
    data.append(['Order Total', f"${total_cost:.2f}", ''])
    data.append(['Total items in the order', str(len(order)), ''])

    import receipt
    receipt.make_receipt(data, 'receipt.pdf')


if __name__ == "__main__":
    main()
