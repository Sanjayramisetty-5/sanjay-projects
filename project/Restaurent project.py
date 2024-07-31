# define the menu of the restaurent
menu={
    'Chicken pakoda':120,
    'Chicken fry ' : 150,
    'Mutton pakoda ': 180,
    'Mutton keema': 220,
    'Biryani':200,
}

#greeting
print("<<<<<<<<<<  Welcome To Sanjay's Restaurent  >>>>>>>>>>")
print("Chicken pakoda  : Rs 120\nChicken fry : Rs 150\nMutton pakoda : Rs 180\nMutton keema : Rs 220\nBiryani : Rs 200")

order_total = 0
#120 + 220 =340

item_1 = input("Enter a name of item you want to order ---> ")
if item_1 in menu:
    order_total+= menu[item_1]   #0+120
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Your ordered item {item_1} is not available yet! ")

another_order = input("Do you want to add another item?  (yes/no) ")
if another_order=="yes":
    item_2=input("Enter a name of item you want to order ---> ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order")
    else:
        print(f"Your item {item_2} is not available!")
    
    another_order = input("Do you want to add another item?  (yes/no) ")
if another_order=="yes":
    item_3=input("Enter a name of item you want to order ---> ")
    if item_3 in menu:
        order_total += menu[item_3]
        print(f"Your item {item_3} has been added to your order")
    else:
        print(f"Your item {item_3} is not available!")


print(f"The total amount of items to pay is {order_total} ")
print("**********   Thanqyou for visiting   **********")