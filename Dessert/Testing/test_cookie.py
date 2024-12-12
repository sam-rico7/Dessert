from dessert import DessertItem, Cookie

def test_cookie_init():
    cookie = Cookie("Chocolate chip", 12, 15.60)
    name = cookie.get_name()
    assert name == "Chocolate chip"
    quant = cookie.get_cookie_quantity()
    assert quant == 12
    price = cookie.get_price_per_dozen()
    assert price == 15.60

def test_packaging():
    cookie = Cookie("Chocolate chip", 12, 15.60)
    assert cookie.packaging == "Box"