# -*- coding: utf-8 -*-
"""
Student Do: Grocery List.

This script showcases basic operations of Python Lists to help Sally
organize her grocery shopping list.
"""

# @TODO: Create a list of groceries

grocery_list = ["water", "butter", "eggs", "apples", "cinnamon", "sugar", "milk"]



# @TODO: Find the first two items on the list

print(grocery_list[0:2])  
               


# @TODO: Find the last five items on the list

print(grocery_list[0:6])


# @TODO: Find every other item on the list, starting from the second item

print(grocery_list[::2])


# @TODO: Add an element to the end of the list

grocery_list = grocery_list + ["flour"]
print(grocery_list)


# @TODO: Changes a specified element within the list at the given index

grocery_list[3] = "gala apples"
print(grocery_list)


# @TODO: Calculate how many items you have in the list

print(f"You have {len(grocery_list)} items on your grocery list!")


