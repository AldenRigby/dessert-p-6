from dessert import Candy

def test_candy():
    testDessert = Candy("airhead", 10, 10)
    assert testDessert.calculate_cost() == 100
    assert testDessert.calculate_tax() == 7.25