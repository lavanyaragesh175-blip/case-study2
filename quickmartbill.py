
# quickmartbill.py

cart = [
    {"name": "Notebook", "category": "Stationery", "price": 40, "qty": 5},
    {"name": "Pen", "category": "Stationery", "price": 10, "qty": 11},
    {"name": "Biscuits", "category": "Snacks", "price": 25, "qty": 4},
    {"name": "Juice", "category": "Drinks", "price": 45, "qty": 3},
    {"name": "Chips", "category": "Snacks", "price": 20, "qty": 6},
]


# 1. Line total
def line_total(item):
    return item["price"] * item["qty"]


# 2. Subtotal
def subtotal(cart):
    total = 0
    for item in cart:
        total += line_total(item)
    return total


# 3. Discount
def apply_discount(amount, percent=0):
    return amount - (amount * percent / 100)


# 4. GST
def gst(amount, rate=18):
    return amount * rate / 100


# 5. Category totals
def category_totals(cart):
    totals = {}

    for item in cart:
        category = item["category"]
        total = line_total(item)

        if category in totals:
            totals[category] += total
        else:
            totals[category] = total

    return totals


# 6. Top items
def top_items(cart, n=2):
    sorted_items = sorted(cart, key=line_total, reverse=True)
    names = []

    for item in sorted_items[:n]:
        names.append(item["name"])

    return names


# 7. Print bill
def print_bill(cart, discount_percent=0):
    print(f"{'Item':<10}{'Price':>6}{'Qty':>5}{'Total':>8}")
    print("-" * 29)

    for item in cart:
        print(
            f"{item['name']:<10}"
            f"{item['price']:>6}"
            f"{item['qty']:>5}"
            f"{line_total(item):>8}"
        )

    sub = subtotal(cart)
    discount = sub * discount_percent / 100
    discounted_amount = apply_discount(sub, discount_percent)
    tax = gst(discounted_amount)
    grand_total = discounted_amount + tax

    print("-" * 29)
    print(f"{'Subtotal':<21}{sub:>8.2f}")
    print(f"{'Discount ' + str(discount_percent) + '%':<21}{discount:>8.2f}")
    print(f"{'GST 18%':<21}{tax:>8.2f}")
    print(f"{'Grand total':<21}{grand_total:>8.2f}")
