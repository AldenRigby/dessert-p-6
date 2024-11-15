from dessert import Order, DessertItem, Candy, Cookie, IceCream, Sundae
from receipt import make_receipt

def main():
    mainOrder = Order()
    mainOrder.add(Candy("Candy Corn", 1.5, .25))
    mainOrder.add(Candy("Gummy Bears", .25, .35))
    mainOrder.add(Cookie("Chocolate Chip", 6, 3.99))
    mainOrder.add(IceCream("Pistachio", 2, .79))
    mainOrder.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    mainOrder.add(Cookie("Oatmeal Raisin", 2, 3.45))

    tempData = [["Name", "Item Cost", "Tax" ]]
    for i in mainOrder.order:
        tempData.append([])
        tempData[-1].append(str(i))
        tempData[-1].append(i.calculate_cost())
        tempData[-1].append(i.calculate_tax())
    tempData.append(["Order Subtotals", mainOrder.order_cost(), mainOrder.order_tax()])
    tempData.append(["Order Total", "", round(mainOrder.order_cost() + mainOrder.order_tax(), 2)])
    tempData.append(["Total Items", "", str(len(mainOrder.order))])
    make_receipt(tempData, "receipt.pdf")

main()