# Created empty list
shopping_list = []

# Add the items
shopping_list.append("milk")
shopping_list.append("eggs")
shopping_list.append("bread")
shopping_list.append("butter")
shopping_list.append("orange juice")

print("Shopping list before removing items: " + str(shopping_list))

shopping_list.remove("eggs")
shopping_list.remove("butter")

print("Shopping list after removing items: " + str(shopping_list))
