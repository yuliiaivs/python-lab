sales = [
    {"product": "orange", "quantity": 46, "price": 30},
    {"product": "banana", "quantity": 51, "price": 20},
    {"product": "grapes", "quantity": 30, "price": 15},
    {"product": "strawberry", "quantity": 45, "price": 40},
    {"product": "pineapple", "quantity": 35, "price": 10},
    {"product": "peach", "quantity": 20, "price": 20},
]

def calculate_total_revenue(sales_list):
    revenue = {}
    for sale in sales_list:
        product = sale["product"]
        income = sale["quantity"] * sale["price"]

        if product in revenue:
            revenue[product] += income
        else:
            revenue[product] = income

    return revenue

total_revenue = calculate_total_revenue(sales)

top_products = [product for product, income in total_revenue.items() if income > 1000]

print("Total revenue")
for product, income in total_revenue.items():
    print(f"{product}, {income} uah")

print("Top products > 1000 uah ")
print(top_products)