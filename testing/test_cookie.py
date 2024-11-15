from dessert import Cookie

def test_cookie():
    testDessert = Cookie("snickerdoodle", 12, 10)
    assert testDessert.calculate_cost() == 10
    assert testDessert.calculate_tax() == .72