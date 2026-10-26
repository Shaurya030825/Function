def greet_customers():
    print("Welcome to the Art Supplies Store!")
    print("Get your colours, brushes , and papers here.")
greet_customers()
price_per_items= float(input("Enter the price per art in ruppees: "))
items_bought= int(input("Enter the numb er of art item bought: "))

def calculate_total(price, items):
    total= price*items
    return total

total_cost= calculate_total(price_per_items, items_bought)
rounded_total= round(total_cost,2)
print("Total cost:", rounded_total)

amount_paid= float(input("Enter the amount paid by the customers: "))

def calculate_change(paid, total):
    change= paid- total
    return change

change_due= calculate_change(amount_paid, rounded_total)
rounded_change= round(change_due,2)

def thank_you_message(itmes):
    if itmes >= 5:
        return "Great choice! You picked many art supplies for your project."
    else:
        return "Thanks for shopping at the art suppies store!"

closing_message= thank_you_message(items_bought)

print("")
print("===ART SUPPLIES BILL===")
print("price per item:", price_per_items)
print("Items bought:", items_bought)
print("Total Cost:", rounded_total)
print("Amount paid:", amount_paid)
print("Change Due:", rounded_change)
print(closing_message)
print("===========================")