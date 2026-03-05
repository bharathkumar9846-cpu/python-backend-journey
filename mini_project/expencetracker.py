expense = []
def add_expenses():
    expense.append({"amount" : int(input("enter amount")), "category" : input("enter")})
def view_expenses():
    for i in expense:
        print(i)
def show_total():
    total = 0
    for b in expense:
            total += b["amount"]
    print("the total :",total)
def show_category_total():
    new_dict={}
    for z in expense:
        if z["category"] in new_dict:
            new_dict[z["category"]] += z["amount"]
        else:
            new_dict[z["category"]] = z["amount"]
    print(new_dict)
while True:
    print("\n1 : Add expense")
    print("2 : View all expenses")
    print("3 : Show total expense")
    print("4 : Show category-wise total")
    print("5 : Exit")

    choice = int(input("Enter choice: "))
    if choice == 1:
       add_expenses()
    elif choice == 2:
         view_expenses()
    elif choice == 4:
          show_category_total()
    elif choice == 3:
         show_total()
    elif choice == 5:
         print("exit")
         break
    else:
        print("invalid")