#Define the menue of Restaurant

menue = {
    'pizza':50,
    'pasta':55,
    'Burger':60,
    'salad':70,
    'Coffe':80
}

#Greet 
print('Welcome to python Restaurant')
print("pizza: RS50\n pasta: RS55\n Burger:RS60\n salad:RS70\nCoffe:RS80")

order_total = 0
#80 + 70 = 150

item_1= input("Enter the name item you want to order = ")
if item_1 in menue:
    order_total +=menue[item_1] #0 + 50
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Orderd item {item_1} is not avaialable yet!")

another_order= input("Do you want to add another item? (Yes/No)")
if another_order == 'Yes':
    item_2 = input("Enter the name of second item = ")
    if item_2 in menue:
        order_total += menue[item_2]
        print(f"Item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2} is not available yet!")

print(f"The total amount of items to pay is {order_total}")