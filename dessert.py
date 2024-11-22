from abc import ABC, abstractmethod
class Order:
    def __init__(self, order = []):
        self.order = order

    def add(self, item):
        self.order.append(item)
        return self.order
    
    def order_cost(self):
        cost = 0
        for i in self.order:
            cost += i.calculate_cost()
        return round(cost, 2)
    
    def order_tax(self):
        cost = 0
        for i in self.order:
            cost += i.calculate_tax()
        return cost

class DessertItem(ABC):
    def __init__(self, name, tax_percent = 7.25):
        self.name = name
        self.tax_percent = tax_percent

    def __str__(self):
        return f"{self.name}"
    
    def calculate_tax(self):
        return round(self.calculate_cost() * self.tax_percent / 100, 2)

    @abstractmethod
    def calculate_cost(self):
        return self

class Candy(DessertItem):
    def __init__(self, name, candyWeight, pricePerPound):
        super().__init__(name)
        self.candyWeight = candyWeight
        self.pricePerPound = pricePerPound

    def __str__(self): #copy and paste this .................
        return f"{self.name}, {self.candyWeight}lbs, ${self.pricePerPound}/lb, ${self.calculate_cost}, ${self.calculate_tax}"
    
    def calculate_cost(self):
        return round(self.candyWeight * self.pricePerPound, 2)

class Cookie(DessertItem):
    def __init__(self, name, cookieQuantity, pricePerDozen):
        super().__init__(name)
        self.cookieQuantity = cookieQuantity
        self.pricePerDozen = pricePerDozen
    
    def calculate_cost(self):
        return round(self.cookieQuantity * self.pricePerDozen / 12, 2)

class IceCream(DessertItem):
    def __init__(self, name, scoopCount, pricePerScoop):
        super().__init__(name)
        self.scoopCount = scoopCount
        self.pricePerScoop = pricePerScoop
    
    def calculate_cost(self):
        return round(self.scoopCount * self.pricePerScoop, 2) 

class Sundae(IceCream):
    def __init__(self, name, scoopCount, pricePerScoop, toppingName, toppingPrice):
        super().__init__(name, scoopCount, pricePerScoop)
        self.toppingName = toppingName
        self.toppingPrice = toppingPrice
    
    def calculate_cost(self):
        return round(self.scoopCount * (self.pricePerScoop + self.toppingPrice), 2)

