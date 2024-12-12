from dessert import DessertItem, IceCream

def test_iceCream_init():
    ice_cream = IceCream("Vanilla", 2, 2.99)
    name = ice_cream.get_name()
    assert name == "Vanilla"
    count = ice_cream.get_scoop_count()
    assert count == 2
    price = ice_cream.get_price_per_scoop()
    assert price == 2.99

def test_packaging():
    ice_cream = IceCream("Vanilla", 2, 2.99)
    assert ice_cream.packaging == "Bowl"
