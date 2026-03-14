# week8_day2_sales.py

prices = {
“monitor”: 250.0,
“keyboard”: 80.0,
“mouse”: 40.0,
“headset”: 120.0
}

n = int(input())

unique_transactions = set()

for _ in range(n):
order_id = input()
product = input()
unique_transactions.add((order_id, product))

counts = {}

for transaction in unique_transactions:
order_id, product = transaction
if product in counts:
counts[product] += 1
else:
counts[product] = 1

print(f”Unique transactions: {len(unique_transactions)}”)

product_order = [“monitor”, “keyboard”, “mouse”, “headset”]
total_revenue = 0.0

for product in product_order:
if product in counts:
quantity = counts[product]
price = prices[product]
subtotal = quantity * price
print(f”{product}: {quantity} x {price:.2f} = {subtotal:.2f}”)
total_revenue += subtotal

print(f”Total revenue: {total_revenue:.2f}”)