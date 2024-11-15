from dessert import Order, DessertItem, Candy, Cookie, IceCream, Sundae

from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle 
from reportlab.lib import colors 
from reportlab.lib.pagesizes import A4 
from reportlab.lib.styles import getSampleStyleSheet 

def make_receipt(data, out_file_name=""):
    tempData = [["Name", "Item Cost", "Tax" ]]
    for i in data.order:
        tempData.append([])
        tempData[-1].append(str(i))
        tempData[-1].append(i.calculate_cost())
        tempData[-1].append(i.calculate_tax())
    tempData.append(["Order Subtotals", data.order_cost(), data.order_tax()])
    tempData.append(["Order Total", "", round(data.order_cost() + data.order_tax(), 2)])
    tempData.append(["Total Items", "", str(len(data.order))])
    make_receipt(tempData, "receipt.pdf")

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
    
    table = Table( data , style = style ) 
    pdf.build([ title , table ])  

def main():
    mainOrder = Order()
    mainOrder.add(Candy("Candy Corn", 1.5, .25))
    mainOrder.add(Candy("Gummy Bears", .25, .35))
    mainOrder.add(Cookie("Chocolate Chip", 6, 3.99))
    mainOrder.add(IceCream("Pistachio", 2, .79))
    mainOrder.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    mainOrder.add(Cookie("Oatmeal Raisin", 2, 3.45))

main()