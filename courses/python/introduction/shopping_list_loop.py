# Created empty list
shopping_list = []

print("Add items to the list, type STOP when you are done")
while True:
    item = input("Add an item to the list: ")

    if item == 'STOP':
        break

    shopping_list.append(item)

print("Here are the items in the list: ")
for item in shopping_list:
    print(item)
