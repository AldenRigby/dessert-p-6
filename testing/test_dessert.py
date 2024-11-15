from dessert import Candy

def test_dessert():
    testDessert = Candy("skittle", 10, 10)
    assert testDessert.tax_percent == 7.25