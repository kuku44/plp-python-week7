# shopping list manager
 
shopping_list = []
while True:
    print("\nadd /remove/show/done")
    choice = input("What would you like to do? ").lower()

    if choice == 'add':
        item = input("Enter an item to add: ")
        shopping_list.append(item)
        print("item has been added to your shopping list.")

    elif choice == 'remove':
        item = input("Enter an item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print("item has been removed from your shopping list.")
        else:
            print("that item is not in your shopping list.")

    elif choice == 'show':
        if shopping_list:
            print("Your shopping list contains:")
            for item in shopping_list:
                print(item)
        else:
            print("Your shopping list is empty.")

    elif choice == 'done':
        print("goodbye!")
    break
