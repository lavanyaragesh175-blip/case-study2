
# main.py

from quickmartbill import (
    cart,
    line_total,
    subtotal,
    apply_discount,
    gst,
    category_totals,
    top_items,
    print_bill
)


def main():

    print("Task 1: Line total")
    print(line_total(cart[0]))

    print("\nTask 2: Subtotal")
    print(subtotal(cart))

    print("\nTask 3: Discount")
    print(apply_discount(500))
    print(apply_discount(500, 10))

    print("\nTask 4: GST")
    print(gst(100))
    print(gst(100, 5))

    print("\nTask 5: Category totals")
    totals = category_totals(cart)

    for category in sorted(totals):
        print(f"{category:<12}{totals[category]}")

    print("\nTask 6: Top items")
    print(top_items(cart))
    print(top_items(cart, 3))

    print("\nTask 7: Bill")
    print_bill(cart, 10)

    # Assert tests
    assert line_total(cart[0]) == 200
    assert subtotal(cart) == 665
    assert apply_discount(500) == 500
    assert apply_discount(500, 10) == 450
    assert gst(100) == 18
    assert gst(100, 5) == 5
    assert category_totals(cart) == {
        "Stationery": 310,
        "Snacks": 220,
        "Drinks": 135
    }
    assert top_items(cart) == ["Notebook", "Juice"]

    print("\nAll tests passed!")


if __name__ == "__main__":
    main()
