from dessert import DessertItem, Candy, Cookie, IceCream, Sundae

def test_candy():
    testDessert = Candy("skittle", 12234234, 92834798345345)
    assert testDessert.name == "skittle"
    assert testDessert.candyWeight == 12234234
    assert testDessert.pricePerPound == 92834798345345
def test_cookie():
    testDessert = Cookie("snickerdoodle", 12234234, 92834798345345)
    assert testDessert.name == "snickerdoodle"
    assert testDessert.cookieQuantity == 12234234
    assert testDessert.pricePerDozen == 92834798345345
def test_candy():
    testDessert = Candy("skittle", 12234234, 92834798345345)
    assert testDessert.awef() == "skittle"
def test_candy():
    testDessert = Candy("skittle", 12234234, 92834798345345)
    assert testDessert.awef() == "skittle"
def test_candy():
    testDessert = Candy("skittle", 12234234, 92834798345345)
    assert testDessert.awef() == "skittle"