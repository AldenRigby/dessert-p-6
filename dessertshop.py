from dessert import Order, DessertItem, Candy, Cookie, IceCream, Sundae

from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle 
from reportlab.lib import colors 
from reportlab.lib.pagesizes import A4 
from reportlab.lib.styles import getSampleStyleSheet 

class DessertShop():
    def __init__(self):
        pass
    def user_prompt_candy(self):
        name = input("What is the name of your candy? ")
        weight = 0
        while True:
            try:
                weight = float(input("How much does your candy weigh in pounds? "))
                break
            except:
                print("Please enter a valid weight.")
        price = 0
        while True:
            try:
                price = float(input("How much does your candy cost per pound? "))
                break
            except:
                print("Please enter a valid price.")
        return Candy(name, weight, price)
    
    def user_prompt_cookie(self):
        name = input("What is the name of your cookie?")
        num = 0
        while True:
            try:
                num = int(input("How many cookies do you have? "))
                break
            except:
                print("Please enter a valid number.")
        price = 0
        while True:
            try:
                price = float(input("How much do your cookies cost per dozen? "))
                break
            except:
                print("Please enter a valid price.")
        return Cookie(name, num, price)
    
    def user_prompt_icecream(self):
        name = input("What is the name of your ice cream? ")
        scoops = 0
        while True:
            try:
                scoops = int(input("How many scoops of ice cream do you have? "))
                break
            except:
                print("Please enter a valid number.")
        price = 0
        while True:
            try:
                price = float(input("How much does your ice cream cost per scoop? "))
                break
            except:
                print("Please enter a valid price.")
        return IceCream(name, scoops, price)
    
    def user_prompt_sundae(self):
        name = input("What is the name of your ice cream? ")
        scoops = 0
        while True:
            try:
                scoops = int(input("How many scoops of ice cream do you have? "))
                break
            except:
                print("Please enter a valid number.")
        price = 0
        while True:
            try:
                price = float(input("How much does your ice cream cost per scoop? "))
                break
            except:
                print("Please enter a valid price.")
        topping = input("What is the name of your topping?")
        toppingPrice = 0
        while True:
            try:
                toppingPrice = float(input("How much does your topping cost per scoop? "))
                break
            except:
                print("Please enter a valid number.")
        return Sundae(name, scoops, price, topping, toppingPrice)

def make_receipt(data, out_file_name=""):
    tempData = [["Name", "Item Cost", "Tax" ]]
    for i in data.order:
        tempData.append([])
        tempData[-1].append(f"{i.name} ({i.packaging})")
        tempData[-1].append(i.calculate_cost())
        tempData[-1].append(i.calculate_tax())
    tempData.append(["Order Subtotals", data.order_cost(), data.order_tax()])
    tempData.append(["Order Total", "", round(data.order_cost() + data.order_tax(), 2)])
    tempData.append(["Total Items", "", str(len(data.order))])

    pdf = SimpleDocTemplate( out_file_name, pagesize = A4 ) 
    styles = getSampleStyleSheet() 
    title_style = styles[ "Heading1" ] 
    title_style.alignment = 1
    title = Paragraph( "receipt" , title_style ) 
    style = TableStyle( 
        [ 
            ( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ), 
            ( "BOX" , ( 0, 0 ), (6 , 6 ), 1 , colors.black ), 
            ( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.gray ), 
            ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ), 
            ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ), 
            ( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ), 
        ] 
    ) 
    
    table = Table( tempData , style = style ) 
    pdf.build([ title , table ]) 

def main():
    shop = DessertShop()
    order = Order()
    '''
    order.add(Candy('Candy Corn', 1.5, 0.25))
    order.add(Candy('Gummy Bears', 0.25, 0.35))
    order.add(Cookie('Chocolate Chip', 6, 3.99))
    order.add(IceCream('Pistachio', 2, 0.79))
    order.add(Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29))
    order.add(Cookie('Oatmeal Raisin', 2, 3.45))
    '''
    # boolean done = false
    done: bool = False
    # build the prompt string once
    prompt = '\n'.join([ '\n',
    '1: Candy',
    '2: Cookie',
    '3: Ice Cream',
    '4: Sunday',
    '\nWhat would you like to add to the order? (1-4, Enter for done): '
    ])
    while not done:
        choice = input(prompt)
        match choice:
            case '':
                done = True
            case '1':
                item = shop.user_prompt_candy()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case '2':
                item = shop.user_prompt_cookie()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case '3':
                item = shop.user_prompt_icecream()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case '4':
                item = shop.user_prompt_sundae()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case _:
                print('Invalid response: Please enter a choice from the menu (1-4) or Enter')
    print()

    make_receipt(order, "receipt.pdf")

    print(order)


main()