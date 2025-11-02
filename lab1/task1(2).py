inventory = {
    "orange": 11,
    "banana": 13,
    "bread": 3,
    "eggs": 4,
    "grapes": 2,
    "pineapple": 15,
    "peach": 16,
}

def update_inventory(product: str, amount: int):
    if product not in inventory:
        inventory[product] = 0
    inventory[product] += amount

    if inventory[product] < 0:
        inventory[product] = 0

update_inventory("grapes", 2)
update_inventory("orange", 10)

low_stock = [product for product, count in inventory.items() if count<5]

print("Inventory:", inventory)
print("Low stock:", low_stock)
