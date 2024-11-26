from dessert import Sundae

def test_sundae_init():
    sundae = Sundae("Rocky Road", 2, 3.11, "Cherry", 1.00)
    name = sundae.get_name()
    assert name == "Rocky Road"
    count = sundae.get_scoop_count()
    assert count == 2
    price = sundae.get_price_per_scoop()
    assert price == 3.11
    topping = sundae.get_topping_name()
    assert topping == "Cherry"
    topping_price = sundae.get_topping_price()
    assert topping_price == 1.00