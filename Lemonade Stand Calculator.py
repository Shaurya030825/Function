def greet_customers():
    print("Welcome to the Lemonade Stand!")
    print("Fresh lemonade, made just for you")
greet_customers()
price_per_cup= float(input("Enter the price per cup in dollars: "))
cups_sold= int(input("Enter the number of cups sold: "))
def calculate_total(price,cups):
    total= price*cups
    return total
total_cost= calculate_total(price_per_cup, cups_sold)
rounded_total= round(total_cost,2)
print("Total_cost:", rounded_total)
amount_paid=float(input("Enter the amount paid by the customer: "))
def calculate_change(paid,total):
    change= paid - total
    return change
change_due= calculate_change(amount_paid, rounded_total)
rounded_change= round(change_due,2)
def thank_you_message(cups):
    if cups>=5:
        return "WOW, Big order! Thanks so much for the support."
    else:
        return "Thanks for shopping by the stand!"
closing_message= thank_you_message(cups_sold)
print("===LEMONADE STAND RECEIPT===")
print("Price per cup:", price_per_cup)
print("Cups Sold:", cups_sold)
print("Total Cost:", rounded_total)
print("Amount Paid:", amount_paid)
print("Change Due:", rounded_change)
print(closing_message)
print("===========================")