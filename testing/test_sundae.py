from dessert import Sundae

def test_sundae():
    testDessert = Sundae("banana split", 10, 10, "swiss cheese", 10)
    assert testDessert.calculate_cost() == 200
    assert testDessert.calculate_tax() == 14.5