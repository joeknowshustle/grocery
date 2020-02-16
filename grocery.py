import sys

store_items = {

        "Apples": .5,
    "banana's": .99,
    "oranges": .99,
    "Wheat": 2.00
    }




def display_items():
    for key in store_items:
        print(key, ' : ', store_items[key])
    active = True
    while active:
        input1 = input("press 'r' to return to the main menu else press enter to exit \n")
        if input1 == 'r':
            menu_system()
        elif input1 == '':
            sys.exit(0)
        else:
            print("\ninvalid input")
            continue


def price_check():
    active = True
    while active:
        item_input = input("\nenter Item to find price press ENTER to return to menu ")
        if item_input in store_items:
            print(store_items[item_input])
        elif item_input == '':
            active = False
            menu_system()

            sel_input = input("would you like to make another selection?(y/n) ")

            if sel_input == 'y':
                continue
            elif sel_input == 'n':
                active = False
                menu_system()
        else:
            print("\nitem not found")
            continue

def check_out():
    checkout_items = []
    running = True
    while running:
        item_total = input("Enter Item name (Press ENTER to checkout):  ")
        if item_total =='':
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



def management_options():
    print("\n1)change prices")
    print("2) add/del store items")
    print("3 exit to main menu")

    active = True
    while active:
        man_selct = input("Make a selection from the following options\n ")
        if man_selct == '1':
            active = False

            def change_prices():
                running = True
                while running:
                    dict_key = input('Enter item name of price to change: or Enter to return to menu. ')
                    if dict_key == '':
                        running = False
                        management_options()

                    if dict_key in store_items:
                    # print(store_items[f"{dict_key}"])
                        new_price = input("enter new price: ")
                        new_price = float(new_price)
                        store_items[f"{dict_key}"] = new_price
                        print(f"\n{store_items}")
                        price_change_choice = input("would you like to make another price change?(y/n)")
                        if price_change_choice == 'y':
                            continue
                        elif price_change_choice =='n':
                            running = False
                            management_options()
                else:
                    print("invalid choice")

                    management_options()




            change_prices()
        elif man_selct == '2':
            active = False

            def add_del_items():
                running = True
                while running:
                    key = input("Enter store Item: press enter to return to menu ")
                    if key == '':
                        running = False
                        management_options()
                    try:
                        value = input("Enter Price")

                        value = float(value)
                    except:
                        print("invalid input")
                        continue
                    store_items[key] = value
                    print(store_items)
                    more_items = input("is there any more items to add? (y/n)")
                    if more_items == 'y':
                        continue

                    else:
                        running = False
                        management_options()

                    # int(value)
                    # store_items.update()

            add_del_items()
        elif man_selct == '3':
            active = False
            menu_system()
        else:
            print("invalid option try again")
            continue


def menu_system():
    print("\nPlease make a selection from the following choices:")
    print("1) Display Items")
    print("2) price check")
    print("3) Management options")
    print("4)checkout")
    active = True
    while active:
        selection_input = input("make selection press ENTER to exit\n")
        if selection_input == '1':
            active = False
            display_items()

        elif selection_input == '2':
            active = False
            price_check()


        elif selection_input == '3':
            active = False
            management_options()
        elif selection_input =='4':
            check_out()
        elif selection_input == '':
            active = False
            break
        else:
            print("invalid option Try again")
            continue


menu_system()

menu_system()
