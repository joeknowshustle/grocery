import sys
import json

itemTypes = ["", "Fruit", "Vegetable", "Grain"]

store_items = {
    "Apples": .5,
    "banana's": .99,
    "oranges": .99,
    "Wheat": 2.00
}
store_items2 = {
    "items": [
        {
            "Name": "Apples",
            "Cost": .5,
            "Qty": 10,
            "Type": itemTypes[1]
        },
        {
            "Name": "Banana",
            "Cost": .99,
            "Qty": 10,
            "Type": itemTypes[1]
        },
        {
            "Name": "Oranges",
            "Cost": .99,
            "Qty": 10,
            "Type": itemTypes[1]
        },
        {
            "Name": "Wheat",
            "Cost": 2.00,
            "Qty": 10,
            "Type": itemTypes[3]
        }

    ]
}
shopping_Cart = {
    "items": [

    ]
}


def display_items():
    for key in store_items:
        print(key, ' : ', store_items[key])


def price_check():
    active = True
    while active:
        item_input = input(
            "\nEnter Item to find price press ENTER to return to menu.")
        if item_input in store_items:
            print(store_items[item_input])
        elif item_input == '':
            active = False
        else:
            print("\nitem not found")


def check_out():
    checkout_items = []
    running = True
    while running:
        item_total = input("Enter Item name (Press ENTER to checkout):  ")
        if item_total == '':
            running = False
        item_quantity = input("\nenter quantity")
        item_quantity = int(item_quantity)
        if item_total in store_items:

            checkout_items.append(store_items[f"{item_total}"])
            print(checkout_items)
            check_out_total = f"Total: {sum(checkout_items)* item_quantity}"
            print(check_out_total)

        else:
            print("Item not found")


def change_prices():
    running = True
    while running:
        dict_key = input(
            'Enter item name of price to change: or Enter to return to menu. ')
        if dict_key in store_items:
            print(store_items[f"{dict_key}"])
            new_price = float(input("enter new price: "))
            store_items[f"{dict_key}"] = new_price
            print(f"\n{store_items}")
            price_change_choice = input(
                "would you like to make another price change?(y/n)").capitalize
            if price_change_choice == 'N':
                running = False
        else:
            print("invalid choice")


def del_Items():
    running = True
    while running:
       # key = input("Enter store Item: press enter to return to menu ")
        name = input("Enter the name ")
        for item in store_items2["items"]:
            if(item["Name"] == name):
                item["Qty"] = 0
                print("Successfully Deleted Item  " + name)
                return
        store_items2["items"] = newItem
        print("Unable to find the item " + name)
        more_items = input(
            "is there any more items to remove? (y/n)").capitalize()
        if(more_items == "N"):
            running = False


def add_Items_toStore():
    running = True
    while running:
       # key = input("Enter store Item: press enter to return to menu ")
        name = input("Enter the name ")
        cost = float(input("Enter Price "))
        qty = float(input("Enter qty "))
        type = itemTypes[float(
            input("Enter Type (1) fruit (2) vege (3) grain. "))]
        while not(type == 1 or type == 2 or type == 3):
            type = float(input("Enter Type (1) fruit (2) vege (3) grain."))
        newItem = {
            "Name": name,
            "Cost": cost,
            "Qty": qty,
            "Type": type
        }
        for item in store_items2["items"]:
            if(item["Name"] == name):
                item["Cost"] = cost
                item["Qty"] = qty
                item["Type"] = type
                print("Successfully updated " + name)
                return
        store_items2["items"] = newItem
        print("Successfully Added the item " + name)
        more_items = input(
            "is there any more items to add? (y/n)").capitalize()
        if(more_items == "N"):
            running = False


def management_options(man_selct):
    active = True
    while active:
        if man_selct == '1':
            change_prices()
        elif man_selct == '2':
            add_Items_toStore()
        elif man_selct == '3':
            del_Items()
        elif man_selct == '4':
            active = False
        else:
            print("Invalid option try again")


if __name__ == "__main__":
    print(store_items2)
    active = True
    while active:
        print("\nPlease make a selection from the following choices:")
        print("1) Display Items")
        print("2) Price Check")
        print("3) Management Options")
        print("4) Checkout")
        print("Q) Quit")
        selection_input = input(
            "make selection press ENTER to exit\n").capitalize()
        if selection_input == '1':
            display_items()
        elif selection_input == '2':
            price_check()
        elif selection_input == '3':
            print("\n1)  prices")
            print("2) Add/Update store items.")
            print("3 Delete store items.")
            print("4 Quit.")
            man_selct = input(
                "Make a selection from the following options\n ")
            management_options(man_selct)
        elif selection_input == '4':
            check_out()
        elif selection_input == '':
            break
        elif selection_input == 'Q' or'':
            break
        else:
            print("invalid option Try again")

