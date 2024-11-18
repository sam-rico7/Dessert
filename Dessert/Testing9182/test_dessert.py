from Dessert.dessert import Candy, Cookie, IceCream, Sundae

def test_candy():
    candy = Candy("Chocolate", 2.0, 5.99)
    assert candy.name == "Chocolate"
    assert candy.candy_weight == 2.0
    assert candy.price_per_pound == 5.99

def test_cookie():
    cookie = Cookie("Chocolate Chip", 12, 3.99)
    assert cookie.name == "Chocolate Chip"
    assert cookie.cookie_quantity == 12
    assert cookie.price_per_dozen == 3.99

def test_ice_cream():
    ice_cream = IceCream("Vanilla", 3, 1.99)
    assert ice_cream.name == "Vanilla"
    assert ice_cream.scoop_count == 3
    assert ice_cream.price_per_scoop == 1.99

def test_sundae():
    sundae = Sundae("Strawberry Sundae", 2, 2.49, "Strawberries", 0.99)
    assert sundae.name == "Strawberry Sundae"
    assert sundae.scoop_count == 2
    assert sundae.price_per_scoop == 2.49
    assert sundae.topping_name == "Strawberries"
    assert sundae.topping_price == 0.99
