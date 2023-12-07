# Script Name:	                python-collections
# Author:				        Juan Maldonado
# Date of lastest revision:		12/06/2023
# Purpose:				        This program creates a variable list of elements that can be manipulated by the user.


# This is a welcome message
print("Hello, welcome to Whole Foods!\nI see you are ready to check out. Let's see what you have on you cart.")

# This is a list of whole foods items
my_cart = ["365 Balsamic Vinegar", "Organic Almond Butter", "Canned Wild Tuna", "Whole Food Organic Frozen Blueberries", "Organic Mixed Veggies", "Hu Kitchen Chocolate Bars", "Skinny Pop Popcorn", "KIND Mini Peanut Butter Dark Chocolate Bar", "Mary's Gone Crackers", "Simple Mills Almond Flour"]

# This prints items in cart.
def print_list():
    print("\nItems in the cart:\n", my_cart)

# This prints the 4th item on the cart
print(f"\nFourth element: {my_cart[3]}")

# Print the 6th through 10th item of the cart
print("\nSixth through tenth elements:", my_cart[5:])

# This switches out the 7th item for an onion
my_cart[6] = "onion"

# This prints the updated cart.
print_list()

# These are methods for array manipulation 

# This method adds an item at the end of the cart list
def append_item():
    item = input("\nEnter the item to add at the end of the cart: ")
    my_cart.append(item)
    print_list()

# This removes all items on the cart
def clear_list():
    print("\nThe items on the cart will now be cleared.")
    my_cart.clear()
    print("\nList cleared.")
    print_list()

# This makes a copy of the list of cart items
def copy_list():
    new_list = my_cart.copy()
    print("\nThe original cart list has been copied.")
    print("\nThis is the copied List:", new_list)

# This prints the number of occurances of a specific item in the cart.
def count_item():
    item = input("\nEnter an item in the cart to count: ")
    count = my_cart.count(item)
    print(f"\nCount of {item}: {count}")

# This extends a list
def extend_list():
    new_elements = input("\nEnter new items (comma-separated): ").split(',')
    my_cart.extend(new_elements)
    print_list()

# This returns the place of the first occurrence of a specified item
def index_item():
    item = input("\nEnter the item to find its location: ")
    try:
        index = my_cart.index(item)
        print(f"location of {item}: {index}")
    except ValueError:
        print(f"{item} not found in the cart.")

# This inserts an item at a spacific space in the cart.
def insert_item():
    index = int(input("\nEnter the location to insert at: "))
    item = input("\nEnter the item to insert: ")
    my_cart.insert(index, item)
    print_list()

# This removes and returns the last item on the cart.
def pop_item():
    if my_cart:
        popped_item = my_cart.pop()
        print(f"\nchecked out item: {popped_item}")
        print_list()
    else:
        print("\nThe cart is empty. Cannot pop from an empty cart.")

# This removes the first occurrence of a specified item of the cart
def remove_item():
    item = input("\nEnter the item to remove: ")
    try:
        my_cart.remove(item)
        print_list()
    except ValueError:
        print(f"{item} not found in the list.")

# This reverses the order of the items in the cart
def reverse_list():
    my_cart.reverse()
    print_list()

# This sorts the elements of a list in ascending order
def sort_list():
    my_cart.sort()
    print_list()

# These are options within the case (pretty much a dictionary of functions)
case_dict = {
    "1": append_item,
    "2": clear_list,
    "3": copy_list,
    "4": count_item,
    "5": extend_list,
    "6": index_item,
    "7": insert_item,
    "8": pop_item,
    "9": remove_item,
    "10": reverse_list,
    "11": sort_list,
}

while True:
    # Prompt user for choice
    print("\nChoose a list manipulation option:")
    print("1. append()")
    print("2. clear()")
    print("3. copy()")
    print("4. count()")
    print("5. extend()")
    print("6. index()")
    print("7. insert()")
    print("8. pop()")
    print("9. remove()")
    print("10. reverse()")
    print("11. sort()")
    print("0. Exit")

    choice = input("Enter your choice (0-11): ")

    # This checks user choices, a way to break the loop
    if choice == "0":
        print("\nExiting the program.")
        break
    # This checks if user choice is in dictionary of functions.
    elif choice in case_dict:
        case_dict[choice]()  
    else:
        print("\nInvalid choice. Please enter a number between 0 and 11.")
