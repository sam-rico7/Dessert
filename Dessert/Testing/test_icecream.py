from dessert import IceCream

def test_ice_cream():
    test_icecream_1 = IceCream("Starwberry", 2, 2.50)
    test_icecream_2 = IceCream("Chocolate", 3, 1.75)
    test_icecream_3 = IceCream("Pecan", 1, 3.50)
    
    assert test_icecream_1.get_cost() == 2.50
    assert test_icecream_1.get_scoop() == 2
    assert test_icecream_1.get_name() == "Starwberry"

    assert test_icecream_2.get_cost() == 1.75
    assert test_icecream_2.get_scoop() == 3
    assert test_icecream_2.get_name() == "Chocolate"

    assert test_icecream_3.get_cost() == 3.50
    assert test_icecream_3.get_scoop() == 1
    assert test_icecream_3.get_name() == "Pecan"
