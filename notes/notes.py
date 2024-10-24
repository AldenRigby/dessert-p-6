class Store:
    name = "BBQ Grill"
    def __init__(self, id):
        self.id = id
        self.desserts = []
        self.featuredDessert = None

    def addDessert(self, dessert):
        assert isinstance(dessert, DessertItem)
        #true false: if false, stops code
        #isinstance is like isnum, checks if it's an instance of that clas
        self.desserts.append(dessert)

    def removeDessert(self, dessert):
        try:
            self.desserts.remove(dessert)
        except:
            print("nuh uh")
        else:
            print(dessert, "removed.")

    def feature(self, name):
        for dessert in self.desserts:
            if dessert.name == name:
                self.featuredDessert = name
                print("Featured dessert is", name)
                break
        else:
            print("nuh uh")
    
    def getFeatured(self):
        return self.featuredDessert
    
    def store(self):
        for dessert in self.desserts:
            dessert.eat()

    def getCandies(self):
        return self.getByType(Candy)
    def getCookies(self):
        return self.getByType(Cookie)
    def getByType(self, typ):
        return [str(dessert) for dessert in self.desserts if isinstance(dessert, typ)]
class DessertItem:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Dessert: {self.name}"
    
    def eat(self):
        print(self.name, "eating", self.diet)

class Candy(DessertItem):
    pass

class Skittle(Candy):
    diet = "mice"

class KitKat(Candy):
    diet = "potato"

class Cookie(DessertItem):
    pass

class Snickerdoodle(Cookie):
    diet = "rodents"

class ChocolateChip(Cookie):
    diet = "carrots"

store = Store(1)
store.addDessert(Snickerdoodle("awefawefawefawefwefawef"))
store.addDessert(Skittle("whee hee hee hee"))
store.addDessert(KitKat("potato"))
store.addDessert(ChocolateChip("google en passant"))

store.feature("potato")
store.store()

print(store.getByType(Cookie))