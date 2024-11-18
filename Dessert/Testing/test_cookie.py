from dessert import Cookie

def test_cookie():
    test_cookies_1 = Cookie("choclate chip", 36, 3.75)
    test_cookies_2 = Cookie("Snicker doodle", 24, 5.50)
    test_cookies_3 = Cookie("Sugar", 48, 3.50)
    
    assert test_cookies_1.get_amount() == 36
    assert test_cookies_1.get_cost() == 3.75
    assert test_cookies_1.get_name() == "choclate chip"

    assert test_cookies_2.get_amount() == 24
    assert test_cookies_2.get_cost() == 5.50
    assert test_cookies_2.get_name() == "Snicker doodle"

    assert test_cookies_3.get_amount() == 48
    assert test_cookies_3.get_cost() == 3.50
    assert test_cookies_3.get_name() == "Sugar"