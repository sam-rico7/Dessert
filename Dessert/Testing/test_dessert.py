from dessert import DessertItem, Candy

def test_tax():
    test_1 = Candy("Pirulin")
    assert test_1.tax_percent == 7.25
