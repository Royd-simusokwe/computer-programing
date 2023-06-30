#a
inventory = {
    "apples": 10,
    "bananas": 15,
    "oranges": 5
}

#b
print(inventory["bananas"])

#c
inventory.update({"orange": 8})

#d
if "grapes" in inventory:
    print("its in the dictionary")
else:
    print("its not available")

#e
inventory.pop("apples")

#f
print(inventory)