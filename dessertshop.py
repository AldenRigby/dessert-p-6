from dessert import Order, DessertItem, Candy, Cookie, IceCream, Sundae
def main():
    mainOrder = Order()
    mainOrder.add(Candy("Candy Corn", 1.5, .25))
    mainOrder.add(Candy("Gummy Bears", .25, .35))
    mainOrder.add(Cookie("Chocolate Chip", 6, 3.99))
    mainOrder.add(IceCream("Pistachio", 2, .79))
    mainOrder.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    mainOrder.add(Cookie("Oatmeal Raisin", 2, 3.45))
    for i in mainOrder.order:
        print(i)
    print("Items in order: " + str(len(mainOrder.order)))

main()