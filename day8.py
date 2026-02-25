
def generate_pizza_bill():
    print("---------------------------------")
    print("Pizza Categories")
    print("1.Normal\n2.Delux")
    category = int(input("Enter your Choice [1 or 2]: "))

    print("\nPizza Types")
    print("1.Veg\n2.Non Veg")
    p_type = int(input("Enter your Choice [1 or 2]: "))

   
    base_price = 400.0 if p_type == 2 else 300.0
    
    
    cheese = int(input("\nEnter Cheese? [1.Yes or 2.NO]: "))
    extra_cheese = 100.0 if cheese == 1 else 0.0

    topping = int(input("Enter Topping? [1.Yes or 2.NO]: "))
    extra_toppings = 100.0 if topping == 1 else 0.0

    water = int(input("\nDo you want Water Bottles? [1.Yes or 2.NO]: "))
    water_bill = 0.0
    if water == 1:
        qty = int(input("How many bottles? : "))
        water_bill = qty * 20.0

    ketchup = int(input("\nDo you want Ketchup? [1.Yes or 2.NO]: "))
    ketchup_bill = 0.0
    if ketchup == 1:
        qty = int(input("How many Packets? : "))
        ketchup_bill = qty * 5.0

    drinks = int(input("\nDo you want Soft Driknks? [1.Yes or 2.NO]: "))
    drinks_bill = 0.0
    if drinks == 1:
        qty = int(input("How many Cans? : "))
        drinks_bill = qty * 75.0

    takeaway = int(input("\nIs it a Take Away? [1.Yes or 2.NO]: "))
    takeaway_charge = 20.0 if takeaway == 1 else 0.0

  
    total_cost = base_price + extra_cheese + extra_toppings + water_bill + ketchup_bill + drinks_bill + takeaway_charge
    gst = total_cost * 0.18 
    net_amount = total_cost + gst

    print("\n---------------------------------")
    print("** Pizza Bill Generator **")
    print("---------------------------------")
    print(f"Base Price        = {base_price}")
    print(f"Extra Cheese      = {extra_cheese}")
    print(f"Extra Toppings    = {extra_toppings}")
    print(f"Water Bottle      = {water_bill}")
    print(f"Ketchup Packets   = {ketchup_bill}")
    print(f"Soft Drinks       = {drinks_bill}")
    print(f"Take Away Charges = {takeaway_charge}")
    print("---------------------------------")
    print(f"Total Cost        = {total_cost}")
    print(f"GST Charges       = {round(gst, 2)}")
    print("---------------------------------")
    print(f"Net Amount Payable = {round(net_amount, 2)}")


generate_pizza_bill()

#pseudocode
# push(data)
# if(stack is full):
#    print ("stack Overflow")
# else:
#    top++:
#    stack[top or index]=data

#pwedocode
# pop(data)
# if (stack is empty)
#    print(stack overflow)
# else:
#    top--
#    stack{top or index}=data
   
#peek(data)
# if (stack is empty )
#    print stack overflow 
# else:
#    return the top
#    stack{top or index}=data

#code
# stack=[]

# while True:
#     print("\n1.Push 2. Pop 3.Peek 4.Display 5.exit")
#     choice=int(input("enter choice:"))
#     if choice==1:
#         val=int(input("enter  value"))
#         stack.append(val)
#         print("pushed",val)
#     elif choice==2:
#         if not stack:
#             print("Stack empty")
#         else:
#             print("popped",stack.pop())
#     elif choice==3:
#         if not stack:
#             print("stack empty")
#         else:
#             print("Top")
#     elif choice==4:
#         print("stack",stack)
#     else:
#         print("invalid choice")

# queue=[]

# while True:
#     print("\n1.Push 2. Pop 3.Peek 4.Display 5.exit")
#     choice=int(input("enter choice:"))
#     if choice==1:
#         val=int(input("enter  value"))
#         queue.append(val)
#         print("pushed",val)
#     elif choice==2:
#         if not queue:
#             print("queue empty")
#         else:
#             print("removed",queue.pop())
#     elif choice==3:
#         if not queue:
#             print("queue empty")
#         else:
#             print("front:",queue[0])
#     elif choice==4:
#         print("Queue",queue)
#     elif choice==5:
#         break
#     else:
#         print("invalid choice")


