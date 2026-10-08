list = []

def createlist():
    global list1

    list1 = []

    listSize = int(input("How many elements do you want to add in list: "))

    for i in range(listSize):
        element = input("Enter element which you want to add in list: ")
        list1.append(element)

    print("List created successfully")
    print("List is:", list1)


def editlist():
    global list1

    if len(list1) == 0:
        print("List is empty")

    else:
        element = input("Enter element which you want to edit: ")

        if element not in list1:
            print("Element is not present in list")

        else:
            print("Current List:", list1)

            index = list1.index(element)

            newElement = input("Enter new element: ")

            list1[index] = newElement

            print("Element updated successfully")
            print("Updated List:", list1)


def deletelist():
    global list1
    if len(list1) == 0:
        print("List is already empty")
    else:
        print("Current List:", list1)

        element = input("Enter element which you want to delete: ")

        if element in list1:
            list1.remove(element)

            print("Element deleted successfully")
            print("Updated List:", list1)

        else:
            print("Element is not present in list")

def viewlist():
    global list1

    if len(list1) == 0:
        print("List is empty")

    else:
        print("Your List is:", list1)


def searchlist():
    global list1

    if len(list1) == 0:
        print("List is empty")

    else:
        element = input("Enter element which you want to search: ")

        if element in list1:
            index = list1.index(element)

            print("Element found")
            print("Element:", element)
            print("Index:", index)

        else:
            print("Element is not present in list")


while True:
    choice = input(
        "\nEnter your choice\n"
        "Press 1. Create New List\n"
        "Press 2. Edit List\n"
        "Press 3. Delete Element\n"
        "Press 4. View List\n"
        "Press 5. Search List\n"
        "Press 6. Exit\n"
        "Enter your choice: "
    )

    print("Choice is: ", choice)

    print("Choice is:", choice)

    if choice == "1":
        createlist()

    elif choice == "2":
        editlist()

    elif choice == "3":
        deletelist()

    elif choice == "4":
        viewlist()

    elif choice == "5":
        searchlist()

    elif choice == "6":
        print("Thank You")
        break

    else:
        print("Invalid choice")
    