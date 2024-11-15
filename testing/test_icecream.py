from dessert import IceCream

def test_icecream():
    testDessert = IceCream("cookies and cream", 10, 10)
    assert testDessert.calculate_cost() == 100
    assert testDessert.calculate_tax() == 7.25