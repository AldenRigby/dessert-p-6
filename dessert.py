class DessertItem:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Dessert: {self.name}"

class Candy(DessertItem):
    def __init__(self, name, candyWeight, pricePerPound):
        super().__init__(name)
        self.candyWeight = candyWeight
        self.pricePerPound = pricePerPound

class Cookie(DessertItem):
    def __init__(self, name, cookieQuantity, pricePerDozen):
        super().__init__(name)
        self.cookieQuantity = cookieQuantity
        self.pricePerDozen = pricePerDozen

class IceCream(DessertItem):
    def __init__(self, name, scoopCount, pricePerScoop):
        super().__init__(name)
        self.scoopCount = scoopCount
        self.pricePerScoop = pricePerScoop

class Sundae(IceCream):
    def __init__(self, name, scoopCount, pricePerScoop, toppingName, toppingPrice):
        super().__init__(name, scoopCount, pricePerScoop)
        self.toppingName = toppingName
        self.toppingPrice = toppingPrice