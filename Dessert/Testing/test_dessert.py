from dessert import *

def test_tax():
    test_1 = Candy("Pirulin")
    assert test_1.tax_percent == 7.25

    
def test_tax_percent():
    candy1 = Candy("Chocolate", 3.5, 1.5)
    assert candy1.tax_percent == 7.25
    
def test_calculate_cost():
    candy = Candy("Chocolate", 3.5, 1.5)
    cost = candy.get_candy_weight() * candy.get_price_per_pound()
    assert candy.calculate_cost() == cost
    cookie = Cookie("Chocolate chip", 12, 15.60)
    cost = cookie.get_cookie_quantity() * (cookie.get_price_per_dozen()/12)
    assert cookie.calculate_cost() == cost
    ice_cream = IceCream("Vanilla", 2, 2.99)
    cost = ice_cream.get_scoop_count() * ice_cream.get_price_per_scoop()
    assert ice_cream.calculate_cost() == cost
    sundae = Sundae("Rocky Road", 2, 3.11, "Cherry", 1.00)
    cost = sundae.get_scoop_count() * sundae.get_price_per_scoop() + sundae.get_topping_price()
    assert sundae.calculate_cost() == cost

def test_calculate_tax():
    candy = Candy("Chocolate", 3.5, 1.5)
    tax = candy.calculate_cost() * (7.25/100)
    assert candy.calculate_tax() == tax

    cookie = Cookie("Chocolate chip", 12, 15.60)
    tax = cookie.calculate_cost() * (7.25/100)
    assert cookie.calculate_tax() == tax

    ice_cream = IceCream("Vanilla", 2, 2.99)
    tax = ice_cream.calculate_cost() * (7.25/100)
    assert ice_cream.calculate_tax() == tax

    sundae = Sundae("Rocky Road", 2, 3.11, "Cherry", 1.00)
    tax = sundae.calculate_cost() * (7.25/100)
    assert sundae.calculate_tax() == tax
