def process_order(order):
    total = 0
    for item in order["items"]:
        total += item["price"] * item["quantity"]
    print(f"Total: {total}")
    print("Processing payment...")
    print("Payment successful!")
    print("Sending confirmation email...")
    print("Order complete.")

#второй код до и после рефакторинга (сверху до, снизу после)

def calculate_total(order):
    total = 0
    for item in order["items"]:
        price = item["price"]
        quantity = item["quantity"]
        total += price * quantity
    return total


def process_order(order):
    total = calculate_total(order)
    print(f"Total: {total}")
    print("Processing payment...")
    print("Payment successful!")
    print("Sending confirmation email...")
    print("Order complete.")
