from dessert import Candy

def test_candy():
    testcandy_1 = Candy("Jolly Ranchers", 2, 6.50)

    name = testcandy_1.get_name()
    assert name == "Jolly Ranchers"
    
    assert testcandy_1.get_weight() == 2
    assert testcandy_1.get_cost() == 6.50
    assert testcandy_1.get_name() == "Jolly Ranchers"
