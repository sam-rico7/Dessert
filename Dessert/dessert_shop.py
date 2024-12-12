from dessert import DessertItem, Candy, Cookie, IceCream, Sundae
from receipt import make_receipt

class Order():
    def __init__(self):
        self.order = []
    def add(self, dessertitem):
        self.order.append(dessertitem)
    def __len__(self):
        return len(self.order)
    def order_cost(self):
        cost = 0.0
        for item in self.order:
            cost += item.calculate_cost()
        return cost
    def order_tax(self):
        tax = 0.0
        for item in self.order:
            tax += item.calculate_cost() * (item.tax_percent/100)
        return tax
    def __str__(self):
        order_summary = []
        for item in self.order:
            order_summary.append(str(item))
        return '; '.join(order_summary)


class DessertShop():
    def user_prompt_candy(self):
        print("Type in the name of the candy(str), the weight in pounds(float), and the price per pound(float).")
        while True:
            candy_name = input("Candy name: ")
            if isinstance(candy_name, str):
                break
            else:
                print("That's not a string. Type in a string.")
                continue
            
        while True:        
            try:
                weight = float(input("Candy weight in pounds: "))
            except ValueError:
                print("That's not a float. Type in a float.")
                continue
            if isinstance(weight, float):
                break
        while True:
            try:
                price = float(input("Price per pounds: "))
            except ValueError:
                print("That's not a float. Type in a float.")
                continue
            if isinstance(price, float):
                break

        candy1 = Candy(candy_name, weight, price)
        return candy1    

    def user_prompt_cookie(self):
        print("Type in the name of the cookie(str), the amount of cookies(int), and the price per dozen(float).")
        while True:
            cookie_name = input("Cookie name: ")
            if isinstance(cookie_name, str):
                break
            else:
                print("That's not a string. Type in a string.")
                continue
        while True:
            try:       
                amount = int(input("Amount of cookies: ")) 
            except ValueError:
                print("That's not a integer. Type in a integer.")
                continue
            if isinstance(amount, int):
                break
        while True:
            try:
                price_12 = float(input("Price per dozen: "))
            except ValueError:
                print("That's not a float. Type in a float.")
                continue    
            if isinstance(price_12, float):
                break
        cookie1 = Cookie(cookie_name, amount, price_12)
        return cookie1    

    def user_prompt_icecream(self):
        print("Type in the name of the ice cream (str), the amount of scoops (int), and the price per scoop (flt)")
        while True:
            icecream_name = input("Icecream name: ")
            if isinstance(icecream_name, str):
                break
            else:
                print("That's not a string...")
                continue

        while True:
            try:
                scooby_number = int(input("How many scoops: "))
            except ValueError:
                print("That's not a integer...")
                continue
            if isinstance(scooby_number, int):
                break
        while True:
            try:
                scooby_price = float(input("Price per scoop: "))
            except ValueError:
                print("That's not a float...")
                continue
            if isinstance(scooby_price, float):
                break
            
        icecream1 = IceCream(icecream_name, scooby_number, scooby_price)
        return icecream1
        
    def user_prompt_sundae(self):
        print("Type in the name of the ice cream(str), the scoop count(int), the price per scoop(float), topping name(str), and topping price(float).")
        while True:
            sundae_name = input("Ice cream name: ")
            if isinstance(sundae_name, str):
                break
            else:
                print("That's not a string. Type in a string.")
                continue
        while True:  
            try:      
                scoop_num = int(input("Amount of scoops: "))
            except ValueError:
                print("That's not an integer. Type in an integer.")
                continue
            if isinstance(scoop_num, int):
                break

        while True:
            try:
                scoop_price = float(input("Price per scoop: "))
            except ValueError:
                print("That's not a float. Type in a float.")
                continue
            if isinstance(scoop_price, float):
                break

        while True:
            topping_name = input("Topping name: ")
            if isinstance(topping_name, str):
                break
            else:
                print("That's not a string. Type in a string.")
                continue
        while True:
            try:
                topping_price = float(input("Topping price: "))
            except ValueError:
                print("That's not a float. Type in a float.")
                continue
            if isinstance(topping_price, float):
                break

        sundae1 = Sundae(sundae_name, scoop_num, scoop_price, topping_name, topping_price)
        return sundae1
    
    
def main(Order):
    shop = DessertShop()
    order = Order()
    '''
    order.add(Candy('Candy Corn', 1.5, 0.25))
    order.add(Candy('Gummy Bears', 0.25, 0.35))
    order.add(Cookie('Chocolate Chip', 6, 3.99))
    order.add(IceCream('Pistachio', 2, 0.79))
    order.add(Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29))
    order.add(Cookie('Oatmeal Raisin', 2, 3.45))
    '''
    # boolean done = false
    done: bool = False
    # build the prompt string once
    prompt = '\n'.join([ '\n',
        '1: Candy',
        '2: Cookie',
        '3: Ice Cream',
        '4: Sunday',
        '\nWhat would you like to add to the order? (1-4, Enter for done): '
    ])

    while not done:
        choice = input(prompt)
        match choice:
            case '':
                done = True
            case '1':
                item = shop.user_prompt_candy()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case '2':
                item = shop.user_prompt_cookie()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case '3':
                item = shop.user_prompt_icecream()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case '4':
                item = shop.user_prompt_sundae()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case _:
                print('Invalid response: Please enter a choice from the menu (1-4) or Enter')
        print()

    data = [["Name", "Amount", "Price"]]
    for item in order.order:
        if isinstance(item, Candy):
            data.append([item.name, item.candy_weight, item.price_per_pound])
        elif isinstance(item, Cookie):
            data.append([item.name, item.cookie_quantity, item.price_per_dozen])
        elif isinstance(item, IceCream):
            data.append([item.name, item.scoop_count, item.price_per_scoop])
        elif isinstance(item, Sundae):
            data.append([item.name, item.scoop_count, item.price_per_scoop, item.topping_name, item.topping_price])
    data.append(["Order Subtotals", "$"+str(round(order.order_cost(), 2)), "$" + str(round(order.order_tax(), 2))])
    data.append(["Total", "", "$" + str(round(order.order_cost() + order.order_tax(), 2))])
    data.append(["Total items in the order", "", str(order.__len__())])
    import receipt
    receipt.make_receipt(data, "receipt.pdf")
    print(order)

main(Order)